#Here will be the piece template, with every piece, and the posible rotations
from abc import ABC,abstractmethod
from enum import Enum
from board import Board

class Direction(Enum):

    LEFT = 0
    RIGHT = 1
    DOWN = 2

class Piece(ABC):
    @abstractmethod
    def __init__(self,name:str,data:[],the_board:Board) -> None:
        self.__set_name(name)
        self.__data = data
        self.__board = the_board
        self.__board_piece_lower_corner_coord = []
        self.__add_to_board()

    @abstractmethod
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

    @abstractmethod
    def move(self,wich_direction:Direction):
        coords = self.__get__board_piece_lower_corner_coord()
        print(f'Al entrar a move = {coords}')
        if coords[0] == self.__board.size - 1: #bottom reached?
            return
        if wich_direction == Direction.DOWN:
            self.__board.board = self.__board.board[-1:] + self.__board.board[:-1]
            self.__set__board_piece_lower_corner_coord([(coords[0]+1)%self.__board.size,coords[1]])
        elif wich_direction == Direction.RIGHT:
            for index,row in enumerate(self.__board.board[coords[0]:3]):
                self.__board.board[index] = row[-1:] + row[:-1]
                self.__set__board_piece_lower_corner_coord([coords[0],(coords[1]+1)%self.__board.size])
        elif wich_direction == Direction.LEFT:
            for index,row in enumerate(self.__board.board[coords[0]:3]):
                self.__board.board[index] = row[1:] + row[:1]
                self.__set__board_piece_lower_corner_coord([coords[0],(coords[1]-1)%self.__board.size])
        self.__update_board(wich_direction)

    @abstractmethod
    def get_name(self):
        return self.__name

    def __add_to_board(self):
        self.__set__board_piece_lower_corner_coord([0,0])
        self.__update_board()

    def __update_board(self,wich_direction = Direction.DOWN):
        coords = self.__get__board_piece_lower_corner_coord()
        print(f'Al entrar a update = {coords}')
        if coords[0] == 1 and wich_direction :#if piece is entering the board add the next part of the piece
            self.__board.board[0][coords[1]] = self.__data[1][0]
            self.__board.board[0][coords[1]+1] = self.__data[1][1]
            self.__board.board[0][coords[1]+2] = self.__data[1][2]
        elif coords[0] == 2 and wich_direction :
            self.__board.board[0][coords[1]] = self.__data[0][0]
            self.__board.board[0][coords[1]+1] = self.__data[0][1]
            self.__board.board[0][coords[1]+2] = self.__data[0][2]
        elif coords[0] == 0 and wich_direction :#if piece was rotated before enter the board
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
        self.__board_piece_lower_corner_coord = coords

    def __get__board_piece_lower_corner_coord(self):
            return self.__board_piece_lower_corner_coord 
    
    def __set_name(self,name):
        self.__name = name


class Left_L(Piece):
    data=[                        #Initial position             Rotated 90 deg        Rotated 180 deg         Rotated 270 deg                                           
            ['🔲','🔲','🔲'],   #0,0 - 0,1 - 0,2        -   2,0 - 1,0 - 0,0     -   2,2 - 2,1 - 2,0     -   0,2 - 1,2 - 2,2                                                                                 
            ['🔳','🔲','🔲'],   #1,0 - 1,1 - 1,2        -   2,1 - 1,1 - 0,1     -   1,2 - 1,1 - 1,0     -   0,1 - 1,1 - 2,1                                                                                    
            ['🔳','🔳','🔳']    #2,0 - 2,1 - 2,2        -   2,2 - 1,2 - 0,2     -   0,2 - 0,1 - 0,0     -   0,0 - 1,0 - 2,0                                                                               
        ]
    def __init__(self,my_board:Board) -> None:
        super().__init__('L_left',self.data,my_board)

    def rotate(self):
        super().rotate()
    
    def move(self,wich_direction:Direction):
        super().move(wich_direction)

    
    def get_name(self):
        return super().get_name()
    

class Inverted_T(Piece):
    data=[                        #Initial position             Rotated 90 deg        Rotated 180 deg         Rotated 270 deg                                           
            ['🔲','🔲','🔲'],   #0,0 - 0,1 - 0,2        -   2,0 - 1,0 - 0,0     -   2,2 - 2,1 - 2,0     -   0,2 - 1,2 - 2,2                                                                                 
            ['🔲','🔳','🔲'],   #1,0 - 1,1 - 1,2        -   2,1 - 1,1 - 0,1     -   1,2 - 1,1 - 1,0     -   0,1 - 1,1 - 2,1                                                                                    
            ['🔳','🔳','🔳']    #2,0 - 2,1 - 2,2        -   2,2 - 1,2 - 0,2     -   0,2 - 0,1 - 0,0     -   0,0 - 1,0 - 2,0                                                                               
        ]
    def __init__(self,my_board:Board) -> None:
        super().__init__('L_left',self.data,my_board)

    def rotate(self):
        super().rotate()
    
    def move(self,wich_direction:Direction):
        super().move(wich_direction)
    
    def get_name(self):
        return super().get_name()
    
class Right_L(Piece):
    data=[                        #Initial position             Rotated 90 deg        Rotated 180 deg         Rotated 270 deg                                           
            ['🔲','🔲','🔲'],   #0,0 - 0,1 - 0,2        -   2,0 - 1,0 - 0,0     -   2,2 - 2,1 - 2,0     -   0,2 - 1,2 - 2,2                                                                                 
            ['🔲','🔲','🔳'],   #1,0 - 1,1 - 1,2        -   2,1 - 1,1 - 0,1     -   1,2 - 1,1 - 1,0     -   0,1 - 1,1 - 2,1                                                                                    
            ['🔳','🔳','🔳']    #2,0 - 2,1 - 2,2        -   2,2 - 1,2 - 0,2     -   0,2 - 0,1 - 0,0     -   0,0 - 1,0 - 2,0                                                                               
        ]
    def __init__(self,my_board:Board) -> None:
        super().__init__('L_left',self.data,my_board)
    
    def rotate(self):
        super().rotate()
    
    def move(self,wich_direction:Direction):
        super().move(wich_direction)
    
    def get_name(self):
        return super().get_name()