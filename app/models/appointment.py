from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.database import Base


class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    provider_id = Column(Integer, ForeignKey("providers.id"))

    timeslot_id = Column(Integer, ForeignKey("timeslots.id"))

    status = Column(String, default="BOOKED")