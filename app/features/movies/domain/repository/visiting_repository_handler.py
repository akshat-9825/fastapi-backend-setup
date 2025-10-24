from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import func

from app.common.modules.db_module import DB
from app.features.movies.domain.entities.visiting_entity import VisitingEntity
from app.features.movies.domain.repository.visiting_repository import VisitingRepository


class VisitingRepositoryHandler(VisitingRepository):
    db: DB

    def create(self, visiting: VisitingEntity) -> VisitingEntity:
        with self.db.session() as session:
            session.add(visiting)
            session.commit()
            session.refresh(visiting)
            return visiting

    def get_locked_seats(self, show_id: UUID) -> set[int]:
        """Get all currently locked seats for a show (not expired)"""
        with self.db.session() as session:
            now = datetime.utcnow()
            locked_seats_result = (
                session.query(func.unnest(VisitingEntity.seat).label("seat"))
                .filter(
                    VisitingEntity.show_id == show_id, VisitingEntity.expires_at > now
                )
                .all()
            )
            return {row.seat for row in locked_seats_result}

    def cleanup_expired(self, show_id: UUID) -> None:
        """Remove expired visiting records for a show"""
        with self.db.session() as session:
            now = datetime.now(timezone.utc)
            session.query(VisitingEntity).filter(
                VisitingEntity.show_id == show_id, VisitingEntity.expires_at <= now
            ).delete()
            session.commit()
