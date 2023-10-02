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

#the main idea to solve this is to make a functional game with all the pieces and the posibility to play in real time
from board import Board
from pieces import Left_L,Direction
import time #the board will be updated and move down the actual piece every second
import keyboard #for key strokes capture

tablero = Board(10) #create new board
tablero.get_board()
print('')
L_izq = Left_L(tablero) #for test purposes, the pieces will be created randomly
print('')
tablero.get_board()
print('')
L_izq.move(tablero,Direction.DOWN)
print('')
L_izq.move(tablero,Direction.DOWN)
print('')
L_izq.move(tablero,Direction.DOWN)
print('')
L_izq.move(tablero,Direction.RIGHT)
print('')
L_izq.move(tablero,Direction.RIGHT)
print('')
L_izq.move(tablero,Direction.RIGHT)
print('')
L_izq.move(tablero,Direction.RIGHT)
print('')
L_izq.move(tablero,Direction.RIGHT)
print('')
L_izq.move(tablero,Direction.RIGHT)
print('')
L_izq.move(tablero,Direction.RIGHT)
print('')
L_izq.move(tablero,Direction.RIGHT)
print('')
L_izq.move(tablero,Direction.RIGHT)
print('')
L_izq.move(tablero,Direction.RIGHT)
# print(L_izq.get_name())
# print(L_izq.data)
# L_izq.rotate()
# L_izq.rotate()
# L_izq.rotate()
# L_izq.rotate()
