from database import Base, engine
import models

Base.metadata.create_all(bind=engine)

class Settings:
    DATABASE_URL = "sqlite:///./test.db"

settings = Settings()
