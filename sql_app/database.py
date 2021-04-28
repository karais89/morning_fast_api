# sqlalchemy 임포트 하기
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy에 대한 데이터베이스 URL 만들기
# 이 예에서는 SQLite 데이터베이스에 "연결"하고 있습니다 (SQLite 데이터베이스로 파일 열기)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# SQLAlchemy 엔진 만들기
# connect_args={"check_same_thread": False} SQLite에만 필요합니다. 다른 데이터베이스에는 필요하지 않습니다.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal 클래스 생성
# SessionLocal 클래스의 각 인스턴스는 데이터베이스 세션이 됩니다. 
# 클래스 자체는 아직 데이터베이스 세션이 아닙니다.
# 나중에 세션 (SQLAlchemy에서 가져온 세션)을 사용합니다.
# SessionLocal 클래스를 만들려면 sessionmaker 함수를 사용하십시오
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base 클래스 생성
# 이제 클래스를 반환하는 함수 declarative_base()를 사용할 것입니다
# 나중에이 클래스에서 상속하여 각 데이터베이스 모델 또는 클래스 (ORM 모델)를 만듭니다.
Base = declarative_base()