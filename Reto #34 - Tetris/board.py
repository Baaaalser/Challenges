class board():
    def __init__(self,size:int) -> None:
        self.size = size
        self.board = ['🔲'*size]*size
        self.heigth = '🔲'*size
        self.witdh = '🔲'*size
    def get_board(self):
        for element in self.board:
            print(element)  