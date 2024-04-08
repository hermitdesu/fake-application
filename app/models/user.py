import datetime

from sqlalchemy import BigInteger, DateTime, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import AlchemyBaseModel


class User(AlchemyBaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger,
        nullable=False,
        unique=True,
        primary_key=True,
    )
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    application_filepath: Mapped[str] = mapped_column(
        String, nullable=True, unique=True
    )
    registered_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=datetime.datetime.now
    )
