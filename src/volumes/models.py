from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer
from src.models import Base


class Volume(Base):
    __tablename__ = "volumes"

    id: Mapped[int] = mapped_column("id", autoincrement=True, nullable=False, unique=True, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    size: Mapped[int] = mapped_column(Integer, nullable=False)