from models.models import Session
from services.standings_service import StandingsService
from services.championship_info_service import ChampionshipInfoService

database_session = Session()
standings_service = StandingsService(database_session)
championship_info_service = ChampionshipInfoService(database_session)
