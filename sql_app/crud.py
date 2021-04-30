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

# 이제 데이터를 생성하는 유틸리티 함수를 생성합니다.
# 단계는 다음과 같습니다.
# 1. 데이터로 SQLAlchemy 모델 인스턴스를 만듭니다.
# 2. add: 해당 인스턴스 개체를 데이터베이스 세션에 추가
# 3. commit: 변경 사항을 데이터베이스에 커밋하여 저장
# 4. refresh: 인스턴스를 새로 고칩니다 (생성 된 ID와 같이 데이터베이스의 새 데이터를 포함하도록).
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhased"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Items 항목을 읽습니다.
def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


# 각 키워드 인수를 Item에 전달하고 Pydantic 모델에서 각각을 읽는 대신 다음을 사용하여 Pydantic 모델의 데이터로 dict를 생성합니다.
# item.dict()
# 그런 다음 dict의 키-값 쌍을 키워드 인수로 SQLAlchemy 항목에 다음과 함께 전달합니다.
# Item(**item.dict())
# 그런 다음 Pydantic 모델에서 제공하지 않는 추가 키워드 인수 owner_id를 다음과 함께 전달합니다.
# Item(**item.dict(), owner_id=user_id)
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item