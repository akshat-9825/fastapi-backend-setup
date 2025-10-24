from injector import Module, provider, singleton

from app.common.modules.db_module import DB
from app.features.movies.application.services.movie_service import MovieService
from app.features.movies.application.services.movie_service_handler import (
    MovieServiceHandler,
)
from app.features.movies.domain.repository.movie_repository import MovieRepository
from app.features.movies.domain.repository.movie_repository_handler import (
    MovieRepositoryHandler,
)


class MovieModule(Module):
    @provider
    @singleton
    def provide_movie_repository(self, db: DB) -> MovieRepository:
        return MovieRepositoryHandler(db=db)

    @provider
    @singleton
    def provide_movie_service(self, repository: MovieRepository) -> MovieService:
        return MovieServiceHandler(repository=repository)
