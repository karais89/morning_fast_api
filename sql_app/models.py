# 데이터베이스 모델 만들기
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

# 데이터베이스에서 Base를 가져옵니다(위에서 database.py 파일).
from .database import Base

# 상속되는 클래스를 만듭니다. 이러한 클래스는 SQLAlchemy 모델입니다.
class User(Base):
    # __tablename__ 속성은 SQLAlchemy에게 이러한 각 모델에 대해 데이터베이스에서 사용할 테이블의 이름을 알려줍니다.
    __tablename__ = "users"
    
    # 모델 속성/열을 만듭니다
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # 관계를 만듭니다.
    # 이를 위해 SQLAlchemy ORM에서 제공하는 "relationship" 함수를 사용합니다. 
    # 이것은이 테이블과 관련된 다른 테이블의 값을 포함하는 "마법"속성이 될 것입니다
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
