from sqlmodel import Field, SQLModel


class RAG_db(SQLModel):
    filename: str
    directory: str | None
    hash: str


class RAG_Create(RAG_db, table=True):
    id: int | None = Field(default=None, primary_key=True)