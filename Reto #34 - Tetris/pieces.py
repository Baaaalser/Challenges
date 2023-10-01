from abc import ABC,abstractmethod
from enum import Enum
class rotation(Enum):

    DEG_45 = 0
    DEG_90 = 1
    DEG_270 = 2
    DEG_360 = 3

class piece(ABC):
    @abstractmethod
    def __init__(self,name:str) -> None:
        self.__set_name(name)
    @abstractmethod
    def rotate(self,rotate_to:rotation):
        pass

    @abstractmethod
    def move(self,move_to:str):
        pass

    @abstractmethod
    def get_name(self):
        return self.__name


    def __set_name(self,name):
        self.__name = name


class left_L(piece):
    data=[  
            ['🔲','🔲','🔲'],
            ['🔳','🔲','🔲'],
            ['🔳','🔳','🔳']
        ]
    def __init__(self) -> None:
        super().__init__('L_left')

    def rotate(self, rotate_to: rotation):
        return super().rotate(rotate_to)
    
    def move(self, move_to: str):
        return super().move(move_to)
    
    def get_name(self):
        return super().get_name()