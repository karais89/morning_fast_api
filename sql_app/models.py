# 데이터베이스 모델 만들기
# Base 클래스에서 SQLAlchemy 모델 생성
# SQLAlchemy 모델을 만들기 위해 이전에 만든 Base 클래스를 사용합니다.
# SQLAlchemy는 "model"이라는 용어를 사용하여 데이터베이스와 상호 작용하는 이러한 클래스 및 인스턴스를 나타냅니다.
# 그러나 Pydantic은 "model"이라는 용어를 사용하여 데이터 유효성 검사, 변환, 문서화 클래스 및 인스턴스와 같은 다른 것을 나타냅니다.
from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relation, relationship

# 데이터베이스에서 Base를 가져옵니다 (database.py 파일). 상속되는 클래스를 만듭니다. 이러한 클래스는 SQLAlchemy 모델입니다.
from .database import Base


class User(Base):
    # __tablename__ 속성은 SQLAlchemy에게 이러한 각 모델에 대해 데이터베이스에서 사용할 테이블의 이름을 알려줍니다.
    __tablename__ = "users"

    # 이제 모든 모델 (클래스) 속성을 만듭니다. 이러한 각 속성은 해당 데이터베이스 테이블의 열을 나타냅니다.
    # SQLAlchemy의 열을 기본값으로 사용합니다. 그리고 SQLAlchemy 클래스 "type"을 Integer, String 및 Boolean으로 전달합니다. 이 클래스는 데이터베이스의 유형을 인수로 정의합니다.
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # 이제 관계를 만듭니다. 이를 위해 SQLAlchemy ORM에서 제공하는 관계를 사용합니다.
    # 이것은 이 테이블과 관련된 다른 테이블의 값을 포함하는 "마법" 속성이 될 것입니다.
    # my_user.items에서와 같이 사용자의 속성 항목에 액세스 할 때 사용자 테이블에서 이 레코드를 가리키는 외래 키가 있는 항목 SQLAlchemy 모델(item 테이블의) 목록이 있습니다.
    # my_user.items에 액세스하면 SQLAlchemy는 실제로 항목 테이블의 데이터베이스에서 항목을 가져와 여기에 채 웁니다.
    # 그리고 항목의 속성 소유자에 액세스 할 때 사용자 테이블의 사용자 SQLAlchemy 모델이 포함됩니다. 사용자 테이블에서 가져올 레코드를 알기 위해 외래 키와 함께 owner_id 속성/열을 사용합니다.
    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")