from ariadne import QueryType


standings_query = QueryType()


@standings_query.field('hello')
async def standings_resolver(_, __):
    return 'hi!'
