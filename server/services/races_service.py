from models.models import LapTime, Race


class RacesService:

    def __init__(self, database_session):
        self._database_session = database_session

    def get_races(self):
        races = self._database_session.query(Race).all()
        return races

    def get_race_by_id(self, race_id):
        race = self._database_session.query(Race).get(race_id)
        return race

    def get_lap_times_for_race(self, race_id):
        lap_times = self._database_session.query(LapTime)
        if lap_times is None:
            return None

        race_lap_times = lap_times.filter(LapTime.race_id == race_id)
        return race_lap_times

    def get_lap_times_for_race_and_driver(self, race_id, driver_id):
        race_lap_times = self.get_lap_times_for_race(race_id)
        if race_lap_times is None:
            return None

        driver_lap_times = race_lap_times.filter(LapTime.driver_id == driver_id)
        return driver_lap_times
