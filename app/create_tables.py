from app.core.database import engine, Base

from app.models.customer import Customer
from app.models.provider import Provider
from app.models.timeslot import TimeSlot
from app.models.appointment import Appointment

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")