from models.models import Circuit, Driver


class ChampionshipInfoService:

    def __init__(self, database_session):
        self._database_session = database_session

    def get_drivers(self):
        drivers = self._database_session.query(Driver).all()
        return drivers

    def get_driver_by_id(self, driver_id):
        driver = self._database_session.query(Driver).get(driver_id)
        return driver

    def get_circuits(self):
        circuits = self._database_session.query(Circuit).all()
        return circuits

    def get_circuit_by_id(self, circuit_id):
        circuit = self._database_session.query(Circuit).get(circuit_id)
        return circuit
