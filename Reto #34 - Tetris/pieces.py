#Here will be the piece template, with every piece, and the posible rotations
from abc import ABC,abstractmethod
from enum import Enum
from board import Board
import numpy

class Direction(Enum):

    LEFT = 0
    RIGHT = 1
    DOWN = 2

class Piece(ABC):
    @abstractmethod
    def __init__(self,data:[],the_board:Board) -> None:
        self.__board_bottom_reached = False
        self.__data = data #current píece
        self.__board = the_board # the board
        self.__piece_coords = []
        self.__add_to_board()

    
    def rotate(self):
        tmp_data_0 = self.__data[0][0]
        tmp_data_1 = self.__data[0][1]
        tmp_data_2 = self.__data[0][2]

        self.__data[0][0] = self.__data[2][0]
        self.__data[0][1] = self.__data[1][0]
        self.__data[0][2] = tmp_data_0

        self.__data[1][0] = self.__data[2][1]
        tmp_data_0 = self.__data[1][2]
        self.__data[1][2] = tmp_data_1

        self.__data[2][0] = self.__data[2][2]
        self.__data[2][1] = tmp_data_0
        self.__data[2][2] = tmp_data_2
        self.__update_board()

    def move(self,direction:Direction):
        coords = self.__get__board_piece_lower_corner_coord()
        print(f'Al entrar a move = {coords}')
        print(self.__board.get_heigth())
        if( self.__board_bottom_reached): #bottom reached?
            return
        if( coords[0] == (self.__board.get_heigth()-1)): #bottom reached?
            #i need to know the last row with '🔳' to set the heigth.
            self.__board.set_heigth(self.__board.calculate_bottom())
            self.__board_bottom_reached = True
            return
        if direction == Direction.DOWN:
            if(self.__board.size != self.__board.get_heigth()):#for the 1st piece i have the whole board
                partial_board = self.__board.board[0:-(self.__board.size-self.__board.get_heigth())]
                # ver de agregar una opcion de cortar y pegar la pieza de forma de no tocar el tablero mas que actualiza donde se encuentra la pieza en este momento.
                #
                partial_board_numpy = numpy.array(partial_board)
                print(partial_board_numpy[0:,coords[1]:3])
                self.__board.board = partial_board[-1:] + partial_board[:-1] + self.__board.board[-(self.__board.size-self.__board.get_heigth()):]
            else:
                self.__board.board = self.__board.board[-1:] + self.__board.board[:-1]
            self.__set__board_piece_lower_corner_coord([(coords[0]+1)%self.__board.size,coords[1]])
        elif direction == Direction.RIGHT and coords[1] < (self.__board.size-3):
            for index,row in enumerate(self.__board.board[coords[0]:3]):
                self.__board.board[index] = row[-1:] + row[:-1]
                self.__set__board_piece_lower_corner_coord([coords[0],(coords[1]+1)%self.__board.size])
        elif direction == Direction.LEFT and coords[1] > 0:
            for index,row in enumerate(self.__board.board[coords[0]:3]):
                self.__board.board[index] = row[1:] + row[:1]
                self.__set__board_piece_lower_corner_coord([coords[0],(coords[1]-1)%self.__board.size])
        self.__update_board()


    def __add_to_board(self):
        self.__set__board_piece_lower_corner_coord([0,0])
        self.__update_board()

    def __update_board(self):
        coords = self.__get__board_piece_lower_corner_coord()
        print(f'Al entrar a update = {coords}')
        if coords[0] == 1:#if piece is entering the board add the next part of the piece
            self.__board.board[0][coords[1]] = self.__data[1][0]
            self.__board.board[0][coords[1]+1] = self.__data[1][1]
            self.__board.board[0][coords[1]+2] = self.__data[1][2]

            self.__board.board[1][coords[1]] = self.__data[2][0]
            self.__board.board[1][coords[1]+1] = self.__data[2][1]
            self.__board.board[1][coords[1]+2] = self.__data[2][2]

        elif coords[0] == 2:
            self.__board.board[0][coords[1]] = self.__data[0][0]
            self.__board.board[0][coords[1]+1] = self.__data[0][1]
            self.__board.board[0][coords[1]+2] = self.__data[0][2]

            self.__board.board[1][coords[1]] = self.__data[1][0]
            self.__board.board[1][coords[1]+1] = self.__data[1][1]
            self.__board.board[1][coords[1]+2] = self.__data[1][2]

            self.__board.board[2][coords[1]] = self.__data[2][0]
            self.__board.board[2][coords[1]+1] = self.__data[2][1]
            self.__board.board[2][coords[1]+2] = self.__data[2][2]

        elif coords[0] == 0:#if piece was rotated before enter the board
            self.__board.board[0][coords[1]%self.__board.size] = self.__data[2][0]
            self.__board.board[0][(coords[1]+1)%self.__board.size] = self.__data[2][1]
            self.__board.board[0][(coords[1]+2)%self.__board.size] = self.__data[2][2]
        else:
            for row in range(0,3):
                for col in range(0,3):
                    self.__board.board[coords[0]-row][coords[1]+col] = self.__data[2-row][col]
        self.__board.get_board()

        
    #this function can only be able to work if the piece is on the board
    def __set__board_piece_lower_corner_coord(self,coords:[]):
        self.__piece_coords = coords

    def __get__board_piece_lower_corner_coord(self):
        return self.__piece_coords 
    


