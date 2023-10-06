# /*
#  * Crea un programa capaz de interactuar con un fichero TXT.
#  * IMPORTANTE: El fichero TXT NO debe subirse como parte de la corrección. 
#  * Únicamente el código.
#  * 
#  * - Si no existe, debe crear un fichero llamado "text.txt".
#  * - Desde el programa debes ser capaz de introducir texto por consola y guardarlo
#  *   en una nueva línea cada vez que se pulse el botón "Enter".
#  * - Si el fichero existe, el programa tiene que dar la opción de seguir escribiendo
#  *   a continuación o borrar su contenido y comenzar desde el principio.
#  * - Si se selecciona continuar escribiendo, se tiene que mostrar por consola
#  *   el texto que ya posee el fichero.  
#  */
from pathlib import Path

FILE_NAME = 'text.txt'
INITIAL_MENU = '''******************Archivos******************
Escoja una de las siguientes opciones:
1.Ingresar nueva línea
0.Salir
'''

FILE_EXISTS_MENU = '''******************Archivos******************
El archivo ya existe
Escoja una de las siguientes opciones:
1.Escribir a continuación
2.Borrar contenido del archivo
0.Salir
'''

buffer = ''
file_exists = False
while True:
    file_exists = Path(FILE_NAME).exists()
    if file_exists:
        new_line = input(FILE_EXISTS_MENU)
    else:
        new_line = input(INITIAL_MENU)

    if int(new_line) == 1:
        if file_exists:
            with open(FILE_NAME,'r',encoding='utf-8') as f:
                print(f.read())
            buffer = input('Ingrese la nueva línea: ')
            with open(FILE_NAME,'a',encoding='utf-8') as f:
                f.write(buffer+'\n')
        else:
            buffer = input('Se creó el archivo, ingrese la nueva línea: ')
            with open(FILE_NAME,'w',encoding='utf-8') as f:
                f.write(buffer+'\n')
    elif int(new_line) == 2:
        with open(FILE_NAME,'w',encoding='utf-8') as f:
            buffer = input('Se eliminó el contenido, ingrese la nueva línea: ')
            f.write(buffer+'\n')
    elif int(new_line) == 0:
        break
    
    

    

