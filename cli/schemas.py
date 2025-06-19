from pydantic import BaseModel, constr, conint
from typing import List, Optional


class VolumeCreateSchema(BaseModel):
    name: constr(min_length=2, max_length=50)
    size: conint(ge=1)


class VolumeUpdateSchema(BaseModel):
    size: conint(ge=1)


class VolumeReadSchema(BaseModel):
    id: int
    name: str
    size: int


class PaginatedListResponse(BaseModel):
    data: List[VolumeReadSchema]
    total_count: int
    has_more: bool
    page: Optional[int] = None
    items_per_page: Optional[int] = None