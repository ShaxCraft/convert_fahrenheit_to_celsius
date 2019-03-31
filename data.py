# Данные пользователя в градусах Фаренгейта.
# User data in degrees Fahrenheit.

ErrorInput = 'Keep digital data!\n\n'  # Введите цыфровые данные!

try:
    fahrenheit = float(input('Enter degrees Fahrenheit:\n'))  # Введите градусы Фаренгейта
except:
    print(ErrorInput)
