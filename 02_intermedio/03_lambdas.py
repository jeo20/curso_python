# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=9145

### Lambdas ###
"""
Las expresiones lambda en Python son una forma corta de declarar funciones pequeñas y anónimas 
(no es necesario proporcionar un nombre para las funciones lambda).
Las funciones Lambda se comportan como funciones normales declaradas con la palabra clave def
"""

def sum_two_values(
    first_value, second_value): return first_value + second_value


print(sum_two_values(2, 4))


def multiply_values(
    first_value, second_value): return first_value * second_value - 3


print(multiply_values(2, 4))


def sum_three_values(value):
    return lambda first_value, second_value: first_value + second_value + value


print(sum_three_values(5)(2, 4))