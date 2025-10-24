from uuid import UUID

from app.features.movies.application.models.movie_details_model import (
    MovieDetailsResponseModel,
    ShowWithSeatsModel,
)
from app.features.movies.application.models.movie_response_model import (
    MovieResponseModel,
)
from app.features.movies.application.services.movie_service import MovieService
from app.features.movies.domain.repository.movie_repository import MovieRepository
from app.features.movies.domain.repository.show_repository import ShowRepository


class MovieServiceHandler(MovieService):
    repository: MovieRepository
    show_repository: ShowRepository

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

    def get_movie_details(self, movie_id: UUID) -> MovieDetailsResponseModel | None:
        """Get movie details with all shows and available seats."""
        movie = self.repository.get_by_id(movie_id)
        if not movie:
            return None

        # Get all shows for this movie
        shows = self.show_repository.get_by_movie_id(movie_id)
        if not shows:
            return MovieDetailsResponseModel(
                movie_id=movie.movie_id,  # type: ignore
                title=movie.title,  # type: ignore
                duration=movie.duration,  # type: ignore
                shows=[],
            )

        # Get available seats for all shows in one query
        show_ids = [show.show_id for show in shows]
        available_seats_map = self.show_repository.get_available_seats_bulk(show_ids)

        # Build response
        shows_with_seats = [
            ShowWithSeatsModel(
                show_id=show.show_id,
                available_seats=available_seats_map.get(show.show_id, []),
                start_time=show.start_time,
                end_time=show.end_time,
            )
            for show in shows
        ]

        return MovieDetailsResponseModel(
            movie_id=movie.movie_id,  # type: ignore
            title=movie.title,  # type: ignore
            duration=movie.duration,  # type: ignore
            shows=shows_with_seats,
        )
