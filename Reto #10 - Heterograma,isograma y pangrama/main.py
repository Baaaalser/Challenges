# /*
#  * Crea 3 funciones, cada una encargada de detectar si una cadena de
#  * texto es un heterograma, un isograma o un pangrama.
#  * - Debes buscar la definición de cada uno de estos términos.
#  */
# heterograma es una palabra o frase que no contiene ninguna letra repetida
# isograma es una palabra o frase en la que cada letra aparece el mismo número de veces
#pangrama es una frase en la que aparecen todas las letras del abecedario. 
# Si cada letra aparece sólo una vez, formando por tanto un heterograma, se le llama pangrama perfecto.
import collections
def heterograma(palabra:str):
    for index,letra in enumerate(palabra.replace(" ","").lower()):
        if(letra in palabra[index+1:] or letra in palabra[:index]):
            print(f'"{palabra}" No es heterograma')
            return
    print(f'"{palabra}" Es heterograma')
    return

def isograma(palabra:str):
    counts = collections.Counter(palabra.replace(" ","").lower())# counts every letter ocurrences skipping spaces
    maximum = max(counts.values()) #get count max value
    minimum = min(counts.values()) # get min value
    print(f'"{palabra}"{" es isograma" if (maximum == minimum) else " no es isograma"}') # if max = min then ok, else not.

def pangrama(palabra:str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if not(letter in palabra.replace(" ","").lower()):
            print(f'"{palabra}" no es pangrama')
            return
    print(f'"{palabra}" es pangrama')

heterograma('aledaño')
heterograma('daño')
heterograma('perro')

isograma('aledaño')
isograma('daño   ')

pangrama('aledaño')
pangrama('El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja')
heterograma('El veloz murciélago hindú comía feliz cardillo y kiwi. La cigüeña tocaba el saxofón detrás del palenque de paja')