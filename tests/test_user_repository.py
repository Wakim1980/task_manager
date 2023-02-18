from _pytest.fixtures import fixture

from src.random_user import RandomUser
from src.user import User
from src.user_repository import UserRepository


@fixture
def user():
    random_user = RandomUser.generate()
    return User(0,random_user.login, str(hash(random_user.login)), random_user.last_name, random_user.first_name, random_user.email)


@fixture
def user_repository():
    user_repository = UserRepository()
    return user_repository


def test_user_add(user_repository: UserRepository, user: User):
    assert user_repository.add(user).id != 0


def test_remove(user_repository: UserRepository):
    random_user = RandomUser.generate()
    user = User(0, random_user.login, str(hash(random_user.login)), random_user.last_name, random_user.first_name,random_user.email)
    user_repository.add(user)
    assert user_repository.remove(user.id) is True


def test_user_update(user_repository: UserRepository):
    random_user = RandomUser.generate()
    user = User(0, random_user.login, str(hash(random_user.login)), random_user.last_name, random_user.first_name,random_user.email)
    user_repository.add(user)
    user.first_name = "Andrey"
    assert user_repository.update(user) is True


def test_find_by_id(user_repository: UserRepository):
    assert user_repository.find_by_id(1).login == "Wakim"


def test_find_by_login(user_repository: UserRepository):
    assert user_repository.fin_by_login("Wakim").login == "Wakim"


def test_find_by_email(user_repository: UserRepository):
    assert user_repository.find_by_email("Hludeev.Andrey1980@gmail.com").email == "Hludeev.Andrey1980@gmail.com"


def test_get_all(user_repository: UserRepository):
    assert len(user_repository.get_all()) > 0



