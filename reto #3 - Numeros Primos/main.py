# Escribe un programa que se encargue de comprobar si un número es o no primo,
# hecho esto imprime los primos entre 1 y 100

# Uso el teorema de Wilson: Un número natural n > 1 es primo si y solo si el factorial (n - 1)! + 1 es divisible por n. 

def factorial(num:int):
    result:float = 1
    for index in range(1,num):
        result *= index
    if((result + 1)%num == 0):
        print(num)
    # return result

for primos in range (2,100):
    factorial(primos)