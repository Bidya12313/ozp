from sqlalchemy.orm import Mapped, mapped_column

from engine import Base


class Test(Base):
    __tablename__ = 'test'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()