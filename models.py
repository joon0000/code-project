from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey,Text
from typing import List

class Base(DeclarativeBase):
    pass

# 1 user must have 1 role
# 1 role can  have many user
# so relationship btw user and role be like
# 1 to many 

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username:Mapped[str] = mapped_column(nullable=False, unique=True)
    password:Mapped[str] = mapped_column(nullable=False)
    email:Mapped[str] = mapped_column(unique=True, nullable=True)
    role_id:Mapped[int] = mapped_column(ForeignKey('roles.id'))
    role:Mapped['Role'] = relationship(back_populates='user')
    letter:Mapped[List['Letter']] = relationship(back_populates='user')
    
    def __repr__(self) -> str:
        return f"<User username={self.username}>"
    
class Role(Base):
    __tablename__ = 'roles'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name:Mapped[str] = mapped_column(nullable=False, unique=True)
    user:Mapped[List['User']] = relationship(back_populates='role')
    
    def __repr__(self):
        f"<role name={self.name} by {self.user.username}>"
    
class Letter(Base):
    __tablename__ = 'letters'
    id:Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title:Mapped[str] = mapped_column(unique=True, nullable=False)
    secret_content:Mapped[str] = mapped_column(nullable=False)
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))
    user:Mapped['User'] = relationship(back_populates='letter')
    
    def __repr__(self):
        return f"<User(book_title={self.title}, user={self.user})>"
    
    
    