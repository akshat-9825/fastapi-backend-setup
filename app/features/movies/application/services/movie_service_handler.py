from app.features.movies.application.models.movie_response_model import (
    MovieResponseModel,
)
from app.features.movies.application.services.movie_service import MovieService
from app.features.movies.domain.repository.movie_repository import MovieRepository


class MovieServiceHandler(MovieService):
    repository: MovieRepository

    def get_movies(self) -> list[MovieResponseModel]:
        """Get all movies."""
        entities = self.repository.get_all()

        transformed_entities = [
            MovieResponseModel(
                movie_id=entity.movie_id,  # type: ignore
                title=entity.title,  # type: ignore
                duration=entity.duration,  # type: ignore
            )
            for entity in entities
        ]

        return transformed_entities
