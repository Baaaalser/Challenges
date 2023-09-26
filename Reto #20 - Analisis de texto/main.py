# /*
#  * Crea un programa que analice texto y obtenga:
#  * - Número total de palabras.
#  * - Longitud media de las palabras.
#  * - Número de oraciones del texto (cada vez que aparecen un punto).
#  * - Encuentre la palabra más larga.
#  *
#  * Todo esto utilizando un único bucle.
#  */

# El hotel del centro es el más antiguo del pueblo y también es aquel que tiene más comodidades. 
# Este hotel fue construido en 1911, pero primero se utilizó como casa de familia. 
# En 1975 un inversionista compró esta propiedad y la reformó para transformarla en el hotel que hoy conocemos. 
# Es un hotel pequeño, pero cuenta con servicio a la habitación, con pileta climatizada, 
# con un restaurante de categoría, entre otras cosas.



phrase = """El hotel del centro es el más antiguo del pueblo y también es aquel que tiene más comodidades. 
Este hotel fue construido en 1911, pero primero se utilizó como casa de familia. 
En 1975 un inversionista compró esta propiedad y la reformó para transformarla en el hotel que hoy conocemos. 
Es un hotel pequeño, pero cuenta con servicio a la habitación, con pileta climatizada, 
con un restaurante de categoría, entre otras cosas."""


def analyze_text(text :str):
    words = text.replace(',',' ').replace('.',' ').replace('\n',' ').split(' ')
    sentences_count = len(text.split('.'))-1# saco las oraciones y las cuento(-1 porque la última está vacía)
    index_of_longest_word = 0
    words_length = 0
    counter = 0
    another_word = []
    for word in words:
        if(word != ''):
            another_word.append(word)
        else:
            continue
        if(len(another_word[index_of_longest_word]) < len(word)):
            index_of_longest_word = counter
        words_length += len(word)
        counter+= 1
    words_count = len(another_word)
    print(f'Total words = {words_count} \nMean Length = {round(words_length/words_count,2)} \nNumber of sentences = {sentences_count} \nLongest word = {another_word[index_of_longest_word]}')

analyze_text(phrase)