from sqlmodel import create_engine, SQLModel

DATABASE_URL = "sqlite:///./test.db"

en_connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, echo=True, connect_args=en_connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)