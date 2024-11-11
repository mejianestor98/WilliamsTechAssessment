from ariadne import QueryType

from container import races_service


races_query = QueryType()


@races_query.field('races')
def races_resolver(_, __):
    return races_service.get_races()


@races_query.field('race_by_id')
def race_by_id_resolver(_, __, race_id):
    return races_service.get_race_by_id(race_id)
