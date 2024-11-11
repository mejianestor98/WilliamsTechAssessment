from models.models import DriverStanding


class StandingsService:

    def __init__(self, database_session) -> None:
        self._database_session = database_session

    def get_driver_standings(self, race_id):
        driver_standings = self._database_session.query(DriverStanding)
        if driver_standings is None:
            return None

        race_driver_standings = driver_standings.filter(DriverStanding.race_id == race_id)
        return race_driver_standings
