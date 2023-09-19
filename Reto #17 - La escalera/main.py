# /*
#  * Crea una función que dibuje una escalera según su número de escalones.
#  * - Si el número es positivo, será ascendente de izquiera a derecha.
#  * - Si el número es negativo, será descendente de izquiera a derecha.
#  * - Si el número es cero, se dibujarán dos guiones bajos (__).
#  * 
#  * Ejemplo: 4
#  *         _
#  *       _|       
#  *     _|
#  *   _|
#  * _|
#  * 
#  */


def stairs(num : int):
    going_up = '_|'
    going_down = '|_'
    going_forward = '__'

    if(num > 0):
        for index in range(0,num):
            print(f'{" "*(num-index)}{going_up}')
    elif(num < 0):
        for index in range(0,num*-1):
            print(f'{" "*index}{going_down}')
    else:
        print(going_forward)

stairs(5)
stairs(0)
stairs(-8)