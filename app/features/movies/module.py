from injector import Module, provider, singleton

from app.common.modules.db_module import DB
from app.features.movies.application.services.booking_service import BookingService
from app.features.movies.application.services.booking_service_handler import (
    BookingServiceHandler,
)
from app.features.movies.application.services.movie_service import MovieService
from app.features.movies.application.services.movie_service_handler import (
    MovieServiceHandler,
)
from app.features.movies.application.services.show_service import ShowService
from app.features.movies.application.services.show_service_handler import (
    ShowServiceHandler,
)
from app.features.movies.domain.repository.booking_repository import BookingRepository
from app.features.movies.domain.repository.booking_repository_handler import (
    BookingRepositoryHandler,
)
from app.features.movies.domain.repository.movie_repository import MovieRepository
from app.features.movies.domain.repository.movie_repository_handler import (
    MovieRepositoryHandler,
)
from app.features.movies.domain.repository.show_repository import ShowRepository
from app.features.movies.domain.repository.show_repository_handler import (
    ShowRepositoryHandler,
)


class MovieModule(Module):
    @provider
    @singleton
    def provide_movie_repository(self, db: DB) -> MovieRepository:
        return MovieRepositoryHandler(db=db)

    @provider
    @singleton
    def provide_movie_service(
        self, repository: MovieRepository, show_repository: ShowRepository
    ) -> MovieService:
        return MovieServiceHandler(
            repository=repository, show_repository=show_repository
        )

    @provider
    @singleton
    def provide_show_repository(self, db: DB) -> ShowRepository:
        return ShowRepositoryHandler(db=db)

    @provider
    @singleton
    def provide_show_service(self, repository: ShowRepository) -> ShowService:
        return ShowServiceHandler(repository=repository)

    @provider
    @singleton
    def provide_booking_repository(self, db: DB) -> BookingRepository:
        return BookingRepositoryHandler(db=db)

    @provider
    @singleton
    def provide_booking_service(
        self, repository: BookingRepository, show_repository: ShowRepository
    ) -> BookingService:
        return BookingServiceHandler(
            repository=repository, show_repository=show_repository
        )
