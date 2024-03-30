from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey
from sqlalchemy.orm import relationship

from db import Base, engine


class Apartmens(Base):
    __tablename__ = "apartmens"

    id = Column(Integer, primary_key=True)
    accommodation_id = Column(Integer, ForeignKey(Accommodation.id), index=True, nullable=False)
    comfort_id = Column(Integer, ForeignKey(Comfort.id), index=True, nullable=False)
    payment_id = Column(Integer, ForeignKey(Payment.id), index=True, nullable=False)
    propertie_id = Column(Integer, ForeignKey(Propertie.id), index=True, nullable=False)
    comment_id = Column(Integer, ForeignKey(Comment.id), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), index=True, nullable=False)
    country = Column(String, nullable=False)
    city = Column(String, nullable=False)
    address = Column(String, nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)

    def __repr__(self):
        return f"Apartmens id: {self.id}, title: {self.id}"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(Integer, nullable=False)
    login = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    def __repr__(self):
        return f"User id: {self.id}, {self.name}"


class Comfort(Base):
    __tablename__ = "comforts"

    id = Column(Integer, primary_key=True)
    apartmens_id = Column(Integer, ForeignKey(Apartmens.id), index=True, nullable=False)

    def __repr__(self):
        return f"Comfort id: {self.id}, {self.apartmens_id}"


class Propertie(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True)
    apartmens_id = Column(Integer, ForeignKey(Apartmens.id), index=True, nullable=False)

    def __repr__(self):
        return f"Propertie id: {self.id}, {self.apartmens_id}"


class Payment(Base):
    __tablename__ = "payments"

    id = Column(Integer, primary_key=True)
    apartmens_id = Column(Integer, ForeignKey(Apartmens.id), index=True, nullable=False)
    price = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Payment id: {self.id}, {self.price}"


class Accommodation(Base):
    __tablename__ = "accommodations"

    id = Column(Integer, primary_key=True)
    apartmens_id = Column(Integer, ForeignKey(Apartmens.id), index=True, nullable=False)
    date_arrival = Column(Date)
    date_departure = Column(Date)

    def __repr__(self):
        return f"Accommodation id: {self.id}, {self.apartmens_id}"


class Comment(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True)
    apartmens_id = Column(Integer, ForeignKey(Apartmens.id), index=True, nullable=False)
    user_id = Column(Integer, ForeignKey(User.id), index=True, nullable=False)
    date_create = Column(Date)
    description = Column(Text)

    def __repr__(self):
        return f"Comment id: {self.id}, {self.apartmens_id}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
