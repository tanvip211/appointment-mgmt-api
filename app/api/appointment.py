from fastapi import APIRouter, Depends, HTTPException
import sqlalchemy
from sqlalchemy.orm import Session
from typing import Optional
from datetime import date

from app.core.dependencies import get_db
from app.models.appointment import Appointment
from app.models.timeslot import TimeSlot
from app.schemas.appointment import (
    AppointmentCreate,
    AppointmentResponse
)

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.post("/", response_model=AppointmentResponse)
def create_appointment(
    appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):
    existing_appointment = (
        db.query(Appointment)
        .filter(
            Appointment.timeslot_id ==
            appointment.timeslot_id
        )
        .first()
    )

    if existing_appointment:
        raise HTTPException(
            status_code=400,
            detail="This time slot is already booked"
        )

    db_appointment = Appointment(
        customer_id=appointment.customer_id,
        provider_id=appointment.provider_id,
        timeslot_id=appointment.timeslot_id
    )

    db.add(db_appointment)

    db.commit()

    db.refresh(db_appointment)

    return db_appointment


@router.get("/", response_model=list[AppointmentResponse])
def get_appointments(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db)
):
    return (
        db.query(Appointment)
        .offset(skip)
        .limit(limit)
        .all()
    )


@router.get("/{appointment_id}",
            response_model=AppointmentResponse)
def get_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    return appointment


@router.put("/{appointment_id}",
            response_model=AppointmentResponse)
def update_appointment(
    appointment_id: int,
    updated_appointment: AppointmentCreate,
    db: Session = Depends(get_db)
):
    appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    appointment.customer_id = updated_appointment.customer_id
    appointment.provider_id = updated_appointment.provider_id
    appointment.timeslot_id = updated_appointment.timeslot_id

    db.commit()
    db.refresh(appointment)

    return appointment


@router.delete("/{appointment_id}")
def delete_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    db.delete(appointment)
    db.commit()

    return {
        "message": "Appointment deleted successfully"
    }

@router.put("/{appointment_id}/cancel")
def cancel_appointment(
    appointment_id: int,
    db: Session = Depends(get_db)
):
    appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    appointment.status = "CANCELLED"

    db.commit()

    return {
        "message": "Appointment cancelled successfully"
    }

@router.put("/{appointment_id}/reschedule")
def reschedule_appointment(
    appointment_id: int,
    new_timeslot_id: int,
    db: Session = Depends(get_db)
):
    appointment = (
        db.query(Appointment)
        .filter(Appointment.id == appointment_id)
        .first()
    )

    if not appointment:
        raise HTTPException(
            status_code=404,
            detail="Appointment not found"
        )

    existing_appointment = (
        db.query(Appointment)
        .filter(
            Appointment.timeslot_id == new_timeslot_id
        )
        .first()
    )

    if existing_appointment:
        raise HTTPException(
            status_code=400,
            detail="New time slot already booked"
        )

    appointment.timeslot_id = new_timeslot_id

    db.commit()

    return {
        "message": "Appointment rescheduled successfully"
    }

@router.get("/search/")
def search_appointments(
    customer_id: Optional[int] = None,
    provider_id: Optional[int] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Appointment)

    if customer_id:
        query = query.filter(
            Appointment.customer_id == customer_id
        )

    if provider_id:
        query = query.filter(
            Appointment.provider_id == provider_id
        )

    return query.all()

@router.get("/search-by-date/")
def search_by_date(
    search_date: date,
    db: Session = Depends(get_db)
):
    return (
        db.query(Appointment)
        .join(
            TimeSlot,
            Appointment.timeslot_id == TimeSlot.id
        )
        .filter(
            TimeSlot.start_time.cast(
                sqlalchemy.Date
            ) == search_date
        )
        .all()
    )