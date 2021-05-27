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