from uuid import UUID

from app.features.movies.application.models.show_response_model import ShowResponseModel
from app.features.movies.application.services.show_service import ShowService
from app.features.movies.domain.repository.show_repository import ShowRepository


class ShowServiceHandler(ShowService):
    repository: ShowRepository

    def get_shows(self) -> list[ShowResponseModel]:
        entities = self.repository.get_all()
        return [ShowResponseModel.model_validate(entity) for entity in entities]

    def get_show_by_id(self, show_id: UUID) -> ShowResponseModel | None:
        entity = self.repository.get_by_id(show_id)
        if not entity:
            return None
        return ShowResponseModel.model_validate(entity)

    def get_shows_by_movie(self, movie_id: UUID) -> list[ShowResponseModel]:
        entities = self.repository.get_by_movie_id(movie_id)
        return [ShowResponseModel.model_validate(entity) for entity in entities]

    def get_available_seats(self, show_id: UUID) -> list[int]:
        return self.repository.get_available_seats(show_id)
