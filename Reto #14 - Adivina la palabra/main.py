# /*
#  * Crea un pequeño juego que consista en adivinar palabras en un número máximo de intentos:
#  * - El juego comienza proponiendo una palabra aleatoria incompleta
#  *   - Por ejemplo "m_ur_d_v", y el número de intentos que le quedan
#  * - El usuario puede introducir únicamente una letra o una palabra (de la misma longitud que
#  *   la palabra a adivinar)
#  *   - Si escribe una letra y acierta, se muestra esa letra en la palabra. Si falla, se resta
#  *     uno al número de intentos
#  *   - Si escribe una resolución y acierta, finaliza el juego, en caso contrario, se resta uno
#  *     al número de intentos
#  *   - Si el contador de intentos llega a 0, el jugador pierde
#  * - La palabra debe ocultar de forma aleatoria letras, y nunca puede comenzar
#  *   ocultando más del 60%
#  * - Puedes utilizar las palabras que quieras y el número de intentos que consideres
#  */

import random


def riddle(word):
    tildes = ("àáâãäåèéêëìíîïòóôõöùúûü")
    vocales = ("aaaaaaeeeeiiiiooooouuuu")
    quitatildes = str.maketrans(tildes, vocales)
    tries = 3
    length = len(word)
    hidden_word = list(word.translate(quitatildes).lower())
    print(hidden_word)
    number_hidden = random.randrange(int(0.3*length),int(0.6*length)) # between 30 - 60% of the word
    counter = 0
    while (counter <= number_hidden):
        hidden_word[random.randrange(0,length)] = '_'
        counter += 1
    won = False
    while (tries > 0 and not won): 
        found = False
        print("".join(hidden_word))
        print(f'Intentos {tries}')
        guess = input('Ingrese una letra, la palabra o Quit para salir:')
        if (len(guess) < length and not guess.lower() == 'quit'):
            for index,letter in enumerate(hidden_word):
                if(letter == '_'):
                    if word.translate(quitatildes)[index] == guess.lower():
                        hidden_word[index] = guess
                        found = True
                        if (not '_' in hidden_word): won = True
            if not found : tries -=1 
        elif(guess.lower() == 'quit'):
            break
        elif(len(guess)==length):
            if (guess.translate(quitatildes).lower() == word.translate(quitatildes).lower()):
                won = True
            else:
                tries -=1
        else:
            guess = input(f'la palabra no puede superar los {length} caracteres!')
    if(not won): 
        print('You lose!')
    else:
        print('You won!')
    


# riddle('adivinanza')
riddle('otorrinolaringólogo')