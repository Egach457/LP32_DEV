from getpass import getpass
import sys

from webapp import create_app
from webapp.lib.db import db
from webapp.user.models import User

app = create_app()

with app.app_context():
    email = input("Введите почту: ")
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    phone = input("Введите номре телефона: ")
    #TODO: помнеть принты на yield
    if User.query.filter(User.email == email).count():
        print("Пользователь с таким именем уже существует")
        sys.exit(0)

    password1 = getpass("Введите пароль")
    password2 = getpass("Повторите пароль")

    if not password1 == password2:
        print("Пароли не одинаковые")
        sys.exit(0)

    new_user = User(email=email, role="admin",
                    first_name=first_name, last_name=last_name, phone=phone)
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print("Создан пользователь с id={}".format(new_user.id))
