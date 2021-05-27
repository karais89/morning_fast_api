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