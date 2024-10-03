from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from .engine import Base


class Taxes(Base):
    __tablename__ = 'taxes'
    id: Mapped[int] = mapped_column(primary_key=True)
    declarant: Mapped[str] = mapped_column()
    payer: Mapped[str] = mapped_column()
    director: Mapped[str] = mapped_column()
    description: Mapped[Optional[str]] = mapped_column()
    amount: Mapped[int] = mapped_column()
    category: Mapped[str] = mapped_column()
    document: Mapped[Optional[str]] = mapped_column()
    comment: Mapped[Optional[str]] = mapped_column(nullable=True)
    status: Mapped[Optional[str]] = mapped_column()