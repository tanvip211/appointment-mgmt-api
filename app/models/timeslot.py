from sqlalchemy import Column, Integer, DateTime, ForeignKey
from app.core.database import Base


class TimeSlot(Base):
    __tablename__ = "timeslots"

    id = Column(Integer, primary_key=True, index=True)

    provider_id = Column(Integer, ForeignKey("providers.id"))

    start_time = Column(DateTime, nullable=False)

    end_time = Column(DateTime, nullable=False)