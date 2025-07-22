import pytest
from django.contrib.auth.models import User


@pytest.fixture()
def user_1(db): # Фикстура использует фикстуру db для доступа к БД
    user = User.objects.create_user("test-user")
    print('create-user')
    return user

@pytest.fixture
def new_user_factory():
    def create_app_user(
            username: str,
            password: str=None,
            first_name: str = 'firstname',
            last_name: str = 'lastname',
            is_staff: str = False,
            is_superuser: str = False,
            is_active: str = True,
    ):
        user = User.objects.create_user(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )
    return create_app_user