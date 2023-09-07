# Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci
# empezando en 0, el siguiente siempre es la suma de los 2 previos
# ej: 0, 1 , 1 , 2 , 3 , 5 , 8 , 13....



prev_value = 0
prev_value2 = 1

for index in range(0,50):
    print(prev_value)
    fibo = prev_value + prev_value2
    prev_value = prev_value2
    prev_value2 = fibo
    