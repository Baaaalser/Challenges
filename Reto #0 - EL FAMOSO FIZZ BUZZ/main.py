# Reto #0
# Escribe un programa que muestre por consola(con un print) los números del 1 al 100, sustituyendo
# por "fizz", "buzz" o "fizzbuzz" según corresponda:
# -Múltiplos de 3 por la palabra "fizz"
# -Múltiplos de 5 por la palabra "buzz"
# -Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz"
for index in range(1,101):
    print(index,end=' ')
    if (index % 3 == 0): #si el resto de dividir x 3 es 0, es múltiplo de 3
        print('fizz',end='') # no agrego el salto de línea
    if (index % 5 == 0): #si el resto de dividir x 5 es 0, es múltiplo de 5
        print('buzz',end='') # no agrego el salto de línea
    print('')
