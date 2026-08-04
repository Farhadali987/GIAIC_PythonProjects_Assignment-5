from sqlalchemy.orm import Session
from app.repositories.base import BaseRepository
from app.models.user import User

class UserService:
    def __init__(self):
        self.repository = BaseRepository(User)

    def get_user(self, db: Session, user_id: int):
        return self.repository.get(db, user_id)
