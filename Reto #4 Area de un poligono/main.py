# Crea una unica función (sólo una) que sea capaz de calcular y retornar el área de un polígono
# -la función recibirá por parámetro sólo un polígono a la vez que podrá ser: triángulo, rectángulo y cuadrado.
# -imprime el cálculo del  área de un polígono de cada tipo

# área del rectángulo, cuadrado  b x h
# área del cuadrado  b^2
# área del triángulo con fórmula de herón(para cualquier triángulo) A = sqr(S(s-lado1)(s-lado2)(s-lado3)) siendo s = (lado1+lado2+lado3)/2

import math

class Polygon():
    def __init__(self,polygontype:str):
        self.polygontype = polygontype

    def get_type(self):
        return self.polygontype

    def get_area(self):
        pass

class Triangle(Polygon):
    def __init__(self,side1,side2,side3):
        super().__init__('Triangle')
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_area(self)-> float:
        s = (self.side1 + self.side2 + self.side3)/2
        a = math.sqrt(s*(s-self.side1)*(s-self.side2)*(s-self.side3))

        return a


class Square(Polygon):
    def __init__(self,side:int):
        super().__init__('Square')
        self.side = side
        
    def get_area(self)->float:
        return self.side**2

class Rectangle(Polygon):
    def __init__(self,side1:int,side2:int):
        self.side1 = side1
        self.side2 = side2
        super().__init__('Rectangle')
    
    def get_area(self)->float:
        return(self.side1*self.side2)


def polygonAreaCalculator(mypolygon : Polygon):
    #imprir el área:
    print(mypolygon.get_type())
    print(mypolygon.get_area())
    return


miclase = Triangle(2,3,4)
# print(miclase.polygontype)
# print(miclase.get_type())
# print(miclase.get_area())


miclase1 = Triangle(3,4,2)
miCuadrado = Square(3)
miRectangulo = Rectangle(2,3)

polygonAreaCalculator(miclase)
polygonAreaCalculator(miCuadrado)
polygonAreaCalculator(miRectangulo)