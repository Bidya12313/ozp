from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from datetime import datetime

from .engine import Base


class Taxes(Base):
    __tablename__ = 'taxes'
    id: Mapped[int] = mapped_column(primary_key=True)
    typetx: Mapped[str] = mapped_column()
    declarant: Mapped[str] = mapped_column()
    payer: Mapped[str] = mapped_column()
    director: Mapped[str] = mapped_column()
    recipient: Mapped[str] = mapped_column()
    amount: Mapped[float] = mapped_column()
    category: Mapped[str] = mapped_column()
    document: Mapped[Optional[str]] = mapped_column()
    comment: Mapped[Optional[str]] = mapped_column(nullable=True)
    time: Mapped[datetime] = mapped_column(default=datetime.now)
    status: Mapped[Optional[str]] = mapped_column()