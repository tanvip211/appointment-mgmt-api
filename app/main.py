from fastapi import FastAPI

from app.api.customer import router as customer_router
from app.api.provider import router as provider_router
from app.api.timeslot import router as timeslot_router
from app.api.appointment import router as appointment_router

app = FastAPI(
    title="Appointment Management API"
)

app.include_router(customer_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Appointment Management API"
    }

app.include_router(provider_router)
app.include_router(timeslot_router)
app.include_router(appointment_router)