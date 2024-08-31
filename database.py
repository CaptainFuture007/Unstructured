from sqlmodel import Field, SQLModel, create_engine
from sqlite_db_schema import RAG_db, RAG_Create

sqlite_file_name = "database.db"  
sqlite_url = f"sqlite:///{sqlite_file_name}"  


engine = create_engine(sqlite_url, echo=True)  


def create_db_and_tables():  
    SQLModel.metadata.create_all(engine)  

# More code here later 👈

if __name__ == "__main__":  
    create_db_and_tables() 