# импортируем библиотеку:
import pytest

# импортируем код тестируемого приложения Калькулятор:
# app.calculator - значит, что в папке app лежит файл calculator
from app.calculator import Calculator

# создаем класс тестируемого приложения, которые обязательно начинаются со слова Test:
class TestCalc:
    # определяем подготовительный метод setup в котором подключаем тестируемый объект
    def setup(self):
        # создаем объект калькулятора из импортируемого класса
        self.calc = Calculator

    # пишем тесты, которые обязательно начинаются со слова test
    # функция умножения (multiply), которую проверяем и результат (correctly), который она должна вернуть
    def test_multiply_calculate_correctly(self):
        # assert сравниваем ожидание с результатом
        assert self.calc.multiply(self, 5, 5) == 25

    # # добавим отрицательный тест для умножения (как шпаргалка на будущее)
    # def test_multiply_calculation_failed(self):
    #     assert self.calc.multiply(self, 5, 5) == 26

    # функция деления (division) положительный тест
    def test_division_calculate_correctly(self):
        # assert сравниваем ожидание с результатом
        assert self.calc.division(self, 30, 3) == 10

    # # добавим отрицательный тест для деления (как шпаргалка на будущее)
    # def test_division_calculation_failed(self):
    #     assert self.calc.division(self, 30, 3) == 20

    # функция вычитания (subtraction) положительный тест
    def test_subtraction_calculate_correctly(self):
        # assert сравниваем ожидание с результатом
        assert self.calc.subtraction(self, 208, 8) == 200

    # # добавим отрицательный тест для вычитания (как шпаргалка на будущее)
    # def test_subtraction_calculation_failed(self):
    #     assert self.calc.subtraction(self, 208, 8) == 100

    # функция сложения (adding) положительный тест
    def test_adding_calculate_correctly(self):
        # assert сравниваем ожидание с результатом
        assert self.calc.adding(self, 150, 170) == 320

    # # добавим отрицательный тест для сложения (как шпаргалка на будущее)
    # def test_adding_calculation_failed(self):
    #     assert self.calc.adding(self, 150, 170) == 330