import asyncclick as click
from cli.client import VolumeAPIClient
from cli.schemas import VolumeCreateSchema, VolumeUpdateSchema
from rich.table import Table
from rich.console import Console
from cli.logger import log_action


API_URL = "http://localhost:8000"
console = Console()


@click.group()
async def cli():
    """Volume management CLI."""
    pass


@cli.command("list-volumes")
@log_action
async def list_volumes():
    """List all volumes."""
    client = VolumeAPIClient(API_URL)
    result = await client.read_volumes()
    table = Table(title="Volumes")
    table.add_column("ID", style="cyan")
    table.add_column("Name")
    table.add_column("Size", justify="right")

    for volume in result.data:
        table.add_row(str(volume.id), volume.name, str(volume.size))

    console.print(table)
    await client.close()


@cli.command("create-volume")
@click.option("--name", required=True, help="Volume title")
@click.option("--size", required=True, type=int, help="Volume size")
@log_action
async def create_volume(name, size):
    """Create a new volume."""
    client = VolumeAPIClient(API_URL)
    volume = VolumeCreateSchema(name=name, size=size)
    created = await client.create_volume(volume)
    console.print_json(data=created.model_dump())
    await client.close()


@cli.command("get-volume")
@click.argument("volume_id", type=int)
@log_action
async def get_volume(volume_id):
    """Get volume info by id (json)"""
    client = VolumeAPIClient(API_URL)
    volume = await client.read_volume(volume_id)
    console.print_json(data=volume.model_dump())
    await client.close()


@cli.command("update-volume")
@click.argument("volume_id", type=int)
@click.option("--size", required=True, type=int, help="New volume size")
@log_action
async def update_volume(volume_id, size):
    """Update volume size."""
    client = VolumeAPIClient(API_URL)
    update = VolumeUpdateSchema(size=size)
    result = await client.update_volume(volume_id, update)
    console.print_json(data=result)
    await client.close()


@cli.command("delete-volume")
@click.argument("volume_id", type=int)
@log_action
async def delete_volume(volume_id):
    """Delete volume by id."""
    client = VolumeAPIClient(API_URL)
    result = await client.delete_volume(volume_id)
    console.print_json(data=result)
    await client.close()


if __name__ == "__main__":
    cli(_anyio_backend="asyncio")