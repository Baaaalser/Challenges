# /*
#  * Crea una función que encuentre todos los triples pitagóricos
#  * (ternas) menores o iguales a un número dado.
#  * - Debes buscar información sobre qué es un triple pitagórico.
#  * - La función únicamente recibe el número máximo que puede
#  *   aparecer en el triple.
#  * - Ejemplo: Los triples menores o iguales a 10 están
#  *   formados por (3, 4, 5) y (6, 8, 10).
#  *
from itertools import combinations

def pitagorical_triade(number : int):
    num_list = [i  for i in range(3,number+1)]#saco una lista de los número menores
    combs = list(combinations(num_list, 3))
    unq = set(combs)#convertir a set para sacar los valores únicos
    for el in unq:
        if pow(el[0],2)+pow(el[1],2) == pow(el[2],2):
            print(el)

pitagorical_triade(8)
print('-------------------------')
pitagorical_triade(10)
print('-------------------------')
pitagorical_triade(15)
print('-------------------------')
pitagorical_triade(20)
