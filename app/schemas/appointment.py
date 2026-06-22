from pydantic import BaseModel


class AppointmentCreate(BaseModel):
    customer_id: int
    provider_id: int
    timeslot_id: int


class AppointmentResponse(AppointmentCreate):
    id: int
    status: str

    class Config:
        from_attributes = True