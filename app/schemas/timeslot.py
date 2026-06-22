from pydantic import BaseModel
from datetime import datetime


class TimeSlotCreate(BaseModel):
    provider_id: int
    start_time: datetime
    end_time: datetime


class TimeSlotResponse(TimeSlotCreate):
    id: int

    class Config:
        from_attributes = True