from ariadne import QueryType

from container import summaries_service

summaries_query = QueryType()


@summaries_query.field('circuit_summary')
def circuit_summary_resolver(_, __, circuit_id):
    return summaries_service.get_circuit_summary(circuit_id)


@summaries_query.field('driver_summary')
def driver_summary_resolver(_, __, driver_id):
    return summaries_service.get_driver_summary(driver_id)
