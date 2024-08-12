from allure import step
from pydantic import BaseModel, Field


@step('Модель регистрации пользователя')
class UserRegistrationModel(BaseModel):
    email: str = Field(default="random-email-test@mail.ru")
    password: str = Field(default="some_p@ss0rd-123")
    name: str = Field(default="Yuri Gagarin")


@step('Модель авторизации пользователя')
class UserLoginModel(BaseModel):
    email: str = Field(default="random-email-test@mail.ru")
    password: str = Field(default="some_p@ss0rd-123")
