# SQL (Relational) Databases
- https://fastapi.tiangolo.com/tutorial/sql-databases/

FastAPI는 SQL(관계형) 데이터베이스를 필수적으로 사용할 필요가 없습니다.

그러나 당신이 원한다면 관계형 데이터베이스를 사용할 수 있습니다.

여기에서 [SQLAlchemy](https://www.sqlalchemy.org/)를 사용한 예를 볼 수 있습니다.

다음과 같이 SQLAlchemy에서 지원하는 모든 데이터베이스에 쉽게 적용 할 수 있습니다.

- PostgreSQL
- MySQL
- SQLite
- Oracle
- Microsoft SQL Server, etc.

이 예제에서는 단일 파일을 사용하고 Python이 통합 지원을 제공하기 때문에 SQLite를 사용합니다. 따라서 이 예제를 복사하여 그대로 실행할 수 있습니다.

나중에 상용 애플리케이션의 경우 PostgreSQL과 같은 데이터베이스 서버를 사용할 수 있습니다.

팁
```
Frontend 및 기타 도구를 포함하여 모두 Docker를 기반으로하는 FastAPI 및 PostgreSQL이 포함 된 공식 프로젝트 생성기가 있습니다. https://github.com/tiangolo/full-stack-fastapi-postgresql
```

참고
```
대부분의 코드는 모든 프레임 워크에서 사용하는 표준 SQLAlchemy 코드입니다.

FastAPI 특정 코드는 항상 작습니다.
```

## ORMs

FastAPI는 모든 데이터베이스 및 모든 스타일의 라이브러리와 함께 작동하여 데이터베이스와 통신합니다.

일반적인 패턴은 "ORM": "객체-관계형 매핑"라이브러리를 사용하는 것입니다.

ORM에는 코드의 개체와 데이터베이스 테이블("관계") 간에 변환 ("매핑")하는 도구가 있습니다.

ORM을 사용하면 일반적으로 SQL 데이터베이스의 테이블을 나타내는 클래스를 만들고 클래스의 각 속성은 이름과 유형이 있는 열을 나타냅니다.

예를 들어 `Pet` 클래스는 SQL 테이블 `pets`를 나타낼 수 있습니다.

그리고 해당 클래스의 각 인스턴스 객체는 데이터베이스의 행을 나타냅니다.

예를 들어 개체 `orion_cat` (`Pet`의 인스턴스)은 열 `type`에 대해 `orion_cat.type` 속성을 가질 수 있습니다. 그리고 해당 속성의 값은 다음과 같습니다. `"cat"`

이러한 ORM에는 테이블 또는 엔터티 간의 연결 또는 관계를 만드는 도구도 있습니다.

이런 식으로 `orion_cat.owner` 속성을 가질 수도 있고 소유자는 테이블 소유자에서 가져온 이 애완 동물의 소유자에 대한 데이터를 포함 할 수 있습니다.

따라서 `orion_cat.owner.name`은 이 애완 동물 소유자의 이름 (`owners` 테이블의 `name` 열)이 될 수 있습니다.

`"Arquillian"`과 같은 값을 가질 수 있습니다.

그리고 ORM은 애완 동물 개체에서 액세스하려고 할 때 해당 테이블 소유자로부터 정보를 얻기 위해 모든 작업을 수행합니다.

일반적인 ORM은 예를 들어 Django-ORM (Django 프레임 워크의 일부), SQLAlchemy ORM (SQLAlchemy의 일부, 프레임 워크와 무관) 및 Peewee (프레임 워크와 무관) 등입니다.

여기서는 **SQLAlchemy ORM**을 사용하는 방법을 살펴 보겠습니다.

비슷한 방식으로 다른 ORM을 사용할 수 있습니다.

팁
```
여기 문서에서 Peewee를 사용하는 동등한 기사가 있습니다.
```

## 파일 구조

이 예의 경우 다음과 같은 구조의 `sql_app`이라는 하위 디렉터리가 포함 된 `my_super_project`라는 디렉터리가 있다고 가정합니다.

```
.
└── sql_app
    ├── __init__.py
    ├── crud.py
    ├── database.py
    ├── main.py
    ├── models.py
    └── schemas.py
```

`__init__.py` 파일은 단지 빈 파일이지만 모든 모듈 (Python 파일)이 있는 sql_app이 패키지임을 Python에 알립니다.

이제 각 파일/모듈의 기능을 살펴 보겠습니다.

## SQLAlchemy 파트 만들기

`sql_app/database.py` 파일을 참조하십시오.

### SQLAlchemy 파트 가져 오기

```py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
```

### SQLAlchemy에 대한 데이터베이스 URL 만들기
```py
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
```

이 예에서는 SQLite 데이터베이스에 "연결"하고 있습니다 (SQLite 데이터베이스로 파일 열기).

파일은 `sql_app.db` 파일의 동일한 디렉토리에 있습니다.

이것이 마지막 부분이 `./sql_app.db` 인 이유입니다.

대신 PostgreSQL 데이터베이스를 사용하는 경우 다음 줄의 주석 처리를 제거하면됩니다.

```py
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
```

... 데이터베이스 데이터 및 자격 증명(MySQL, MariaDB 또는 다른 모든 경우에 동일)을 각자의 DB 정보로 수정합니다.

팁
```
이것은 다른 데이터베이스를 사용하려는 경우 수정해야하는 주요 행입니다.
```

### SQLAlchemy 엔진 만들기

첫 번째 단계는 SQLAlchemy "엔진"을 만드는 것입니다.

나중에 다른 곳에서도 이 `엔진`을 사용할 것입니다.

```py
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
```
#### note

```py
connect_args={"check_same_thread": False}
```
... SQLite에만 필요합니다. 다른 데이터베이스에는 필요하지 않습니다.

더 알아보기
```
기본적으로 SQLite는 각 스레드가 독립적 인 요청을 처리한다고 가정하고 하나의 스레드 만 통신하도록 허용합니다.

이는 서로 다른 요청에 대해 실수로 동일한 연결을 공유하는 것을 방지하기위한 것입니다.

그러나 FastAPI에서 일반 함수 (def)를 사용하면 동일한 요청에 대해 둘 이상의 스레드가 데이터베이스와 상호 작용할 수 있으므로 SQLite가 connect_args = { "check_same_thread": False}를 허용해야한다는 것을 알려야합니다.

또한 각 요청이 종속성에서 자체 데이터베이스 연결 세션을 가져 오도록하므로 기본 메커니즘이 필요하지 않습니다.
```

### SessionLocal 클래스 만들기

`SessionLocal` 클래스의 각 인스턴스는 데이터베이스 세션이 됩니다. 클래스 자체는 아직 데이터베이스 세션이 아닙니다.

그러나 `SessionLocal` 클래스의 인스턴스를 생성하면 이 인스턴스가 실제 데이터베이스 세션이됩니다.

SQLAlchemy에서 가져 오는 `Session`과 구별하기 위해 이름을 `SessionLocal`로 지정합니다.

나중에 `Session`(SQLAlchemy에서 가져온 `Session`)을 사용합니다.

`SessionLocal` 클래스를 만들려면 `sessionmaker` 함수를 사용하십시오.

```py
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

### Base 클래스 만들기

이제 클래스를 반환하는 함수 `declarative_base()`를 사용할 것입니다.

나중에 이 클래스에서 상속하여 각 데이터베이스 모델 또는 클래스 (ORM 모델)를 만듭니다.

```py
Base = declarative_base()
```

### 전체 코드

```py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

## 데이터베이스 모델 만들기

이제 `sql_app/models.py` 파일을 보겠습니다.

### Base 클래스에서 SQLAlchemy 모델 만들기

SQLAlchemy 모델을 만들기 위해 이전에 만든 이 Base 클래스를 사용합니다.

팁
```
SQLAlchemy는 "모델"이라는 용어를 사용하여 데이터베이스와 상호 작용하는 이러한 클래스 및 인스턴스를 나타냅니다.

그러나 Pydantic은 "모델"이라는 용어를 사용하여 데이터 유효성 검사, 변환, 문서 클래스 및 인스턴스와 같은 다른 것을 나타냅니다.
```

`database`에서 `Base`를 가져옵니다 (위에서 `database.py` 파일).

상속되는 클래스를 만듭니다.

이러한 클래스는 SQLAlchemy 모델입니다.

```py
from .database import Base

class User(Base):
    __tablename__ = "users"

class Item(Base):
    __tablename__ = "items"
```

`__tablename__` 속성은 SQLAlchemy에게 이러한 각 모델에 대해 데이터베이스에서 사용할 테이블의 이름을 알려줍니다.

### 모델 속성/열 만들기

이제 모든 모델 (클래스) 속성을 만듭니다.

이러한 각 속성은 해당 데이터베이스 테이블의 열을 나타냅니다.

SQLAlchemy의 `Column`을 기본값으로 사용합니다.

그리고 SQLAlchemy 클래스 "type"을 `Integer`, `String` 및 `Boolean`으로 전달합니다. 이 클래스는 데이터베이스의 유형을 인수로 정의합니다.

```py
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Item(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))
```

### 관계 만들기

이제 관계를 만듭니다.

이를 위해 SQLAlchemy ORM에서 제공하는 `relationship`를 사용합니다.

이것은 이 테이블과 관련된 다른 테이블의 값을 포함하는 "마법" 속성이 될 것입니다.

```py
from sqlalchemy.orm import relationship

class User(Base):
    items = relationship("Item", back_populates="owner")

class Item(Base):
    owner = relationship("User", back_populates="items")
```

사용자의 속성 항목에 my_user.items와 같이 액세스 할 때 사용자 테이블 에서 이 레코드를 가리키는 외래 키가 있는 항목의 SQLAlchemy 모델 (항목 테이블에서) 목록이 있습니다.

my_user.items에 액세스하면 SQLAlchemy가 실제로 항목 테이블의 데이터베이스에서 항목을 가져 와서 여기에서 채우십시오.

그리고 항목의 속성 소유자에 액세스 할 때 사용자 테이블의 사용자 SQLAlchemy 모델이 포함됩니다. Owner_ID 속성 / 열을 외래 키로 사용하여 사용자 테이블에서 얻을 수있는 레코드를 알 수 있습니다.

### 전체 코드
```py
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")
```

## Pydantic 모델 생성

이제 `sql_app/schemas.py` 파일을 확인해 봅시다.

팁
```
SQLAlchemy 모델과 Pydantic 모델 간의 혼란을 피하기 위해 SqlAlchemy 모델을 사용하여 models.py과 Pydantic 모델과 함께 schemas.py 파일을 갖게됩니다.

이 일부 Pydantic 모델은 "schema"(유효한 데이터 모양)를 더 많거나 적게 정의합니다.

그래서 이것은 둘 다 사용하는 동안 혼란을 피하고 도움이 될 것입니다.
```

### Pydantic 모델/스키마 만들기

`ItemBase` 및 `UserBase` Pydantic 모델을 만들거나 데이터를 생성하거나 읽는 동안 일반적인 속성을 갖도록 "스키마"라고 말합니다.

또한 동일한 속성을 가지도록 상속하는 `ItemCreate` 및 `UserCreate`를 생성하고 생성에 필요한 추가 데이터(속성)를 생성합니다.

따라서 사용자는 또한 만들 때 비밀번호를 가질 것입니다. 

그러나 보안을 위해 비밀번호는 다른 일부 Pydantic 모델에 있지 않습니다. 예를 들어 사용자를 읽을 때 API에서 전송되지 않습니다.

```py
from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str
```

#### SQLAlchemy 스타일과 Pydantic 스타일

SQLAlchemy 모델은 = 를 사용하여 속성을 정의하고 유형을 다음과 같이 `Column`에 매개 변수로 전달합니다.
```py
name = Column(String)
```

Pydantic 모델은 :를 사용하여 유형을 선언하지만 새로운 유형 주석 구문 / 유형 힌트 :
```py
name: str
```

염두에 두십시오. 따라서 = 및 :를 사용할 때 혼동하지 마십시오.


### 읽기 / 반환을위한 Pydantic 모델 / 스키마 생성

이제 데이터를 읽을 때 사용할 때까지 사용될 Pydantic 모델(스키마)을 API에서 리턴 할 때 사용할 수 있습니다.

예를 들어, 항목을 만들기 전에 해당 항목에 할당된 ID가 무엇인지 알 수 없지만, 항목을 읽을 때(API에서 반환할 때) 해당 ID를 이미 알고 있습니다.

동일한 방법으로 사용자를 읽을 때 이제 항목에 이 사용자의 항목이 포함됨을 선언할 수 있습니다.

이러한 항목의 ID뿐만 아니라 항목을 읽기 위해 Pydantic 모델에서 정의한 모든 데이터도 다음과 같습니다. `Item`.

```py
class Item(ItemBase):
    id: int
    owner_id: int

class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []
```

팁
```
사용자를 읽을 때 (API에서 반환) 사용되는 Pydantic 모델 User에는 암호가 포함되어 있지 않습니다.
```

### Pydantic의 orm_mode 사용

이제 읽기를 위한 Pydantic 모델, Item 및 User에서 내부 Config 클래스를 추가합니다.

이 Config 클래스는 Pydantic에 구성을 제공하는 데 사용됩니다.

Config 클래스에서 orm_mode = True 속성을 설정합니다.

```py
class Item(ItemBase):
    class Config:
        orm_mode = True

class User(UserBase):
    class Config:
        orm_mode = True
```

팁
```
아래와 같이 =로 값을 할당하고 있습니다.

orm_mode = True

:를 사용하지 않습니다 이전의 유형 선언과 마찬가지로.

이것은 유형을 선언하는 것이 아니라 구성 값을 설정하는 것입니다.
```

Pydantic의 orm_mode는 Pydantic 모델이 딕셔너리가 아니라 ORM 모델 (또는 속성이있는 다른 임의의 개체)이더라도 데이터를 읽도록 지시합니다.

이렇게하면 다음과 같이 `dict`에서 id 값을 가져 오는 대신

```py
id = data["id"]
```

또한 다음과 같이 속성에서 가져 오려고 시도합니다.

```py
id = data.id
```

이를 통해 Pydantic 모델은 ORM과 호환되며 경로 작업의 response_model 인수에서 선언 할 수 있습니다.

데이터베이스 모델을 반환 할 수 있으며 여기에서 데이터를 읽습니다.

#### ORM 모드에 대한 기술적 세부 사항

SQLAlchemy 및 기타 많은 기능은 기본적으로 "지연 로딩"입니다.

예를 들어 해당 데이터를 포함 할 속성에 액세스하지 않는 한 데이터베이스에서 관계에 대한 데이터를 가져 오지 않는다는 의미입니다.

예를 들어, 속성 항목에 액세스

```py
current_user.items
```

SQLAlchemy가 항목 테이블로 이동하여 이 사용자에 대한 항목을 가져 오지만 이전에는 가져 오지 않습니다.

`orm_mode`가 없으면 경로 작업에서 SQLAlchemy 모델을 반환하면 관계 데이터가 포함되지 않습니다.

Pydantic 모델에서 이러한 관계를 선언 한 경우에도 마찬가지입니다.

그러나 ORM 모드를 사용하면 Pydantic 자체가 속성 (딕셔너리를 가정하는 대신)에서 필요한 데이터에 액세스하려고 시도하므로 반환하려는 특정 데이터를 선언 할 수 있으며 ORM에서도 가져 와서 가져올 수 있습니다.

### 전체 코드
```py
from typing import List, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True
```

## CRUD 유틸

이제 `sql_app/crud.py` 파일을 보겠습니다.

이 파일에는 데이터베이스의 데이터와 상호 작용하는 재사용 가능한 함수가 있습니다.

CRUD는 생성, 읽기, 업데이트 및 삭제에서 제공됩니다.

...이 예에서 우리는 단지 만들고 읽고 있습니다.

### 데이터 읽기

`sqlalchemy.orm`에서 `Session`을 가져 오면 db 매개 변수의 유형을 선언하고 함수에서 더 나은 유형 검사 및 완성 기능을 사용할 수 있습니다.

`model` (SQLAlchemy 모델) 및 `schemas` (Pydantic 모델/스키마)를 가져옵니다.

다음을위한 유틸리티 함수 생성 :

- ID와 이메일로 단일 사용자를 읽습니다.
- 여러 사용자를 읽습니다.
- 여러 항목을 읽습니다.

```py
from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()
```

팁
```
경로 작업 기능과는 별도로 데이터베이스와 상호 작용(사용자 또는 항목 가져 오기) 전용 기능을 만들면 여러 부분에서 더 쉽게 재사용하고 단위 테스트를 추가 할 수 있습니다.
```

### 데이터 생성

이제 데이터를 만드는 유틸리티 함수를 만듭니다.

단계는 다음과 같습니다.

- 데이터로 SQLAlchemy 모델 인스턴스를 만듭니다.
- `add` 해당 인스턴스 개체를 데이터베이스 세션에 추가하십시오.
- `commit` 변경 사항을 데이터베이스에 커밋하여 저장합니다.
- `refresh` 인스턴스를 새로 고칩니다 (생성 된 ID와 같이 데이터베이스의 새 데이터를 포함하도록).

```py
def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
```

팁
```
User에 대한 SQLAlchemy 모델에는 암호의 보안 해시 버전을 포함해야하는 hashed_password가 포함되어 있습니다.

그러나 API 클라이언트가 제공하는 것은 원래 비밀번호이므로 이를 추출하고 애플리케이션에서 해시 된 비밀번호를 생성해야합니다.

그런 다음 저장할 값과 함께 hashed_password 인수를 전달합니다.
```

경고
```
이 예는 안전하지 않으며 암호는 해시되지 않습니다.

실제 응용 프로그램에서는 암호를 해시하고 일반 텍스트로 저장하지 않아야합니다.

자세한 내용은 자습서의 보안 섹션으로 돌아가십시오.

여기서는 데이터베이스의 도구와 메커니즘에만 초점을 맞추고 있습니다.
```

팁
```
각 키워드 인수를 Item에 전달하고 Pydantic 모델에서 각각을 읽는 대신 다음을 사용하여 Pydantic 모델의 데이터를 사용하여 사전을 생성합니다.

item.dict()

그런 다음 dict의 키-값 쌍을 키워드 인수로 SQLAlchemy 항목에 다음과 함께 전달합니다.

Item(**item.dict())

그런 다음 Pydantic 모델에서 제공하지 않는 추가 키워드 인수 owner_id를 다음과 함께 전달합니다.

Item(**item.dict(), owner_id=user_id)
```


### 전체 코드

```py
from sqlalchemy.orm import Session
from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    fake_hashed_password = user.password + "notreallyhashed"
    db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
```

## Main FastAPI app

이제 `sql_app/main.py` 파일에서 이전에 만든 다른 모든 부분을 통합하고 사용하겠습니다.

### 데이터베이스 테이블 만들기

매우 간단한 방법으로 데이터베이스 테이블을 만듭니다.

```py
models.Base.metadata.create_all(bind=engine)
```

#### Alembic 참고

일반적으로 [Alembic](https://alembic.sqlalchemy.org/en/latest/)을 사용하여 데이터베이스를 초기화 (테이블 생성 등) 할 수 있습니다.

또한 Alembic을 "마이그레이션"(주요 작업)에 사용합니다.

"마이그레이션"은 SQLAlchemy 모델의 구조를 변경하고, 새 속성을 추가하는 등 데이터베이스에서 이러한 변경 사항을 복제하고, 새 열, 새 테이블을 추가하는 등의 작업을 수행 할 때마다 필요한 일련의 단계입니다.

[프로젝트 생성-템플릿의 템플릿](https://fastapi.tiangolo.com/project-generation/)에서 FastAPI 프로젝트에서 Alembic의 예를 찾을 수 있습니다. [특히 소스 코드의 alembic 디렉토리에 있습니다.](https://github.com/tiangolo/full-stack-fastapi-postgresql/tree/master/%7B%7Bcookiecutter.project_slug%7D%7D/backend/app/alembic/)


### 종속성 만들기

정보
```
이 작업을 수행하려면 Python 3.7 이상을 사용하거나 Python 3.6에서 "backports"를 설치해야합니다.

$ pip install async-exit-stack async-generator

이렇게하면 async-exit-stack 및 async-generator가 설치됩니다.

마지막에 설명 된 "middleware"와 함께 대체 방법을 사용할 수도 있습니다.
```

이제 `sql_app/databases.py` 파일에서 만든 `SessionLocal` 클래스를 사용하여 종속성을 만듭니다.

요청마다 독립적 인 데이터베이스 세션/연결 (SessionLocal)이 필요하고 모든 요청에 동일한 세션을 사용한 다음 요청이 완료된 후 닫아야 합니다.

그런 다음 다음 요청을 위해 새 세션이 생성됩니다.

이를 위해 이전에 `yield`를 사용한 [종속성에 대한 섹션](https://fastapi.tiangolo.com/tutorial/dependencies/dependencies-with-yield/)에서 설명한대로 yield를 사용하여 새 종속성을 만듭니다.

우리의 종속성은 단일 요청에 사용될 새 SQLAlchemy `SessionLocal`을 생성 한 다음 요청이 완료되면 닫습니다.

```py
# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

정보
```
SessionLocal() 생성 및 요청 처리를 try 블록에 넣습니다.

그리고 finally 블록에서 닫습니다.

이렇게하면 요청 후에 데이터베이스 세션이 항상 닫힙니다. 요청을 처리하는 동안 예외가 발생하더라도.

그러나 종료 코드에서 다른 예외를 발생시킬 수 없습니다 (yield 후). yield 및 HTTPException이있는 종속성에서 자세히보기
```

그런 다음 경로 연산 함수에서 종속성을 사용할 때 SQLAlchemy에서 직접 가져온 `Session` 유형으로 선언합니다.

그러면 편집기가 `db` 매개 변수가 `Session` 유형임을 알 수 있기 때문에 경로 작업 함수 내에서 더 나은 편집기 지원을 제공합니다.

```py
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    pass


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pass


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    pass


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    pass


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    pass
```

Technical Details
```
db 매개 변수는 실제로 SessionLocal 유형이지만 이 클래스 (sessionmaker()로 생성됨)는 SQLAlchemy 세션의 "proxy"이므로 편집기는 제공되는 메소드를 실제로 알지 못합니다.

그러나 유형을 Session으로 선언함으로써 편집기는 이제 사용 가능한 메서드 (.add(), .query(), .commit() 등)를 알 수 있고 더 나은 지원 (예 : 완료)을 제공 할 수 있습니다. 형식 선언은 실제 개체에 영향을 주지 않습니다.
```

### FastAPI 경로 작업 생성

이제 마지막으로 표준 FastAPI 경로 작업 코드가 있습니다.

```py
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
```

`yield`를 사용하여 종속성의 각 요청 전에 데이터베이스 세션을 생성 한 다음 나중에 닫습니다.

그런 다음 경로 작업 함수에 필요한 종속성을 생성하여 해당 세션을 직접 가져올 수 있습니다.

이를 통해 경로 작업 함수 내부에서 직접 `crud.get_user`를 호출하고 해당 세션을 사용할 수 있습니다.

팁
```
반환하는 값은 SQLAlchemy 모델 또는 SQLAlchemy 모델 목록입니다.

그러나 모든 경로 작업에는 orm_mode를 사용하는 Pydantic 모델/스키마가 포함 된 response_model이 있으므로 Pydantic 모델에서 선언 된 데이터는 모든 일반 필터링 및 유효성 검사와 함께 해당 모델에서 추출되어 클라이언트로 반환됩니다.
```

팁
```
또한 List [schemas.Item]과 같은 표준 Python 유형이있는 response_model이 있습니다.

그러나 해당 목록의 내용/파라미터가 orm_mode가있는 pydantic 모델이므로 데이터는 문제없이 정상적으로 검색되어 클라이언트에 반환됩니다.
```

### def vs async def 정보

여기서는 경로 연산 기능과 종속성 내부에서 SQL Alchemy 코드를 사용하고 있으며 차례로 외부 데이터베이스와 통신합니다.

잠재적으로 "대기"가 필요할 수 있습니다.

그러나 SQLAlchemy는 다음과 같이 await를 직접 사용할 수있는 호환성이 없습니다.

```py
user = await db.query(User).first()
```

... 대신 다음을 사용합니다.

```py
user = db.query(User).first()
```

그런 다음 일반 `def`를 사용하여 `async def` 없이 경로 작업 함수와 종속성을 다음과 같이 선언해야합니다.

```py
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    ...
```

정보
```
관계형 데이터베이스에 비동기 적으로 연결해야하는 경우 비동기 SQL (관계형) 데이터베이스를 참조하십시오.
```

Very Technical Details
```
호기심이 많고 깊은 기술 지식이 있다면 비동기 문서에서이 비동기 def와 def가 어떻게 처리되는지에 대한 매우 기술적 인 세부 사항을 확인할 수 있습니다.
```

### 전체 코드

```py
from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
```

## 마이그레이션
