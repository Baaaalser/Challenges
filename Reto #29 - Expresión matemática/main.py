# /*
#  * Crea una función que reciba una expresión matemática (String)
#  * y compruebe si es correcta. Retornará true o false.
#  * - Para que una expresión matemática sea correcta debe poseer
#  *   un número, una operación y otro número separados por espacios.
#  *   Tantos números y operaciones como queramos.
#  * - Números positivos, negativos, enteros o decimales.
#  * - Operaciones soportadas: + - * / % 
#  *
#  * Ejemplos:
#  * "5 + 6 / 7 - 4" -> true
#  * "5 a 6" -> false
#  */


def check_if_correct(expresion :str) -> bool:
    expresion_list = str(expresion).split(' ') #separo por espacios
    math_list = ['+','-','*','/','%']
    valid = True
    
    for index,element in enumerate(expresion_list):#par, es número, impar operación
        if(index%2 == 0):#numero
            if ('-' in element and element.count('-') == 1):#negativo
                element = element.replace('-','')#quito el signo
            if('.' in element and element.count('.') == 1 ):#viene con decimal, si tiene más de un punto esta mal
                element = element.replace('.','')#quito el punto
            if element.isnumeric():
                continue
            else:
                return False
        else:#operador
            if math_list.count(element) == 1:
                continue
            else:
                return False
    
    return True

print(check_if_correct('5 + 6 / 7 - 4'))
print(check_if_correct('5 a 6'))
print(check_if_correct("-9.6 + 5"))
print(check_if_correct("-9.6 + -7565"))
print(check_if_correct("-9.6 - -7565"))

print(check_if_correct("3 + 5"))
print(check_if_correct("3 a 5"))
print(check_if_correct("-3 + 5"))
print(check_if_correct("- 3 + 5"))
print(check_if_correct("-3 a 5"))
print(check_if_correct("-3+5"))
print(check_if_correct("3 + 5 - 1 / 4 % 8"))

