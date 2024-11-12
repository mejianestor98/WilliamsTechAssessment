from ariadne import QueryType

from container import summaries_service

summaries_query = QueryType()


@summaries_query.field('circuit_summary')
def circuit_summary_resolver(_, __, circuit_id):
    return summaries_service.get_circuit_summary(circuit_id)
