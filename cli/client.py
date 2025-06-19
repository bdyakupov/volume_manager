import httpx
from typing import Optional, Dict, Any
from schemas import (
    VolumeCreateSchema,
    VolumeReadSchema,
    VolumeUpdateSchema,
    PaginatedListResponse
)


class VolumeAPIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.client = httpx.AsyncClient(base_url=self.base_url)


    async def create_volume(self, volume: VolumeCreateSchema) -> VolumeReadSchema:
        try:
            response = await self.client.post("/volumes/", json=volume.model_dump())
            response.raise_for_status()
            return VolumeReadSchema(**response.json())
        except httpx.HTTPStatusError as e:
            raise RuntimeError(f"Unable to create volume: {e.response.status_code} {e.response.text}")


    async def read_volumes(
        self,
        page: Optional[int] = 1,
        items_per_page: Optional[int] = 10
    ) -> PaginatedListResponse:
        try:
            response = await self.client.get("/volumes/", params={
                "page": page,
                "items_per_page": items_per_page
            })
            response.raise_for_status()
            return PaginatedListResponse(**response.json())
        except httpx.HTTPStatusError as e:
            raise RuntimeError(f"Unable to load list of volumes: {e.response.status_code} {e.response.text}")


    async def read_volume(self, volume_id: int) -> VolumeReadSchema:
        try:
            response = await self.client.get(f"/volumes/{volume_id}")
            response.raise_for_status()
            return VolumeReadSchema(**response.json())
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise RuntimeError(f"Volume with ID {volume_id} not found.")
            raise RuntimeError(f"Unable to load volume info: {e.response.status_code} {e.response.text}")


    async def update_volume(self, volume_id: int, update: VolumeUpdateSchema) -> Dict[str, Any]:
        try:
            response = await self.client.patch(f"/volumes/{volume_id}", json=update.model_dump())
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise RuntimeError(f"Volume with ID {volume_id} not found.")
            raise RuntimeError(f"Unable to update volume: {e.response.status_code} {e.response.text}")


    async def delete_volume(self, volume_id: int) -> Dict[str, Any]:
        try:
            response = await self.client.delete(f"/volumes/{volume_id}")
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                raise RuntimeError(f"Volume with ID {volume_id} not found.")
            raise RuntimeError(f"Unable to delete volume: {e.response.status_code} {e.response.text}")


    async def close(self):
        await self.client.aclose()