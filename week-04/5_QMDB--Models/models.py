from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import relationship, DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from typing import List


class Base(DeclarativeBase):
    pass

class MovieGenre(Base):
    pass

class Movie(Base):
    pass

class User(Base):
    pass

class Genre(Base):
    pass

class Review(Base):
    pass
