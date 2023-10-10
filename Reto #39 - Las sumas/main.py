# /*
#  * Crea una función que encuentre todas las combinaciones de los números
#  * de una lista que suman el valor objetivo.
#  * - La función recibirá una lista de números enteros positivos
#  *   y un valor objetivo.
#  * - Para obtener las combinaciones sólo se puede usar
#  *   una vez cada elemento de la lista (pero pueden existir
#  *   elementos repetidos en ella).
#  * - Ejemplo: Lista = [1, 5, 3, 2],  Objetivo = 6
#  *   Soluciones: [1, 5] y [1, 3, 2] (ambas combinaciones suman 6)
#  *   (Si no existen combinaciones, retornar una lista vacía)
#   */


def permutations(head : list, total:int, tail = 0,result = []):
    if sum(head) == total:
        head.sort()#acomodo así no repito patrón
        if result.count(head) == 0 and head is not None:
            print('Result:',head)
            result.append(head)
        return
    else:
        for i in range(len(head)):
            permutations(list(head[:i] + head[i+1:]),total,tail+head[i],result)

lista = [1,5,3,2]

permutations(lista,6)
permutations([1,2,1,3,1,1,2,1,4,2,2], 7)
permutations([1,2,1,3,1,1,2,1,4,2,2], 8)