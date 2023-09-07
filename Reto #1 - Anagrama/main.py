# Escribe una función que reciba 2 palabras (String) y retorne 
# Verdadero o falso (bool) según sean o no anagramas(se leen al derecho igual que al revés)
# ej: amor => roma , saco => cosa, etc.

def anagrama(palabra:str,otra_palabra:str)->bool:
    palabra = palabra.lower()
    otra_palabra = otra_palabra.lower()

    if len(palabra) != len(otra_palabra):
        return False
    for element in palabra:
        if not element in otra_palabra:
            return False
    return True

while(True):
    palabra = input("Ingrese una palabra o quit() para salir: ")
    if (palabra =='quit()'):
        break
    otra_palabra = input("Ingrese otra palabra o quit() para salir: ")
    if (otra_palabra == 'quit()'):
        break
    if(anagrama(palabra,otra_palabra)):
        print('Verdadero')
    else:
        print('Falso')