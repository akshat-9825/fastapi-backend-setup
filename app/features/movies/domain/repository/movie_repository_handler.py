from app.common.modules.db_module import DB
from app.features.movies.domain.entities.movie_entity import MovieEntity
from app.features.movies.domain.repository.movie_repository import MovieRepository


class MovieRepositoryHandler(MovieRepository):
    db: DB

    def get_all(self) -> list[MovieEntity]:
        with self.db.session() as session:
            return session.query(MovieEntity).all()
