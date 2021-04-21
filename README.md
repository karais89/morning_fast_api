# morning_fast_api
fast api 연습

## 세팅

### 파이썬 설치
- https://www.python.org/downloads/
v3.9.4

### 가상환경 설정

```bash
python -m venv venv
```

### vscode 확장 플러그인 설치

- Python (파이썬 기본 자동완성)
- Pylance (자동완성 강화)
- GitHub Pull Requests and Issues
- Python Test Explorer for Visual Studio Code

### FastAPI 설정

```bash
pip install fastapi
pip install uvicorn[standard]
```

### 서버 실행
```
uvicorn main:app --reload
```

### doc
- 스웨거 UI
- redoc 문서

### Recap

요약하면 매개 변수, 본문 등의 유형을 함수 매개 변수로 한 번 선언합니다.

표준 최신 Python 유형으로 수행합니다.

새로운 구문, 특정 라이브러리의 메서드 또는 클래스 등을 배울 필요가 없습니다.

- 데이터 검증
- 입력 데이터 변환 : 네트워크에서 Python 데이터 및 유형으로. 읽기
- 출력 데이터 변환 : Python 데이터 및 유형에서 네트워크 데이터 (JSON)로 변환
- 2 개의 대체 사용자 인터페이스를 포함한 자동 대화 형 API 문서

### 벤치마크

독립적인 TechEmpower 벤치 마크에 따르면 Uvicorn에서 실행되는 FastAPI 애플리케이션은 사용 가능한 가장 빠른 Python 프레임 워크 중 하나로 Starlette 및 vicorn 자체 (FastAPI에서 내부적으로 사용됨)보다 낮습니다. (*)

이에 대한 자세한 내용은 벤치 마크 섹션을 참조하십시오.

## 튜토리얼

### SQL (Relational) Databases

FastAPI는 SQL(관계형) 데이터베이스를 반드시 사용할 필요는 없습니다.

그러나 관계형 데이터베이스 사용을 원하는 경우 사용할 수 있습니다.

여기에서 [SQLAlchemy](https://www.sqlalchemy.org/)를 사용한 예를 볼 수 있습니다.

다음과 같이 SQLAlchemy에서 지원하는 모든 데이터베이스에 쉽게 적용 할 수 있습니다.
- PostgreSQL
- MySQL
- SQLite
- Oracle
- Microsoft SQL Server, etc.
이 예제에서는 단일 파일을 사용하고 Python이 통합 지원을 제공하기 때문에 SQLite를 사용합니다. 따라서이 예제를 복사하여 그대로 실행할 수 있습니다.
나중에 프로덕션 애플리케이션의 경우 PostgreSQL과 같은 데이터베이스 서버를 사용할 수 있습니다.

### ORMs

FastAPI는 모든 데이터베이스 및 모든 스타일의 라이브러리와 함께 작동하여 데이터베이스와 통신합니다.

일반적인 패턴은 "ORM": "객체-관계형 매핑"라이브러리를 사용하는 것입니다.

ORM에는 코드의 개체와 데이터베이스 테이블("관계")간에 변환("매핑")하는 도구가 있습니다.

ORM을 사용하면 일반적으로 SQL 데이터베이스의 테이블을 나타내는 클래스를 만들고 클래스의 각 속성은 이름과 유형이 있는 열을 나타냅니다.

예를 들어 Pet 클래스는 SQL 테이블 pets를 나타낼 수 있습니다.

그리고 해당 클래스의 각 인스턴스 객체는 데이터베이스의 행을 나타냅니다.

예를 들어 개체 orion_cat(Pet의 인스턴스)은 열 type에 대해 orion_cat.type 속성을 가질 수 있습니다. 그리고 해당 속성의 값은 다음과 같습니다. "cat".

이러한 ORM에는 테이블 또는 엔터티 간의 연결 또는 관계를 만드는 도구도 있습니다.

이런 식으로 orion_cat.owner 속성을 가질 수도 있고 소유자는 테이블 소유자에서 가져온이 애완 동물의 소유자에 대한 데이터를 포함 할 수 있습니다.

따라서 orion_cat.owner.name은 이 애완 동물 소유자의 이름(owners 테이블의 이름 열)이 될 수 있습니다.

"Arquillian"과 같은 값을 가질 수 있습니다.

그리고 ORM은 애완 동물 개체에서 액세스하려고 할 때 해당 테이블 소유자로부터 정보를 얻기 위해 모든 작업을 수행합니다.

일반적인 ORM은 예를 들어 Django-ORM (Django 프레임 워크의 일부), SQLAlchemy ORM (SQLAlchemy의 일부, 프레임 워크와 무관) 및 Peewee (프레임 워크와 무관) 등입니다.

여기서는 SQLAlchemy ORM을 사용하는 방법을 살펴 보겠습니다.

비슷한 방식으로 다른 ORM을 사용할 수 있습니다.

