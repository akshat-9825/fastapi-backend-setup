"""Database Dependency Injection Module"""

from injector import Module, provider, singleton
from sqlalchemy import Engine

from app.database import SessionLocal, engine


class DB:
    """
    Database service wrapper.
    Simple pattern matching company standard.
    """

    def __init__(self, engine: Engine):
        self.engine = engine
        self.session = SessionLocal


class DbModule(Module):
    """
    Provides database service as a singleton.
    Use this in other modules to inject database dependencies.
    """

    @provider
    @singleton
    def provide_db(self) -> DB:
        """
        Provide DB service for creating database sessions.

        Usage in repositories:
            class UserRepositoryHandler(UserRepository):
                db: DB  # Injector will set this

                def get_all(self):
                    with self.db.session() as session:
                        return session.query(User).all()
        """
        return DB(engine=engine)
