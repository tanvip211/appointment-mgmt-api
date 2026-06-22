from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.timeslot import TimeSlot
from app.schemas.timeslot import (
    TimeSlotCreate,
    TimeSlotResponse
)

router = APIRouter(
    prefix="/timeslots",
    tags=["TimeSlots"]
)


@router.post("/", response_model=TimeSlotResponse)
def create_timeslot(
    timeslot: TimeSlotCreate,
    db: Session = Depends(get_db)
):
    db_timeslot = TimeSlot(
        provider_id=timeslot.provider_id,
        start_time=timeslot.start_time,
        end_time=timeslot.end_time
    )

    db.add(db_timeslot)
    db.commit()
    db.refresh(db_timeslot)

    return db_timeslot


@router.get("/", response_model=list[TimeSlotResponse])
def get_timeslots(
    db: Session = Depends(get_db)
):
    return db.query(TimeSlot).all()


@router.get("/{timeslot_id}",
            response_model=TimeSlotResponse)
def get_timeslot(
    timeslot_id: int,
    db: Session = Depends(get_db)
):
    timeslot = (
        db.query(TimeSlot)
        .filter(TimeSlot.id == timeslot_id)
        .first()
    )

    if not timeslot:
        raise HTTPException(
            status_code=404,
            detail="TimeSlot not found"
        )

    return timeslot


@router.put("/{timeslot_id}",
            response_model=TimeSlotResponse)
def update_timeslot(
    timeslot_id: int,
    updated_timeslot: TimeSlotCreate,
    db: Session = Depends(get_db)
):
    timeslot = (
        db.query(TimeSlot)
        .filter(TimeSlot.id == timeslot_id)
        .first()
    )

    if not timeslot:
        raise HTTPException(
            status_code=404,
            detail="TimeSlot not found"
        )

    timeslot.provider_id = updated_timeslot.provider_id
    timeslot.start_time = updated_timeslot.start_time
    timeslot.end_time = updated_timeslot.end_time

    db.commit()
    db.refresh(timeslot)

    return timeslot


@router.delete("/{timeslot_id}")
def delete_timeslot(
    timeslot_id: int,
    db: Session = Depends(get_db)
):
    timeslot = (
        db.query(TimeSlot)
        .filter(TimeSlot.id == timeslot_id)
        .first()
    )

    if not timeslot:
        raise HTTPException(
            status_code=404,
            detail="TimeSlot not found"
        )

    db.delete(timeslot)
    db.commit()

    return {
        "message": "TimeSlot deleted successfully"
    }