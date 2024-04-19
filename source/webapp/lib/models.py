from typing import Optional
from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Table
from sqlalchemy.dialects.postgresql import ENUM as PgEnum
from sqlalchemy.orm import relationship, Mapped, mapped_column

from webapp.lib.db import Base, engine
from webapp.user.models import User


# association_table = Table(
# "association_table",
# Base.metadata,
# Column("apartmens_id", ForeignKey("apartmens.id"), primary_key=True),
# Column("accommodations_id", ForeignKey("accommodations.id"), primary_key=True),
# Column("comforts_id", ForeignKey("comforts.id"), primary_key=True),
# Column("payments_id", ForeignKey("payments.id"), primary_key=True),
# Column("properties_id", ForeignKey("properties.id"), primary_key=True),
# Column("comments_id", ForeignKey("comments.id"), primary_key=True),
# Column("users_id", ForeignKey("users.id"), primary_key=True),
# )


class ApartmensTypeChoice(Enum):
    DEFAULT_VALUE = "Не определенно"
    APARTMENT = "Квартира"
    HOUSE = "Дом"
    ROOM = "Комната"
    HOTEL = "Отель"


class PaymensTypeChoice(Enum):
    DEFAULT_VALUE = "Не определенно"
    CASH = "Наличные"
    CARD = "Карта"


class Apartmens(Base):
    __tablename__ = "apartmens"

    id: Mapped[int] = mapped_column(primary_key=True)
    accommodation_id: Mapped[int] = mapped_column(
        ForeignKey("accommodations.id", ondelete="CASCADE"), index=True, nullable=False
    )
    comfort_id: Mapped[int] = mapped_column(
        ForeignKey("comforts.id", ondelete="CASCADE"), index=True, nullable=False
    )
    payment_id: Mapped[int] = mapped_column(
        ForeignKey("payments.id", ondelete="CASCADE"), index=True, nullable=False
    )
    propertie_id: Mapped[int] = mapped_column(
        ForeignKey("properties.id", ondelete="CASCADE"), index=True, nullable=False
    )
    comment_id: Mapped[int] = mapped_column(
        ForeignKey("comments.id", ondelete="CASCADE"), index=True, nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    country: Mapped[str] = mapped_column(String(64), nullable=False)
    city: Mapped[str] = mapped_column(String(64), nullable=False)
    address: Mapped[str] = mapped_column(String(164), nullable=False)
    title: Mapped[str] = mapped_column(String(164), nullable=False)
    description: Mapped[Optional[Text]] = mapped_column(Text, nullable=True)
    rent_type: Mapped[ApartmensTypeChoice] = mapped_column(
        PgEnum(
            ApartmensTypeChoice,
            name="apartmenstypechoice",
            create_type=False,
            values_callable=lambda n: [item.value for item in n],
        ),
        nullable=False,
        default=ApartmensTypeChoice.DEFAULT_VALUE,
    )
    payment_type: Mapped[PaymensTypeChoice] = mapped_column(
        PgEnum(
            PaymensTypeChoice,
            name="paymenstypechoice",
            create_type=False,
            values_callable=lambda n: [item.value for item in n],
        ),
        nullable=False,
        default=PaymensTypeChoice.DEFAULT_VALUE,
    )
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
    comments_bunch: Mapped[list["Comment"]] = relationship(
        back_populates="apartmens_bunch",
        uselist=True,
    )
    user_bunch: Mapped[list["User"]] = relationship(
        back_populates="apartmens_bunch",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"Apartmens id: {self.id}, title: {self.address}"


class ComfortChoice(Enum):
    DEFAULT_VALUE = "Не определенно"
    WI_FI = "Wi-Fi"
    HAIR_DRYER = "Фен"
    TOWELS = "Полотенец"
    BALCONY = "Балкон"
    AIR_CONDITIONER = "Кондиционер"
    TV = "Телевизор"


class Comfort(Base):
    __tablename__ = "comforts"

    id: Mapped[int] = mapped_column(primary_key=True)
    apartmens_id: Mapped[int] = mapped_column(
        ForeignKey("apartmens.id", ondelete="CASCADE"), index=True, nullable=False
    )
    comfort_choice: Mapped[ComfortChoice] = mapped_column(
        PgEnum(
            ComfortChoice,
            name="comfortchoice",
            create_type=False,
            values_callable=lambda n: [item.value for item in n],
        ),
        nullable=False,
        default=ComfortChoice.DEFAULT_VALUE,
    )
    apartmens_bunch: Mapped["Apartmens"] = relationship(
        back_populates="comforts_bunch",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"Comfort id: {self.id}, {self.apartmens_id}"


class PropertieChoise(Enum):
    DEFAULT_VALUE = "Не определенно"
    NO_CHILDREN = "Без детей"
    NO_PARTIES = "Без вечеринок"
    NO_SMOKING = "Курение запрещено"
    NO_PETS = "Без питомце"


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
    footege_room: Mapped[str] = mapped_column(String(10), nullable=False)
    propertie_choice: Mapped[PropertieChoise] = mapped_column(
        PgEnum(
            PropertieChoise,
            name="propertiechoise",
            create_type=False,
            values_callable=lambda n: [item.value for item in n],
        ),
        nullable=False,
        default=PropertieChoise.DEFAULT_VALUE,
    )
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
    apartmens: Mapped["Apartmens"] = relationship(
        back_populates="comment_bunch",
        uselist=False,
    )
    user_bunch: Mapped["User"] = relationship(
        back_populates="comment_bunch",
        uselist=False,
    )

    def __repr__(self) -> str:
        return f"Comment id: {self.id}, {self.date_create}"


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
