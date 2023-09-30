"""/*
 * Los primeros dispositivos móviles tenían un teclado llamado T9
 * con el que se podía escribir texto utilizando únicamente su
 * teclado numérico (del 0 al 9).
 *
 * Crea una función que transforme las pulsaciones del T9 a su
 * representación con letras.
 * - Debes buscar cuál era su correspondencia original.
 * - Cada bloque de pulsaciones va separado por un guión.
 * - Si un bloque tiene más de un número, debe ser siempre el mismo.
 * - Ejemplo:
 *     Entrada: 6-666-88-777-33-3-33-888
 *     Salida: MOUREDEV
 */"""
import re


def t9_translator(text : str) -> str:
    T9 = {
        2:['a','b','c'],
        3:['d','e','f'],
        4:['g','h','i'],
        5:['j','k','l'],
        6:['m','n','o'],
        7:['p','q','r','s'],
        8:['t','u','v'],
        9:['w','x','y','z'],
    }

    text = ''.join(re.findall(r"[\-\(2-9)g]",text)) #filtro que solo haya - y numeros enteros
    translated = ''
    ncount = 0
    for element in text.split('-'):
        if(element == ''):
            continue
        ncount = element.count(element[0])
        if(len(element) > 1 and len(element) != ncount):#no es el mismo num
            translated = f'Error en : {element}'
            return  translated
        if (ncount > 4 and (element[0] == 7 or element[0]== 9)):
            ncount = ncount % 4
        if (ncount > 3 and element[0] not in('7,9')):
            ncount = ncount % 3
        
        translated += T9.get(int(element[0]))[ncount-1]
    return translated    

# print(t9_translator('6-666-88-z777-33-3-33-888'))
# print(t9_translator('9-2-555-8-33-777'))



print(t9_translator("6-666-88-777-33-3-33-888"))
print(t9_translator("6-666-88-777-33-0-3-33-888"))
print(t9_translator("6-676-88-777-33-3-33-888"))
print(t9_translator("6-6a6-88-777-33-3-33-888"))
print(t9_translator(""))
print(t9_translator("2222"))

