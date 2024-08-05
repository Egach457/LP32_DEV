from abc import ABC, abstractmethod

from webapp.lib.db import db
from webapp.lib.models import Apartmens


class InterfaceShowAnnouncement(ABC):

    @abstractmethod
    def show(self) -> list[Apartmens]:
        pass


class InterfaceSaveAnnouncement(ABC):
    @abstractmethod
    def save(self, apartmens: Apartmens) -> None:
        pass


class InterfaceEditAnnouncement(ABC):
    @abstractmethod
    def edit(self, apartmens: Apartmens) -> None:
        pass


class InterfaceDeleteAnnouncement(ABC):
    @abstractmethod
    def delete(self, apartmens_id: int) -> None:
        pass


class ShowAnnouncement(InterfaceShowAnnouncement):
    def __init__(self) -> None:
        self.session = db.session

    def show(self) -> list[Apartmens]:
        return self.session.query(Apartmens).all()


class SaveAnnouncement(InterfaceSaveAnnouncement):
    def __init__(self) -> None:
        self.session = db.session

    def save(self, apartmens: Apartmens) -> None:
        self.session.add(apartmens)
        self.session.commit()


class EditAnnouncement(InterfaceEditAnnouncement):
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
        self.session = db.session

    def edit(self, apartmens: Apartmens) -> None:
        existing_apartmens = (
            self.session.query(
                Apartmens,
            )
            .filter_by(id=apartmens.id, user_id=self.user_id)
            .first()
        )
        if existing_apartmens:
            existing_apartmens.address = apartmens.address
            existing_apartmens.title = apartmens.title
            existing_apartmens.description = apartmens.description
            self.session.add(existing_apartmens)
            self.session.commit()


class DeleteAnnouncement(InterfaceDeleteAnnouncement):
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id
        self.session = db.session

    def delete(self, apartmens_id: int) -> None:
        apartmens = self.session.query(Apartmens).filter_by(id=apartmens_id, user_id=self.user_id).first()
        if apartmens:
            self.session.delete(apartmens)
            self.session.commit()


class UserShowAnnouncement(ShowAnnouncement):
    def __init__(self, user_id: int) -> None:
        super().__init__()
        self.user_id = user_id

    def show(self) -> list[Apartmens]:
        return self.session.query(Apartmens).filter_by(user_id=self.user_id).all()
