from models.models import Race


class RacesService:

    def __init__(self, database_session):
        self._database_session = database_session

    def get_races(self):
        races = self._database_session.query(Race).all()
        return races

    def get_race_by_id(self, race_id):
        race = self._database_session.query(Race).get(race_id)
        return race
