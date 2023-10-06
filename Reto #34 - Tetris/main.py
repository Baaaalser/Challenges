# /*
#  * Crea un programa capaz de gestionar una pieza de Tetris.
#  * - La pantalla de juego tiene 10 filas y 10 columnas representadas por símbolos 🔲
#  * - La pieza de tetris a manejar será la siguiente (si quieres, puedes elegir otra):
#  *   🔳
#  *   🔳🔳🔳
#  * - La pieza aparecerá por primera vez en la parte superior izquierda de la pantalla de juego.
#  *   🔳🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔳🔳🔳🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  *   🔲🔲🔲🔲🔲🔲🔲🔲🔲🔲
#  * - Debes desarrollar una función capaz de desplazar y rotar la pieza en el tablero,
#  *   recibiendo una acción cada vez que se llame, mostrando cómo se visualiza en la pantalla  de juego.
#  * - Las acciones que se pueden aplicar a la pieza son: derecha, izquierda, abajo, rotar.
#  * - Debes tener en cuenta los límites de la pantalla de juego.
#  */

import random
import keyboard

#1. Crear el tablero
def crear_tablero(tamanio:int):
    tablero = [['🔲'] *tamanio for i in range(tamanio)]
    return tablero

#2. Crear la pieza
def crear_pieza():
    piezas=[[                        #Initial position             Rotated 90 deg        Rotated 180 deg         Rotated 270 deg                                           
            ['🔳','🔲','🔲'],   #0,0 - 0,1 - 0,2        -   2,1 - 1,1 - 0,1     -   1,2 - 1,1 - 1,0     -   0,1 - 1,1 - 2,1                                                                                    
            ['🔳','🔳','🔳']    #1,0 - 1,1 - 1,2        -   2,2 - 1,2 - 0,2     -   0,2 - 0,1 - 0,0     -   0,0 - 1,0 - 2,0                                                                               
        ],
        [
            ['🔳'],['🔳'],['🔳'],['🔳']
        ],
        [
            ['🔲','🔲','🔳'],
            ['🔳','🔳','🔳']
        ],
        [
            ['🔳','🔳'],
            ['🔳','🔳']
        ],
        [
            ['🔲','🔳','🔳'],
            ['🔳','🔳','🔲']
        ],
        [
            ['🔳','🔳','🔲'],
            ['🔲','🔳','🔳']
        ]

    ]
    pieza = random.choice(piezas)
    return pieza

def mostrar_tablero(tablero):
    for element in tablero:
        for pixel in element:
            print(pixel,end='')  
        print('')
    print('')
#3. meter la pieza en el tablero
def ingresar_pieza_a_tablero(tablero,data):
    coords = [0,0]
    for row in range(len(data)):
        for index,col in enumerate(data[row]):
            if tablero[row][index] != data[row][index]:
                tablero[row][index] = col
    coords[0] = row
    coords[1] = 0

    mostrar_tablero(tablero)
    return coords

#3. mover la pieza hacia abajo
def mover_abajo(tablero,data,coords):
    print(coords)
    alto_pieza = len(data)
    ancho_pieza = len(data[0])
    fondo = chequear_colision(tablero,coords,data)#chequeo colisión en cada movimiento de la pieza

    if fondo:#llego al fondo o hay colisión?
        data = crear_pieza()#agrego una pieza nueva
        coords = ingresar_pieza_a_tablero(tablero,data)
        return tablero,coords,data
    

    for i in range(ancho_pieza):
        if tablero[coords[0]+1][coords[1]+i] == '🔳' : continue
        tablero[coords[0]+1][coords[1]+i] = data[alto_pieza-1][i]#pinto la siguiente linea
    for row in range(alto_pieza-1):#muevo la pieza
        for index,col in enumerate(data[row]):#Pinto sólo la línea que me falta mover
            tablero[(coords[0]-(alto_pieza-2)+row)][index+coords[1]] = col
    coords[0] += 1 # actualizo las coordenadas de la pieza
    for row in range(coords[0]-alto_pieza+1):#limpio la linea anterior donde se encontraba la pieza
        for index in range(ancho_pieza):
            tablero[row][index+coords[1]]= '🔲'

    mostrar_tablero(tablero)
    return tablero,coords,data

