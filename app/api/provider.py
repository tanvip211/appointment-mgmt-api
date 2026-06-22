from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.models.provider import Provider
from app.schemas.provider import (
    ProviderCreate,
    ProviderResponse
)

router = APIRouter(
    prefix="/providers",
    tags=["Providers"]
)


@router.post("/", response_model=ProviderResponse)
def create_provider(
    provider: ProviderCreate,
    db: Session = Depends(get_db)
):
    db_provider = Provider(
        name=provider.name,
        specialization=provider.specialization,
        email=provider.email
    )

    db.add(db_provider)
    db.commit()
    db.refresh(db_provider)

    return db_provider


@router.get("/", response_model=list[ProviderResponse])
def get_providers(
    db: Session = Depends(get_db)
):
    return db.query(Provider).all()


@router.get("/{provider_id}",
            response_model=ProviderResponse)
def get_provider(
    provider_id: int,
    db: Session = Depends(get_db)
):
    provider = (
        db.query(Provider)
        .filter(Provider.id == provider_id)
        .first()
    )

    if not provider:
        raise HTTPException(
            status_code=404,
            detail="Provider not found"
        )

    return provider


@router.put("/{provider_id}",
            response_model=ProviderResponse)
def update_provider(
    provider_id: int,
    updated_provider: ProviderCreate,
    db: Session = Depends(get_db)
):
    provider = (
        db.query(Provider)
        .filter(Provider.id == provider_id)
        .first()
    )

    if not provider:
        raise HTTPException(
            status_code=404,
            detail="Provider not found"
        )

    provider.name = updated_provider.name
    provider.specialization = updated_provider.specialization
    provider.email = updated_provider.email

    db.commit()
    db.refresh(provider)

    return provider


@router.delete("/{provider_id}")
def delete_provider(
    provider_id: int,
    db: Session = Depends(get_db)
):
    provider = (
        db.query(Provider)
        .filter(Provider.id == provider_id)
        .first()
    )

    if not provider:
        raise HTTPException(
            status_code=404,
            detail="Provider not found"
        )

    db.delete(provider)
    db.commit()

    return {
        "message": "Provider deleted successfully"
    }