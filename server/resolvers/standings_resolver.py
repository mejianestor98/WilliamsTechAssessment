from ariadne import QueryType

from container import standings_service


standings_query = QueryType()


@standings_query.field('hello')
async def standings_resolver(_, __):
    return standings_service.get_driver_standings()
