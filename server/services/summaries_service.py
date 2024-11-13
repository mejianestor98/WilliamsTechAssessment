from dataclasses import dataclass
from datetime import datetime, timedelta

from models.models import Circuit, Driver, LapTime, Race, RaceResult


HOUR_IN_MS = 3600000


@dataclass(frozen=True)
class CircuitSummary:
    circuit_details: Circuit
    fastest_lap: int
    fastest_lap_text: str
    total_races: int


@dataclass(frozen=True)
class DriverSummary:
    driver_details: Driver
    career_podiums: int
    races_entered: int


class SummariesService:

    def __init__(self, database_session) -> None:
        self._database_session = database_session

    def get_circuit_summary(self, circuit_id):
        circuit_details = self._get_circuit_details(circuit_id)
        circuit_races = self._get_races_for_circuit(circuit_id)

        total_races = self._get_total_races(circuit_races)
        circuit_fastest_lap = self._get_fastest_lap_for_circuit(circuit_races)
        lap_time_text = self._milliseconds_to_text(circuit_fastest_lap)

        circuit_summary = CircuitSummary(circuit_details,
                                         circuit_fastest_lap,
                                         lap_time_text,
                                         total_races)

        return circuit_summary

    def get_driver_summary(self, driver_id):
        driver_details = self._get_driver(driver_id)

        driver_race_results = self._get_race_results_for_driver(driver_id)
        driver_podiums = self._get_number_of_podiums(driver_race_results)
        races_entered = self._get_races_entered(driver_race_results)

        driver_summary = DriverSummary(driver_details, driver_podiums, races_entered)
        return driver_summary

    def _get_circuit_details(self, circuit_id):
        circuit = self._database_session.query(Circuit).get(circuit_id)
        return circuit

    def _get_races_for_circuit(self, circuit_id):
        races = self._get_races()
        circuit_races = races.filter(Race.circuit_id == circuit_id)
        return list(circuit_races)

    def _get_race_results_for_driver(self, driver_id):
        race_results = self._database_session.query(RaceResult)
        driver_race_results = race_results.filter(RaceResult.driver_id == driver_id)
        return driver_race_results

    def _get_races_entered(self, race_results):
        return len(list(race_results))

    def _get_number_of_podiums(self, race_results):
        podium_finishes = list(race_results.filter(RaceResult.finishing_position < 4))
        podium_finishes_number = len(podium_finishes)
        return podium_finishes_number

    def _get_races(self):
        return self._database_session.query(Race)

    def _get_total_races(self, circuit_races):
        return len(circuit_races)

    def _get_fastest_lap_for_circuit(self, circuit_races):

        circuit_fastest_lap = HOUR_IN_MS  # init to big value

        for race in circuit_races:
            race_laps = self._get_laps_for_race(race.id)
            race_fastest_lap = self._get_fastest_lap_for_race(race_laps)

            if race_fastest_lap < circuit_fastest_lap:
                circuit_fastest_lap = race_fastest_lap

        return circuit_fastest_lap

    def _get_laps_for_race(self, race_id):
        laps = self._database_session.query(LapTime)
        race_laps = laps.filter(LapTime.race_id == race_id)
        return list(race_laps)

    def _get_fastest_lap_for_race(self, race_laps):
        if race_laps is None or len(race_laps) == 0:
            return HOUR_IN_MS

        race_fastest_lap = min(race_laps, key=lambda lap: lap.milliseconds)
        return race_fastest_lap.milliseconds

    def _get_driver(self, driver_id):
        return self._database_session.query(Driver).get(driver_id)

    def _milliseconds_to_text(self, laptime_milliseconds):
        timedelta_object = timedelta(milliseconds=laptime_milliseconds)
        datetime_object = datetime(year=1970, month=1, day=1) + timedelta_object

        minutes = datetime_object.minute
        seconds = datetime_object.second
        milliseconds = datetime_object.microsecond // 1000

        return f'{minutes:02}:{seconds:02}.{milliseconds:03}'
