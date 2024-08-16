from allure import step
from pydantic import BaseModel, Field


class OrderDataModel(BaseModel):
    fluorescent_bread_r2_d3: str = Field(default='61c0c5a71d1f82001bdaaa6d')
    biocotlet_from_the_martian_magnolia: str = Field(default='61c0c5a71d1f82001bdaaa71')
    fake_ingredient_id: str = Field(default='1234567890abcdefghijklmn')
    ingredients_key: str = Field(default="ingredients")

    @step('Модель заказа')
    def order_data(self) -> dict:
        return {
            self.ingredients_key: [
                self.fluorescent_bread_r2_d3,
                self.biocotlet_from_the_martian_magnolia,
                self.fluorescent_bread_r2_d3,
            ]
        }

    @step('Пустая модель ингредиентов')
    def empty_ingredients_data(self) -> dict:
        return {self.ingredients_key: []}

    @step('Модель несуществующих ингредиентов')
    def fake_ingredients_data(self) -> dict:
        return {self.ingredients_key: list(self.fake_ingredient_id)}

