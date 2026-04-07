# from alca.forms.registerform import RegisterForm
# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
import datetime
from data import db_session
from data.users import User

db_session.global_init("db/blogs.db")
session = db_session.create_session()
# ggj

def make_user(surname, name, age, position, speciality, address, email):
    user = User()
    user.surname = surname
    user.name = name
    user.age = age
    user.position = position
    user.speciality = speciality
    user.address = address
    user.email = email
    user.modified_date = datetime.datetime.now()
    session.add(user)


make_user(
    surname="Scott",
    name="Ridley",
    age=21,
    position="captain",
    speciality="research engineer",
    address="module_1",
    email="scott_chief@mars.org"
)

make_user(
    surname="Watney",
    name="Mark",
    age=25,
    position="botanist",
    speciality="agriculture",
    address="module_2",
    email="watney@mars.org"
)

make_user(
    surname="Vogel",
    name="Alex",
    age=30,
    position="chemist",
    speciality="chemistry",
    address="module_2",
    email="vogel@mars.org"
)

make_user(
    surname="Johanssen",
    name="Beth",
    age=28,
    position="programmer",
    speciality="software",
    address="module_3",
    email="johanssen@mars.org"
)

session.commit()
session.close()
