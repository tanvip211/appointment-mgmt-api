from pydantic import BaseModel, EmailStr, Field


class ProviderCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    specialization: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    email: EmailStr


class ProviderResponse(ProviderCreate):
    id: int

    class Config:
        from_attributes = True