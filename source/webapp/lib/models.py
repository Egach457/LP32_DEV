from typing import Optional
from enum import Enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, BigInteger, Integer, String, DateTime, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column

from webapp.lib.db import Base, engine
from webapp.user.models import User



association_table = Table(
    "association_table",
    Base.metadata,
    Column("apartmens_id", ForeignKey("apartmens.id"), primary_key=True),
    Column("accommodations_id", ForeignKey("accommodations.id"), primary_key=True),
    Column("comforts_id", ForeignKey("comforts.id"), primary_key=True),
    Column("payments_id", ForeignKey("payments.id"), primary_key=True),
    Column("properties_id", ForeignKey("properties.id"), primary_key=True),
    Column("comments_id", ForeignKey("comments.id"), primary_key=True),
    Column("users_id", ForeignKey("users.id"), primary_key=True),

)


class ApartmensTypeChoice(Enum):
    apartment = "Квартира"
    house = "Дом"
    room = "Комната"
    hotel = "Отель"


class PaymensTypeChoice(Enum):
    cash = "Наличные"
    card = "Карта"


class Apartmens(Base):
    __tablename__ = "apartmens"

    id: Mapped[int] = mapped_column(primary_key=True)
    accommodation_id: Mapped[int] = mapped_column(ForeignKey(
        "accommodations.id", ondelete="CASCADE"), index=True, nullable=False)
    comfort_id: Mapped[int] = mapped_column(ForeignKey(
        "comforts.id", ondelete="CASCADE"), index=True, nullable=False)
    payment_id: Mapped[int]= mapped_column(ForeignKey(
        "payments.id", ondelete="CASCADE"), index=True, nullable=False)
    propertie_id: Mapped[int] = mapped_column(ForeignKey(
        "properties.id", ondelete="CASCADE"), index=True, nullable=False)
    comment_id: Mapped[int] = mapped_column(ForeignKey(
        "comments.id", ondelete="CASCADE"), index=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id", ondelete="CASCADE"), index=True, nullable=False)
    country: Mapped[str] = mapped_column(String(64), nullable=False)
    city: Mapped[str] = mapped_column(String(64), nullable=False)
    address: Mapped[str] = mapped_column(String(164), nullable=False)
    title: Mapped[str] = mapped_column(String(164), nullable=False)
    description: Mapped[Optional[Text]] = mapped_column(Text)
    rent_type: Mapped[ApartmensTypeChoice]
    payment_type: Mapped[PaymensTypeChoice]
    accommodations_bunch: Mapped[list["Accommodation"]] = relationship(
        secondary=association_table, back_populates="apartmens_bunch"
    )
    comforts_bunch: Mapped[list["Comfort"]] = relationship(
        secondary=association_table, back_populates="apartmens_bunch"
    )
    payments_bunch: Mapped[list["Payment"]] = relationship(
        secondary=association_table, back_populates="apartmens_bunch"
    )
    properties_bunch: Mapped[list["Propertie"]] = relationship(
        secondary=association_table, back_populates="apartmens_bunch"
    )
    # comments_bunch: Mapped[list["Comment"]] = relationship(
        # secondary=association_table, back_populates="apartmens_bunch"
    # )

    def __repr__(self) -> str:
        return f"Apartmens id: {self.id}, title: {self.address}"


class ComfortChoice(Enum):
    wi_fi = "Wi-Fi"
    hair_dryer = "Фен"
    towels = "Полотенец"
    balcony = "Балкон"
    air_conditioner = "Кондиционер"
    tv = "Телевизор"


class Comfort(Base):
    __tablename__ = "comforts"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(ForeignKey(
        "apartmens.id", ondelete="CASCADE"), index=True, nullable=False)
    comfort_choice: Mapped[ComfortChoice]
    apartmens_bunch: Mapped[list["Apartmens"]] = relationship(
        secondary=association_table, back_populates="comforts_bunch")

    def __repr__(self) -> str:
        return f"Comfort id: {self.id}, {self.apartmens_id}"


class PropertieChoise(Enum):
    no_children = "Без детей"
    no_parties = "Без вечеринок"
    no_smoking = "Курение запрещено"
    no_pets = "Без питомце"


class Propertie(Base):
    __tablename__ = "properties"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(ForeignKey(
        "apartmens.id", ondelete="CASCADE"), index=True, nullable=False)
    propertie_choice: Mapped[PropertieChoise]
    apartmens_bunch: Mapped[list["Apartmens"]] = relationship(
        secondary=association_table, back_populates="properties_bunch")

    def __repr__(self) -> str:
        return f"Propertie id: {self.id}, {self.apartmens_id}"


class Payment(Base):
    __tablename__ = "payments"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(ForeignKey(
        "apartmens.id", ondelete="CASCADE"), index=True, nullable=False)
    price: Mapped[int] = mapped_column(nullable=False)
    apartmens_bunch: Mapped[list["Apartmens"]] = relationship(
        secondary=association_table, back_populates="payments_bunch")

    def __repr__(self) -> str:
        return f"Payment id: {self.id}, {self.price}"


class Accommodation(Base):
    __tablename__ = "accommodations"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(ForeignKey(
        "apartmens.id", ondelete="CASCADE"), index=True, nullable=False)
    date_arrival: Mapped[DateTime] = mapped_column(DateTime)
    date_departure: Mapped[DateTime] = mapped_column(DateTime)
    apartmens_bunch: Mapped[list["Apartmens"]] = relationship(
        secondary=association_table, back_populates="accommodations_bunch")

    def __repr__(self) -> str:
        return f"Accommodation id: {self.id}, {self.date_arrival}"


class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(ForeignKey(
        "apartmens.id", ondelete="CASCADE"), index=True, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey(
        "users.id", ondelete="CASCADE"), index=True, nullable=False)
    date_create: Mapped[DateTime] = mapped_column(DateTime)
    description: Mapped[Optional[Text]] = mapped_column(Text)
    # apartmens: Mapped[list["Apartmens"]] = relationship(
        # secondary=association_table,
        # back_populates="comment_bunch")
    # user_bunch: Mapped[list["User"]] = relationship(
        # back_populates="comment_bunch")

    def __repr__(self) -> str:
        return f"Comment id: {self.id}, {self.date_create}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
