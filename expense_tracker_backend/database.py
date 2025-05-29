from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "postgresql://neondb_owner:npg_sSR91PLqUmjQ@ep-soft-unit-a81gi8ik-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"

engine = create_engine(
    DATABASE_URL, 
    echo=True,
    connect_args={
        "sslmode": "require",
        "connect_timeout": 30,
    },
    pool_pre_ping=True,
    pool_recycle=300
)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session