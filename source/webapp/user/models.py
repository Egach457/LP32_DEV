from webapp.booking_list.models import Apartmens, ShowAnnouncement


class UserShowAnnouncement(ShowAnnouncement):
    def __init__(self, user_id: int) -> None:
        super().__init__()
        self.user_id = user_id

    def show(self) -> list[Apartmens]:
        return self.session.query(Apartmens).filter_by(user_id=self.user_id).all()
