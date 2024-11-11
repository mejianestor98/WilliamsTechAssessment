from ariadne import QueryType

from container import standings_service


standings_query = QueryType()


@standings_query.field('driver_standings')
async def standings_resolver(_, __, race_id):
    return standings_service.get_driver_standings(race_id)
