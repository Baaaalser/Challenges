#This gonna be the board class and the idea will be to update it with the move/rotation of the piece
class Board():
    def __init__(self,size:int) -> None:
        self.size = size
        # self.board = [['🔲'] *size ]*size  (since the last *size only create a copy by reference, any change in one element will replicate in the others)
        self.board = [['🔲'] *size for i in range(size)]
        self.heigth = size  # actual available board heigth(white spaces)

    def set_heigth(self,altura):
        self.heigth = altura
        return

    def get_heigth(self)-> int:
        return self.heigth
    
    def calculate_bottom(self):
        for index,element in enumerate(self.board):
            if element.count('🔳') > 0:
                return index

    def get_board(self):
        for element in self.board:
            for pixel in element:
                print(pixel,end='')  
            print('')