from sqlmodel import create_engine, Session

sqlite_file_name = "DBFASTAPI.db"
sqlite_url = f"sqlite:///{sqlite_Mathias_Rivera}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session