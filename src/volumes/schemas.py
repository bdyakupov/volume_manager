from pydantic import BaseModel, Field


class VolumeCreateSchema(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    size: int = Field(..., ge=1)


class VolumeReadSchema(BaseModel):
    id: int
    name: str
    size: int

class VolumeUpdateSchema(BaseModel):
    size: int = Field(..., ge=1)


class VolumeDeleteSchema(BaseModel):
    pass