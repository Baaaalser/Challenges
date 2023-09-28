# /*
#  * Crea una función que reciba dos parámetros para crear una cuenta atrás.
#  * - El primero, representa el número en el que comienza la cuenta.
#  * - El segundo, los segundos que tienen que transcurrir entre cada cuenta.
#  * - Sólo se aceptan números enteros positivos.
#  * - El programa finaliza al llegar a cero.
#  * - Debes imprimir cada número de la cuenta atrás.
#  */
import time
def countdown(begin : int,lapse : int):
    begin = int(begin)
    lapse = int(lapse)
    if begin > 0 and lapse > 0:
        while begin > 0:
            print(begin)
            time.sleep(lapse)
            begin -=1
        print(begin)
        return True
    else:
        raise ValueError("Only positive integers are allowed")

#countdown(5,2)
