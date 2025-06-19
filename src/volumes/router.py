from typing import Annotated, Any, cast

from fastcrud.paginated import PaginatedListResponse, compute_offset, paginated_response
from fastcrud.exceptions.http_exceptions import DuplicateValueException, NotFoundException
from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from src.volumes.crud import volume_crud
from src.volumes.schemas import VolumeReadSchema, VolumeCreateSchema, VolumeUpdateSchema
from src.database import async_get_session


router = APIRouter(prefix="/volumes", tags=["Volumes"])


@router.post("/", response_model=VolumeReadSchema, status_code=201)
async def create_volume(
        request: Request,
        volume: VolumeCreateSchema,
        db: Annotated[AsyncSession, Depends(async_get_session)]
) -> VolumeReadSchema:
    name_row = await volume_crud.exists(db=db, name=volume.name)
    if name_row:
        raise DuplicateValueException("Volume name is already registered")
    created_volume = await volume_crud.create(db=db, object = volume)
    return cast(VolumeReadSchema, created_volume)


@router.get("/", response_model=PaginatedListResponse[VolumeReadSchema])
async def read_volumes(
        request: Request,
        db: Annotated[AsyncSession, Depends(async_get_session)],
        page: int = 1,
        items_per_page: int = 10
) -> dict:
    volumes_data = await volume_crud.get_multi(
        db=db,
        offset=compute_offset(page, items_per_page),
        limit=items_per_page,
        is_deleted=False
    )
    response: dict[str, Any] = paginated_response(volumes_data, page=page, items_per_page=items_per_page)
    return response


@router.get("/{volume_id}", response_model=VolumeReadSchema)
async def read_volume(
        request: Request,
        volume_id: int,
        db: Annotated[AsyncSession, Depends(async_get_session)]
) -> VolumeReadSchema:
    db_volume = await volume_crud.get(db=db, id=volume_id, is_deleted=False, schema_to_select=VolumeReadSchema)
    if db_volume is None:
        raise NotFoundException("Volume not found")
    return cast(VolumeReadSchema, db_volume)


@router.patch("/{volume_id}")
async def update_volume(
        request: Request,
        volume_data: VolumeUpdateSchema,
        volume_id: int,
        db: Annotated[AsyncSession, Depends(async_get_session)]
) -> dict[str, str]:
    db_volume = await volume_crud.get(db=db, id=volume_id, schema_to_select=VolumeReadSchema)
    if not db_volume:
        raise NotFoundException("Volume not found")

    await volume_crud.update(db=db, object=volume_data, id=volume_id)
    return {"message": "Volume updated"}


@router.delete("/{volume_id}")
async def delete_volume(
        request: Request,
        volume_id: int,
        db: Annotated[AsyncSession, Depends(async_get_session)]
) -> dict[str, str]:
    db_volume = await volume_crud.get(db=db, id=volume_id, schema_to_select=VolumeReadSchema)
    if not db_volume:
        raise NotFoundException("Volume not found")
    
    await volume_crud.delete(db=db, id=volume_id)
    return {"message": "Volume deleted"}