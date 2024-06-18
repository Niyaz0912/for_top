import pytest
from teacher import Teacher


@pytest.fixture()
def teacher():
    teacher = Teacher("test_name", "test_surname", "test_phone")
    return teacher