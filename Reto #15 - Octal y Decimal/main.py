# /*
#  * Crea una función que reciba un número decimal y lo trasforme a Octal
#  * y Hexadecimal.
#  * - No está permitido usar funciones propias del lenguaje de programación que
#  * realicen esas operaciones directamente.
#  */

def octal_hexa_bin(number):
    binary = ''
    octal = ''
    hexa = ''
    hexa_dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    divisor = number
    dividend_bin = 2
    dividend_oct = 8
    dividend_hexa = 16
    cocient = 0
    residual = 0
    #binary
    while(divisor > 1):
        cocient = divisor / dividend_bin
        residual = int(divisor%dividend_bin)
        binary += str(residual)
        divisor = cocient
    print(binary[::-1])
    #octal
    cocient = 0
    residual = 0
    divisor = number
    while(divisor >1):
        cocient = divisor / dividend_oct
        residual = int(divisor%dividend_oct)
        octal += str(residual)
        divisor = cocient
    print(octal[::-1])
    #hexadecimal
    cocient = 0
    residual = 0
    divisor = number
    while(divisor >1):
        cocient = divisor / dividend_hexa
        residual = int(divisor%dividend_hexa)
        hexa += hexa_dict.get(residual,str(residual))
        divisor = cocient
    print(hexa[::-1])


octal_hexa_bin(100)
octal_hexa_bin(10)
octal_hexa_bin(730)