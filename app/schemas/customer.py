from pydantic import BaseModel, EmailStr, Field


class CustomerCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=1,
        max_length=100
    )

    email: EmailStr

    phone: str = Field(
        ...,
        pattern=r"^\d{10}$"
    )


class CustomerResponse(CustomerCreate):
    id: int

    class Config:
        from_attributes = True