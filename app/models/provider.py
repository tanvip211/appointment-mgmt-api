from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Provider(Base):
    __tablename__ = "providers"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    specialization = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)