"""This gonna be the board class and the idea will be to update it with the move/rotation of the piece"""
class board():
    def __init__(self,size:int) -> None:
        self.size = size
        self.board = ['🔲'*size]*size
        self.heigth = '🔲'*size
        self.witdh = '🔲'*size
    def get_board(self):
        for element in self.board:
            print(element)  