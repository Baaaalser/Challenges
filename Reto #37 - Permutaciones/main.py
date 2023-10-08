# /*
#  * Crea un programa que sea capaz de generar e imprimir todas las 
#  * permutaciones disponibles formadas por las letras de una palabra.
#  * - Las palabras generadas no tienen por qué existir.
#  * - Deben usarse todas las letras en cada permutación.
#  * - Ejemplo: sol, slo, ols, osl, los, lso 
#  */


def permutations(head, tail=''):
    if len(head) == 0:
        print(tail)
    else:
        for i in range(len(head)):
            permutations(head[:i] + head[i+1:], tail + head[i])

print(permutations('sol'))