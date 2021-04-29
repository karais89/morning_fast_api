from sqlalchemy.orm import Session

from . import models, schemas

# id로 단일 사용자를 읽습니다.
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# email로 단일 사용자를 읽습니다.
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

# 여러 사용자를 읽습니다.
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()