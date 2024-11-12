from models.models import Session
from services.championship_info_service import ChampionshipInfoService
from services.races_service import RacesService
from services.standings_service import StandingsService
from services.summaries_service import SummariesService

database_session = Session()

championship_info_service = ChampionshipInfoService(database_session)
races_service = RacesService(database_session)
standings_service = StandingsService(database_session)
summaries_service = SummariesService(database_session)
