from sqlalchemy.orm import Mapped, mapped_column

from .engine import Base


class Declarants(Base):
    __tablename__ = 'declarants'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    password: Mapped[int] = mapped_column()
    chat_id: Mapped[int] = mapped_column()

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


class Directors(Base):
    __tablename__ = 'directors'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    chat_id: Mapped[int] = mapped_column()


class Categories(Base):
    __tablename__ = 'categories'
    id: Mapped[int] = mapped_column(primary_key=True)
    category: Mapped[str] = mapped_column()


class Banks(Base):
    __tablename__ = 'banks'
    id: Mapped[int] = mapped_column(primary_key=True)
    bank: Mapped[str] = mapped_column()