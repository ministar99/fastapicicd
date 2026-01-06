from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# TODO: 실제 MySQL 접속 정보로 수정하세요.
# 예: mysql+pymysql://user:password@localhost:3306/shopdb
MYSQL_URL = "mysql+pymysql://root:32655190@localhost:3306/shopdb"

engine = create_engine(MYSQL_URL, echo=False, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
