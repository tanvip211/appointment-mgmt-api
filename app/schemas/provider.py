from pydantic import BaseModel, EmailStr


class ProviderCreate(BaseModel):
    name: str
    specialization: str
    email: EmailStr


class ProviderResponse(ProviderCreate):
    id: int

    class Config:
        from_attributes = True