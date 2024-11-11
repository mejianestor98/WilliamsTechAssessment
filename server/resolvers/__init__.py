from resolvers.championship_info_resolver import championship_info_query
from resolvers.races_resolver import races_query
from resolvers.standings_resolver import standings_query


resolvers = [
    championship_info_query,
    races_query,
    standings_query
]
