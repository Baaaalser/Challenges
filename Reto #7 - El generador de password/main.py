# /*
#  * Escribe un programa que sea capaz de generar contraseñas de forma aleatoria.
#  * Podrás configurar generar contraseñas con los siguientes parámetros:
#  * - Longitud: Entre 8 y 16.
#  * - Con o sin letras mayúsculas.
#  * - Con o sin números.
#  * - Con o sin símbolos.
#  * (Pudiendo combinar todos estos parámetros entre ellos)
#  */


import random

letters = 'abcdefghijklmnopqrstuvwxyz'
nums = '0123456789'
symbs = '~!@#$%^&*()+?><|'

password = ''

password += letters

print('Generador de contraseñas')
while True:
    length = int(input('Ingrese longitud de la contraseña(8-16): '))
    if (length >= 8 or length <=16):
        break

while True:
    uppercase = input('Usar mayúsculas? S/N:')
    if(uppercase.lower() == 's'):
        password += letters.upper()
        break
    if(uppercase.lower() == 'n'):
        break

while True:
    numbers = input('Usar números? S/N:')
    if(numbers.lower() == 's'):
        password += nums
        break
    if(numbers.lower() == 'n'):
        break

while True:
    symbols = input('Usar símbolos? S/N:')
    if(symbols.lower() == 's'):
        password += symbs
        break
    if(symbols.lower() == 'n'):
        break

print(f'Password = {"".join(random.sample(password,length))}')
