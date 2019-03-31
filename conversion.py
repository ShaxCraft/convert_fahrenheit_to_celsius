# Конверсия градусов Фаренгейта в градусы Цельсия.
# Conversion of Fahrenheit degrees to Celsius degrees.

from data import *


# Формула конверсии в градусы Цельсия.
# Formula conversion to degrees Celsius.
def celsius():
    c = (fahrenheit - 32) / 1.8
    return c
