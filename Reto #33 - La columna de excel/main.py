"""/*
 * Crea una función que calcule el número de la columna de una hoja de Excel
 * teniendo en cuenta su nombre.
 * - Las columnas se designan por letras de la "A" a la "Z" de forma infinita.
 * - Ejemplos: A = 1, Z = 26, AA = 27, CA = 79.
 */"""

import re
def column_calculator(column_name : str)-> int:
    column_name = ''.join(re.findall(r"[a-zA-Zgm]",column_name))#solo letras
    num_value = 0
    for index,letter in enumerate(column_name[::-1]):
        num_value += (ord(letter.upper())-64) * pow(26,index)#convierto letra a su ordinal, y lo multiplico x 26^posicion
    print((num_value))

column_calculator('A')
column_calculator('c')
column_calculator('CA')
column_calculator('zza')
column_calculator('AA')
column_calculator('zz')
column_calculator('aaa')
column_calculator('xfd')
column_calculator('ZZZ')
column_calculator('aaaa')
column_calculator('ZZZz')

