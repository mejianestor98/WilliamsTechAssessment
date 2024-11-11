from ariadne import QueryType

from container import races_service


races_query = QueryType()


@races_query.field('races')
def races_resolver(_, __):
    return races_service.get_races()


@races_query.field('race_by_id')
def race_by_id_resolver(_, __, race_id):
    return races_service.get_race_by_id(race_id)


@races_query.field('lap_times_for_race')
def lap_times_for_race_resolver(_, __, race_id):
    return races_service.get_lap_times_for_race(race_id)


@races_query.field('lap_times_for_race_and_driver')
def lap_times_for_race_and_driver_resolver(_, __, race_id, driver_id):
    return None
