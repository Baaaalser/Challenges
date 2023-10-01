"""/*
 * Crea una función que sea capaz de leer el número representado por el ábaco.
 * - El ábaco se representa por un array con 7 elementos.
 * - Cada elemento tendrá 9 "O" (aunque habitualmente tiene 10 para realizar operaciones)
 *   para las cuentas y una secuencia de "---" para el alambre.
 * - El primer elemento del array representa los millones, y el último las unidades.
 * - El número en cada elemento se representa por las cuentas que están a la izquierda del alambre.
 *
 * Ejemplo de array y resultado:
 * ["O---OOOOOOOO",
 *  "OOO---OOOOOO",
 *  "---OOOOOOOOO",
 *  "OO---OOOOOOO",
 *  "OOOOOOO---OO",
 *  "OOOOOOOOO---",
 *  "---OOOOOOOOO"]
 *  
 *  Resultado: 1.302.790
 */"""


def abacus(num_list : list)->str:
    dec_value = ''
    if(not isinstance(num_list,list) or len(num_list) != 7):
        return 'Error: no se recibió un entrada de datos válida'
    for index,number in enumerate(num_list):
        str_num = str(number)
        if str_num.count('-') != 3 or str_num.count('O') != 9:
            return f'Error: el formato es inválido en la posición {index} para el elemento {str_num}'
        dec_value += str(number.split('---')[0].count('O'))
    
    return '{:,}'.format(int(dec_value)).replace(',','.')

abacus_list = ["O---OOOOOOOO",
          "OOO---OOOOOO",
          "---OOOOOOOOO",
          "OO---OOOOOOO",
          "OOOOOOO---OO",
          "OOOOOOOOO---",
          "---OOOOOOOOO"]





print(abacus(abacus_list))