#4 chequear la colisión de la pieza
def chequear_colision(tablero,coords,pieza):
    if (coords[0]+1) == 10 : #si llegué al final o si hay colisión salgo
        return True #si colisiono creo pieza nueva
    ancho_pieza = len(pieza[0])
    alto_pieza = len(pieza)
    for col_index in range(ancho_pieza):
        # if (tablero[coords[0]+1][coords[1]+col_index].count('🔳') > 0 and pieza[alto_pieza-1][col_index]=='🔳'):
        if (tablero[coords[0]+1][coords[1]+col_index] == '🔳' and pieza[alto_pieza-1][coords[1]+col_index] == '🔳'):
            return True


#5. mover pieza a la derecha
def mover_derecha(tablero,pieza,coords):
    alto_pieza = len(pieza)
    ancho_pieza = len(pieza[0])
    for row in range(alto_pieza):
        if coords[1] == (10 - len(pieza[0])) : return tablero,coords#Si la columna es la última salgo
        for row_index,row in enumerate(pieza):
            for col_index,col in enumerate(row):
                tablero[coords[0]-(len(pieza)-1)+row_index][coords[1]+col_index+1] = col
    coords[1] += 1
    for row_index in range(len(pieza)):
        tablero[coords[0]-(len(pieza)-1)+row_index][coords[1]-1]= '🔲'
    
    mostrar_tablero(tablero)
    return tablero,coords


#6. mover pieza a la izquierda
def mover_izquierda(tablero,pieza,coords):
    if coords[1] == 0 : return tablero,coords#Si la columna es la primera salgo
    for row in range(len(pieza)):
        for row_index,row in enumerate(pieza):
            for col_index,col in enumerate(row):
                tablero[coords[0]-(len(pieza)-1)+row_index][coords[1]+col_index-1] = col
    coords[1] -= 1
    for row_index in range(len(pieza)):
        tablero[coords[0]-(len(pieza)-1)+row_index][coords[1]+len(pieza[0])]= '🔲'
    
    mostrar_tablero(tablero)
    return tablero,coords

#7 Rotar la pieza
def rotar_pieza(tablero,data,coords):
    alto_pieza = len(data)-1
    ancho_pieza = len(data[0])-1
    if (coords[0]+ancho_pieza > 9 or coords[1]+alto_pieza > 9 or 
    chequear_colision(tablero,coords,data)):#si al rotar se va a de los límites o si hay colisión cancelo la rotación
        return tablero,data,coords
    
    rotated = [[''] * len(data) for i in range(len(data[0]))] # creo una lista que sea de cols * rows de la que quiero rotar
    coords[0] = coords[0] - (len (data)-1) #reseteo las coordenadas
    for row_index in range(len(data)-1,-1,-1):#roto la pieza
        for col_index,col in enumerate(data[row_index]):
            rotated[col_index][len(data)-1-row_index] = data[row_index][col_index]

    for row in range(alto_pieza+1): #reseteo el área que ocupaba la pieza previamente
        for col in range(ancho_pieza+1):
            tablero[coords[0]+row][coords[1]+col] = '🔲'

    
    for row_index,row in enumerate(rotated):#actualizo el tablero con la nueva pieza
        for col_index,col in enumerate(row):
            tablero[coords[0]+row_index][coords[1]+col_index] = col
    coords[0] = coords[0] + (len(rotated)-1)#actualizo las coordenadas de la pieza

    mostrar_tablero(tablero)
    return tablero,rotated,coords



tablero = crear_tablero(10)
print('')
pieza = crear_pieza()
print('')
coords = ingresar_pieza_a_tablero(tablero,pieza)
print('')


def presione_tecla(evento):
    global tablero,pieza,coords
    # print(evento.scan_code)
    if evento.scan_code == 75:
        tablero,coords = mover_izquierda(tablero,pieza,coords)
    elif evento.scan_code == 77:
        tablero,coords = mover_derecha(tablero,pieza,coords)
    elif evento.scan_code == 72:
        tablero,pieza,coords = rotar_pieza(tablero,pieza,coords)
    elif evento.scan_code == 80:
        tablero,coords,pieza = mover_abajo(tablero,pieza,coords)

keyboard.on_press(presione_tecla)
# con esc salimos.
keyboard.wait("ESC") 
#dejo de capturar teclado
keyboard.unhook_all() 