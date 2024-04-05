from typing import Optional
from enum import Enum
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, BigInteger, Integer, String, DateTime, Text, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped, mapped_column

from webapp.lib.db import Base, engine

class User(Base, UserMixin):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(64), nullable=False)
    last_name: Mapped[str] = mapped_column(String(64), nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    phone: Mapped[str] = mapped_column(String(13), nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    role: Mapped[str] = mapped_column(String(10), index=True)
    # apartmens: Mapped[list["Apartmens"]] = relationship()
    # comment_bunch: Mapped[list["Comment"]] = relationship(
        # back_populates="user_bunch")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == "admin"

    def __repr__(self) -> str:
        return f"User id: {self.id}, {self.first_name}"
