from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from .engine import Base


class DailyBudget(Base):
    __tablename__ = 'daily_budget'
    id: Mapped[int] = mapped_column(primary_key=True)
    declarant: Mapped[str] = mapped_column(unique=True)
    budget: Mapped[float] = mapped_column(nullable=True)
    requested_budget: Mapped[Optional[int]] = mapped_column()