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
    def __init__(self,name:str) -> None:
        self.__set_name(name)
    @abstractmethod
    def rotate(self):
        pass

    @abstractmethod
    def move(self,board_:Board,wich_direction:Direction):
        pass

    @abstractmethod
    def get_name(self):
        return self.__name


    def __set_name(self,name):
        self.__name = name


class Left_L(Piece):
    data=[                        #Initial position             Rotated 90 deg        Rotated 180 deg         Rotated 270 deg                                           
            ['🔲','🔲','🔲'],   #0,0 - 0,1 - 0,2        -   2,0 - 1,0 - 0,0     -   2,2 - 2,1 - 2,0     -   0,2 - 1,2 - 2,2                                                                                 
            ['🔳','🔲','🔲'],   #1,0 - 1,1 - 1,2        -   2,1 - 1,1 - 0,1     -   1,2 - 1,1 - 1,0     -   0,1 - 1,1 - 2,1                                                                                    
            ['🔳','🔳','🔳']    #2,0 - 2,1 - 2,2        -   2,2 - 1,2 - 0,2     -   0,2 - 0,1 - 0,0     -   0,0 - 1,0 - 2,0                                                                               
        ]
    def __init__(self,my_board:Board) -> None:
        super().__init__('L_left')
        self.__board_piece_lower_corner_coord = []
        self.__board = my_board
        self.__add_to_board()

    def rotate(self):
        tmp_data_0 = self.data[0][0]
        tmp_data_1 = self.data[0][1]
        tmp_data_2 = self.data[0][2]

        self.data[0][0] = self.data[2][0]
        self.data[0][1] = self.data[1][0]
        self.data[0][2] = tmp_data_0

        self.data[1][0] = self.data[2][1]
        tmp_data_0 = self.data[1][2]
        self.data[1][2] = tmp_data_1

        self.data[2][0] = self.data[2][2]
        self.data[2][1] = tmp_data_0
        self.data[2][2] = tmp_data_2

        print(self.data)

    
    def move(self,wich_direction:Direction):
        coords = self.__get__board_piece_lower_corner_coord()
        print(f'Al entrar a move = {coords}')
        if coords[0] == self.__board.size - 1: #bottom reached?
            return
        if wich_direction == Direction.DOWN:
            self.__board.board = self.__board.board[-1:] + self.__board.board[:-1]
            self.__set__board_piece_lower_corner_coord([(coords[0]+1)%self.__board.size,coords[1]])
        elif wich_direction == Direction.RIGHT:
            for index,row in enumerate(self.__board.board):
                self.__board.board[index] = row[-1:] + row[:-1]
                self.__set__board_piece_lower_corner_coord([coords[0],(coords[1]+1)%self.__board.size])
        elif wich_direction == Direction.LEFT:
            for index,row in enumerate(self.__board.board):
                self.__board.board[index] = row[1:] + row[:1]
                self.__set__board_piece_lower_corner_coord([coords[0],(coords[1]-1)%self.__board.size])
        self.update_board()


    def update_board(self):
        coords = self.__get__board_piece_lower_corner_coord()
        print(f'Al entrar a update = {coords}')
        if coords == [1,0]:#if piece is entering the board add the next part of the piece
            self.__board.board[0][0] = self.data[1][0]
            self.__board.board[0][1] = self.data[1][1]
            self.__board.board[0][2] = self.data[1][2]
        elif coords == [2,0]:
            self.__board.board[0][0] = self.data[0][0]
            self.__board.board[0][1] = self.data[0][1]
            self.__board.board[0][2] = self.data[0][2]
        # else:
        #     if coords[0] == 9:
        #         self.__set__board_piece_lower_corner_coord([coords[0]-1,coords[1]])
        #         coords = self.__get__board_piece_lower_corner_coord()
        #         print(f'Al salir de ultimo row = {coords}')
                
            #self.__board[coords[0]][coords[1]] = 
        self.__board.get_board()
    #this function can only be able to work if the piece is on the board
    def __set__board_piece_lower_corner_coord(self,coords:[]):
        self.__board_piece_lower_corner_coord = coords

    def __get__board_piece_lower_corner_coord(self):
            return self.__board_piece_lower_corner_coord 
    
    #if the piece is created must be added to the board
    def __add_to_board(self):
        self.__board.board[0][0] = self.data[2][0]
        self.__board.board[0][1] = self.data[2][1]
        self.__board.board[0][2] = self.data[2][2]
        self.__set__board_piece_lower_corner_coord([0,0])
        self.__board.get_board()
        
        
    
    def get_name(self):
        return super().get_name()