class Left_L(Piece):
    data=[                        #Initial position             Rotated 90 deg        Rotated 180 deg         Rotated 270 deg                                           
            ['🔲','🔲','🔲'],   #0,0 - 0,1 - 0,2        -   2,0 - 1,0 - 0,0     -   2,2 - 2,1 - 2,0     -   0,2 - 1,2 - 2,2                                                                                 
            ['🔳','🔲','🔲'],   #1,0 - 1,1 - 1,2        -   2,1 - 1,1 - 0,1     -   1,2 - 1,1 - 1,0     -   0,1 - 1,1 - 2,1                                                                                    
            ['🔳','🔳','🔳']    #2,0 - 2,1 - 2,2        -   2,2 - 1,2 - 0,2     -   0,2 - 0,1 - 0,0     -   0,0 - 1,0 - 2,0                                                                               
        ]
    def __init__(self,my_board:Board) -> None:
        super().__init__(self.data,my_board)

class Inverted_T(Piece):
    data=[                        #Initial position             Rotated 90 deg        Rotated 180 deg         Rotated 270 deg                                           
            ['🔲','🔲','🔲'],   #0,0 - 0,1 - 0,2        -   2,0 - 1,0 - 0,0     -   2,2 - 2,1 - 2,0     -   0,2 - 1,2 - 2,2                                                                                 
            ['🔲','🔳','🔲'],   #1,0 - 1,1 - 1,2        -   2,1 - 1,1 - 0,1     -   1,2 - 1,1 - 1,0     -   0,1 - 1,1 - 2,1                                                                                    
            ['🔳','🔳','🔳']    #2,0 - 2,1 - 2,2        -   2,2 - 1,2 - 0,2     -   0,2 - 0,1 - 0,0     -   0,0 - 1,0 - 2,0                                                                               
        ]
    def __init__(self,my_board:Board) -> None:
        super().__init__(self.data,my_board)
    
class Right_L(Piece):
    data=[                        #Initial position             Rotated 90 deg        Rotated 180 deg         Rotated 270 deg                                           
            ['🔲','🔲','🔲'],   #0,0 - 0,1 - 0,2        -   2,0 - 1,0 - 0,0     -   2,2 - 2,1 - 2,0     -   0,2 - 1,2 - 2,2                                                                                 
            ['🔲','🔲','🔳'],   #1,0 - 1,1 - 1,2        -   2,1 - 1,1 - 0,1     -   1,2 - 1,1 - 1,0     -   0,1 - 1,1 - 2,1                                                                                    
            ['🔳','🔳','🔳']    #2,0 - 2,1 - 2,2        -   2,2 - 1,2 - 0,2     -   0,2 - 0,1 - 0,0     -   0,0 - 1,0 - 2,0                                                                               
        ]
    def __init__(self,my_board:Board) -> None:
        super().__init__(self.data,my_board)
    
