from db import Base

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    cell_phone = Column(String(20), nullable=True)

    def __repr__(self):
        return f"{self.last_name}, {self.first_name} ({self.email})"


class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)


class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)

# There is a better way to define many-to-many in SQLAlchemy
class MovieGenres(Base):
    __tablename__ = 'movie_genres'
    movie_id = Column(Integer, ForeignKey('movies.id'), primary_key=True)
    genre_id = Column(Integer, ForeignKey('genres.id'), primary_key=True)


class Order(Base):
    __tablename__ = 'orders'
    customer_id = Column(Integer, ForeignKey('customers.id'), primary_key=True)
    movie_id = Column(Integer, ForeignKey('movies.id'), primary_key=True)
    movie_price = Column(Integer, nullable=False)
    purchase_date = Column(DateTime, nullable=False)
