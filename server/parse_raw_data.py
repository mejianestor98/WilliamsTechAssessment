import json
from pathlib import Path

from models.models import (Session,
                           Circuit,
                           Driver,
                           DriverStanding,
                           LapTime,
                           Race,
                           create_tables)


session = Session()
create_tables()


def load_json(file):
    if Path(file).exists() is False:
        return None

    with open(file, 'r', encoding='utf8') as file:
        data = json.load(file)

    return data


def load_circuits(data_folder):
    circuits_path = Path(f'{data_folder}/circuits.json')
    circuit_data = load_json(circuits_path)

    if circuit_data is None:
        return

    for circuit in circuit_data:
        circuit_model = Circuit(id=circuit['circuitId'],
                                reference=circuit['circuitRef'],
                                name=circuit['name'],
                                location=circuit['location'],
                                country=circuit['country'],
                                latitude=circuit['lat'],
                                longitude=circuit['lng'],
                                altitude=circuit['alt'],
                                url=circuit['url'])
        session.add(circuit_model)
    session.commit()


def load_drivers(data_folder):
    drivers_path = Path(f'{data_folder}/drivers.json')
    driver_data = load_json(drivers_path)

    if driver_data is None:
        return

    for driver in driver_data:
        driver_model = Driver(id=driver['driverId'],
                              reference=driver['driverRef'],
                              number=driver['number'],
                              code=driver['code'],
                              forename=driver['forename'],
                              surname=driver['surname'],
                              date_of_birth=driver['dob'],
                              nationality=driver['nationality'],
                              url=driver['url'])
        session.add(driver_model)
    session.commit()


def load_races(data_folder):
    races_path = Path(f'{data_folder}/races.json')
    race_data = load_json(races_path)

    if race_data is None:
        return

    for race in race_data:
        race_model = Race(id=race['raceId'],
                          year=race['year'],
                          round=race['round'],
                          circuit_id=race['circuitId'],
                          name=race['name'],
                          date=race['date'],
                          time=race['time'],
                          url=race['url'],
                          fp1_date=race['fp1_date'],
                          fp1_time=race['fp1_time'],
                          fp2_date=race['fp2_date'],
                          fp2_time=race['fp2_time'],
                          fp3_date=race['fp3_date'],
                          fp3_time=race['fp3_time'],
                          quali_date=race['quali_date'],
                          quali_time=race['quali_time'],
                          sprint_date=race['sprint_date'],
                          sprint_time=race['sprint_time'])
        session.add(race_model)
    session.commit()


def load_driver_standings(data_folder):
    driver_standings_path = Path(f'{data_folder}/driver_standings.json')
    driver_standings_data = load_json(driver_standings_path)

    if driver_standings_data is None:
        return

    for driver_standing in driver_standings_data:
        driver_standing_model = DriverStanding(id=driver_standing['driverStandingsId'],
                                               race_id=driver_standing['raceId'],
                                               driver_id=driver_standing['driverId'],
                                               points=driver_standing['points'],
                                               position=driver_standing['position'],
                                               position_text=driver_standing['positionText'],
                                               wins=driver_standing['wins'])
        session.add(driver_standing_model)
    session.commit()


def load_lap_times(data_folder):
    lap_times_path = Path(f'{data_folder}/lap_times.json')
    lap_times_data = load_json(lap_times_path)

    if lap_times_data is None:
        return None

    for lap_time in lap_times_data:
        lap_time_model = LapTime(race_id=lap_time['raceId'],
                                 driver_id=lap_time['driverId'],
                                 lap=lap_time['lap'],
                                 position=lap_time['position'],
                                 time=lap_time['time'],
                                 milliseconds=lap_time['milliseconds'])
        session.add(lap_time_model)
    session.commit()


def parse_data(base_folder):
    load_circuits(base_folder)
    load_drivers(base_folder)
    load_races(base_folder)
    load_lap_times(base_folder)
    load_driver_standings(base_folder)
    session.close()


if __name__ == '__main__':  # TODO: use click to dynamically set the dataset folder
    parse_data('./dataset')
