import pytest


# @pytest.fixture()
# def user_1(db):
#     user = User.objects.create_user("test-user")
#     return user
#
# @pytest.mark.django_db
# def test_set_check_password(user_1):
#     user_1.set_password("new-password")
#     assert user_1.check_password("new-passwords") is True


# Фикстура user_1 будет вызываться заново для каждого теста (по умолчанию scope='function'),
# @pytest.fixture()
# def user_1(db): # Фикстура использует фикстуру db для доступа к БД
#     user = User.objects.create_user("test-user")
#     print('create-user')
#     return user
#
# def test_set_check_password(user_1):
#     print('check-user1')
#     assert user_1.username == 'test-user'
#
# def test_set_check_password(user_1):
#     print('check-user2')
#     assert user_1.username == 'test-user'



def test_set_check_password(user_1):
    print('check-user1')
    assert user_1.username == 'test-user'

def test_set_check_password(user_1):
    print('check-user2')
    assert user_1.username == 'test-user'

