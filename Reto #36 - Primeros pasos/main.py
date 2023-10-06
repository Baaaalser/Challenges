# /*
#  * Como cada año, el día 256 se celebra el "Día de la Programación".
#  * En nuestra comunidad siempre hacemos una gran fiesta donde repartirmos 
#  * 256 regalos para seguir aprendiendo programación:
#  * https://diadelaprogramacion.com
#  *
#  * Para seguir ayudando, te propongo este reto:
#  * Mostrar la sintaxis de los principales elementos de un lenguaje
#  * en TODOS los lenguajes de programación que podamos. ¿Llegaremos a 50?
#  *
#  * En un fichero, haz lo siguiente (si el lenguaje lo soporta),
#  * y comenta cada bloque para identificar con qué se corresponde:
#  * - Haz un "Hola, mundo!"
#  * - Crea variables de tipo String, numéricas (enteras y decimales)
#  *   y Booleanas (o cualquier tipo de dato primitivo).
#  * - Crea una constante.
#  * - Usa un if, else if y else.
#  * - Crea estructuras como un array, lista, tupla, set y diccionario.
#  * - Usa un for, foreach y un while.
#  * - Crea diferentes funciones (con/sin parámetros y con/sin retorno).
#  * - Crea una clase.
#  * - Muestra el control de excepciones.
#  *
#  * Así, cualquier persona podrá consultar rápidamente diferentes ejemplos
#  * de sintaxis básica de muchos lenguajes.
#  *
#  * ¡Muchas gracias!
#  */

string = "Hola mundo"
entero = 1
flotante = 2.5
booleana = True

CONST_WANNA_BE = "Constante"

if booleana :
    print(string)
elif entero != 2:
    pass
else:
    pass

my_array = [0,1,2,3]
my_tuple = (0,1,2,3)
my_set = set((2,3,'a','hola mundo'))
my_dict = {'a':'hola','b':'mundo'}

for i in range(5):
    print(my_dict)

for a in my_set:
    print(a)

while booleana:
    booleana = False

def funcion():
    print(my_tuple)
    return

funcion()

def otra_funcion(data:set)-> bool:
    print(data)
    return True
print(otra_funcion(my_set))

class Gato():
    def __init__(self,color_pelaje:str):
        self.color_pelaje = color_pelaje

    def maullar(self):
        print('Miau')

    
my_gato = Gato('Verde')
my_gato.maullar()

try:
    my_tuple[0] = 10
except Exception as e:
    print(e)