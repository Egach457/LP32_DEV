from typing import Optional
from enum import Enum
from flask_login import UserMixin
from sqlalchemy import (
    Boolean,
    String,
    DateTime,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import relationship, Mapped, mapped_column
from werkzeug.security import generate_password_hash, check_password_hash

from webapp.lib.db import Base, engine, db

db.metadata.clear()


class ApartmensTypeChoice(Enum):
    APARTMENT = "Квартира"
    HOUSE = "Дом"
    ROOM = "Комната"
    HOTEL = "Отель"


class PaymensTypeChoice(Enum):
    CASH = "Наличные"
    CARD = "Карта"


class Apartmens(Base):
    __tablename__ = "apartmens"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    country: Mapped[str] = mapped_column(String(64), nullable=False)
    city: Mapped[str] = mapped_column(String(64), nullable=False)
    address: Mapped[str] = mapped_column(String(164), nullable=False)
    title: Mapped[str] = mapped_column(String(164), nullable=False)
    description: Mapped[Optional[Text]] = mapped_column(Text, nullable=True)
    rent_type: Mapped[str] = mapped_column(String(32), nullable=False)
    payment_type: Mapped[str] = mapped_column(String(32), nullable=False)
    image_path: Mapped[Optional[str]] = mapped_column(String(225), nullable=True)
    accommodations_bunch: Mapped["Accommodation"] = relationship(
        back_populates="apartmens_bunch",
        uselist=False,
    )
    comforts_bunch: Mapped[list["Comfort"]] = relationship(
        back_populates="apartmens_bunch",
        uselist=True,
    )
    payments_bunch: Mapped["Payment"] = relationship(
        back_populates="apartmens_bunch",
        uselist=False,
    )
    properties_bunch: Mapped[list["Propertie"]] = relationship(
        back_populates="apartmens_bunch",
        uselist=True,
    )
    comment_bunch: Mapped[list["Comment"]] = relationship(
        back_populates="apartmens_bunch",
        uselist=True,
    )
    user_bunch: Mapped["User"] = relationship(
        back_populates="apartmens_bunch",
        foreign_keys=[user_id],
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"Apartmens id: {self.id}, title: {self.address}"


class User(Base, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(64), nullable=False)
    last_name: Mapped[str] = mapped_column(String(64), nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(13), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(String(10), index=True)
    apartmens_bunch: Mapped[list["Apartmens"]] = relationship(
        back_populates="user_bunch",
        uselist=True,
    )
    comment_bunch: Mapped[list["Comment"]] = relationship(
        back_populates="user_bunch",
        uselist=True,
    )

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == "admin"

    def __repr__(self) -> str:
        return f"User id: {self.id}, {self.first_name}"


class Comfort(Base):
    __tablename__ = "comforts"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(
        ForeignKey("apartmens.id", ondelete="CASCADE"), index=True, nullable=False
    )
    wi_fi: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    hair_dryer: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    towels: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    balcony: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    air_conditioner: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    tv: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    apartmens_bunch: Mapped["Apartmens"] = relationship(
        back_populates="comforts_bunch",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"Comfort id: {self.id}, {self.apartmens_id}"


class Propertie(Base):
    __tablename__ = "properties"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(
        ForeignKey("apartmens.id", ondelete="CASCADE"), index=True, nullable=False
    )
    floor: Mapped[str] = mapped_column(String(10), nullable=False)
    apartment_number: Mapped[str] = mapped_column(String(10), nullable=False)
    number_of_beds: Mapped[str] = mapped_column(String(10), nullable=False)
    number_of_guests: Mapped[str] = mapped_column(String(10), nullable=False)
    room_area: Mapped[str] = mapped_column(String(10), nullable=False)
    no_children: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    no_parties: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    no_smoking: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    no_pets: Mapped[str] = mapped_column(Boolean, nullable=True, default=True)
    apartmens_bunch: Mapped["Apartmens"] = relationship(
        back_populates="properties_bunch",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"Propertie id: {self.id}, {self.apartmens_id}"


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(
        ForeignKey("apartmens.id", ondelete="CASCADE"), index=True, nullable=False
    )
    price: Mapped[int] = mapped_column(nullable=False)
    apartmens_bunch: Mapped["Apartmens"] = relationship(
        back_populates="payments_bunch",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"Payment id: {self.id}, {self.price}"


class Accommodation(Base):
    __tablename__ = "accommodations"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(
        ForeignKey("apartmens.id", ondelete="CASCADE"), index=True, nullable=False
    )
    date_arrival: Mapped[DateTime] = mapped_column(DateTime)
    date_departure: Mapped[DateTime] = mapped_column(DateTime)
    apartmens_bunch: Mapped["Apartmens"] = relationship(
        back_populates="accommodations_bunch",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"Accommodation id: {self.id}, {self.date_arrival}"


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(
        ForeignKey("apartmens.id", ondelete="CASCADE"), index=True, nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    date_create: Mapped[DateTime] = mapped_column(DateTime)
    description: Mapped[Optional[Text]] = mapped_column(Text)
    apartmens_bunch: Mapped["Apartmens"] = relationship(
        back_populates="comment_bunch",
        foreign_keys=[apartmens_id],
        uselist=False,
    )
    user_bunch: Mapped["User"] = relationship(
        back_populates="comment_bunch",
        foreign_keys=[user_id],
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"Comment id: {self.id}, {self.date_create}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
