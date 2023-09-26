# /*
#  *	¡El nuevo "The Legend of Zelda: Tears of the Kingdom" ya está disponible! 
#  *
#  * Crea un programa que dibuje una Trifuerza de "Zelda"
#  * formada por asteriscos.
#  * - Debes indicarle el número de filas de los triángulos con un entero positivo (n).
#  * - Cada triángulo calculará su fila mayor utilizando la fórmula 2n-1.
#  *
#  * Ejemplo: Trifuerza 2
#  * 
#  *    *
#  *   ***
#  *  *   *
#  * *** ***
#  *
#  */

def draw_triforce(lines : int):#asi entendí que era
    rows = 2*lines - 1
    triforce = ' *  '
    triforce_2 = '*** '

    for index in range(1,rows):
        print(f'{" "*((rows-index)*2)}{triforce*index}')
        print(f'{" "*((rows-index)*2)}{triforce_2*index}')


def draw_triforce_corregido(lines : int):#asi tenía que ser
    rows = 2*lines
    for row in range(1,rows+1):
        if row <= lines:
            print(' '*(round((rows-row))),end='')
            print('*'*(2*row-1))
        else:
            print(' '*(round((2*lines-row))),end='')
            print('*'*(2*(row-lines)-1),end='')
            print(' '*(round(rows%(row)*2)+1),end='')
            print('*'*(2*(row-lines)-1))

            
draw_triforce(3)
draw_triforce(4)

draw_triforce_corregido(3)
draw_triforce_corregido(4)
draw_triforce_corregido(30)