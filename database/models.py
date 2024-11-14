from sqlalchemy.orm import Mapped, mapped_column

from .engine import Base


class Users(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    password: Mapped[int] = mapped_column()
    operator_status: Mapped[str] = mapped_column(nullable=True)
    admin_status: Mapped[str] = mapped_column(nullable=True)
    director_status: Mapped[str] = mapped_column(nullable=True)

    @property
    def is_authenticated(self):
        return True  
    
    @property
    def is_active(self):
        return True  
    
    @property
    def is_anonymous(self):
        return False  
    
    def get_id(self):
        return str(self.id)  


class Payers(Base):
    __tablename__ = 'payers'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()


class Categories(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column()


class Banks(Base):
    __tablename__ = 'banks'
    id: Mapped[int] = mapped_column(primary_key=True)
    bank: Mapped[str] = mapped_column()