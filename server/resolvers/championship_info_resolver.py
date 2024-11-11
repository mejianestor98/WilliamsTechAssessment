from ariadne import QueryType

from container import championship_info_service

championship_info_query = QueryType()


@championship_info_query.field('drivers')
def drivers_resolver(_, __):
    return championship_info_service.get_drivers()


@championship_info_query.field('driver_by_id')
def driver_by_id_resolver(_, __, driver_id):
    return championship_info_service.get_driver_by_id(driver_id)


@championship_info_query.field('circuits')
def circuits_resolver(_, __):
    return championship_info_service.get_circuits()


@championship_info_query.field('circuit_by_id')
def circuit_by_id_resolver(_, __, circuit_id):
    return championship_info_service.get_circuit_by_id(circuit_id)
