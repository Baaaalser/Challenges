# /*
#  * Crea una función que calcule el punto de encuentro de dos objetos en movimiento
#  * en dos dimensiones.
#  * - Cada objeto está compuesto por una coordenada xy y una velocidad de desplazamiento
#  *   (vector de desplazamiento) por unidad de tiempo (también en formato xy).
#  * - La función recibirá las coordenadas de inicio de ambos objetos y sus velocidades.
#  * - La función calculará y mostrará el punto en el que se encuentran y el tiempo que tardarn en lograrlo.
#  * - La función debe tener en cuenta que los objetos pueden no llegar a encontrarse.   
#  */

from enum import Enum

class movement(Enum):
    STATIC=0
    UP=1
    DOWN=2
    RIGHT=3
    LEFT=4

class objMov():
    def __init__(self,coords:list,speed:list) -> None:
        self.coords = coords
        self.speed = speed

    def show_coords(self):
        print(f"x: {self.coords[0]}")
        print(f"y: {self.coords[1]}")

    def show_speed(self):
        print(f"x speed : {self.speed[0]} m/s")
        print(f"y speed : {self.speed[1]} m/s")

def calculate_colision(obj_a : objMov,obj_b: objMov):
    a_direction = [movement.STATIC,movement.STATIC] #dirección en ambas coordenadas, estáticos en un principio
    b_direction = [movement.STATIC,movement.STATIC]
    # dirección?
    if obj_a.speed[0] > 0 :
        print("a is moving forward from left to right")
        a_direction[0] = movement.RIGHT
    elif obj_a.speed[0] == 0 :
        print("a is static")
    else:
        print("a is moving backward from right to left")
        a_direction[0] = movement.LEFT
    
    if obj_a.speed[1] > 0 :
        print("a is moving upward")
        a_direction[1] = movement.UP
    elif obj_a.speed[1] == 0 :
        print("a is static")
    else:
        print("a is moving downward")
        a_direction[1]= movement.DOWN
    


    if obj_b.speed[0] > 0 :
        print("b is moving forward from left to right")
        b_direction[0] = movement.RIGHT
    elif obj_b.speed[0] == 0 :
        print("b is static and wont collide with a")
    else:
        print("b is moving backwards from right to left")
        b_direction[0] = movement.LEFT


    if obj_b.speed[1] > 0 :
        print("b is moving upward")
        b_direction[1] = movement.UP
    elif obj_b.speed[1] == 0 :
        print("b is static and wont collide with a")
    else:
        print("b is moving downward")
        b_direction[1] = movement.DOWN

    #casos en que se encuentran
    #a y b se mueven en la misma dirección y el que va "detrás" va más rapido
    #a y b se mueven en diferente dirección pero acercándose

    # t = módulo(Xa-Xb / Va-Vb)
    #calculo en X
    d,v,t0,t1 = None,None,None,None
    
    if (((obj_a.coords[0] < obj_b.coords[0]) and (a_direction[0] == movement.RIGHT and b_direction[0]== movement.RIGHT) and (obj_a.speed[0] > obj_b.speed[0])) or
        ((obj_a.coords[0] > obj_b.coords[0]) and (a_direction[0] == movement.LEFT and b_direction[0]== movement.LEFT) and (obj_a.speed[0] < obj_b.speed[0])) or
        ((obj_a.coords[0] > obj_b.coords[0]) and (a_direction[0] == movement.LEFT and b_direction[0]== movement.RIGHT)) or
        ((obj_a.coords[0] < obj_b.coords[0]) and (a_direction[0] == movement.RIGHT and b_direction[0]== movement.LEFT))):
        
        d = obj_a.coords[0] - obj_b.coords[0]
        v = obj_a.speed[0] - obj_b.speed[0]

        t0 = abs(d/v)
    if ((a_direction[0] == movement.STATIC and b_direction[0] == movement.STATIC)and(obj_a.coords[0]== obj_b.coords[0])):
        t0 = 0
    
    #calculo en y

    if(((obj_a.coords[1] < obj_b.coords[1]) and (a_direction[1] == movement.UP and b_direction[1]== movement.UP) and (obj_a.speed[1] > obj_b.speed[1])) or
        ((obj_a.coords[1] > obj_b.coords[1]) and (a_direction[1] == movement.DOWN and b_direction[1]== movement.DOWN) and (obj_a.speed[1] < obj_b.speed[1])) or
        ((obj_a.coords[1] > obj_b.coords[1]) and (a_direction[1] == movement.DOWN and b_direction[1]== movement.UP)) or
        ((obj_a.coords[1] < obj_b.coords[1]) and (a_direction[1] == movement.UP and b_direction[1]== movement.DOWN))):
        
        d = obj_a.coords[1] - obj_b.coords[1]
        v = obj_a.speed[1] - obj_b.speed[1]

        t1 = abs(d/v)
    
    if ((a_direction[0] == movement.STATIC and b_direction[0] == movement.STATIC)and(obj_a.coords[0]== obj_b.coords[0])):
        if t1 is not None:
            X = obj_a.coords[0] + (obj_a.speed[0] * t1)
            Y = obj_a.coords[1] + (obj_a.speed[1] * t1)
            print(f"Collision at coords ({X},{Y} in {t1} seconds)")
    elif ((a_direction[1] == movement.STATIC and b_direction[1] == movement.STATIC)and(obj_a.coords[1]== obj_b.coords[1])):
        if t0 is not None:
            X = obj_a.coords[0] + (obj_a.speed[0] * t0)
            Y = obj_a.coords[1] + (obj_a.speed[1] * t0)
            print(f"Collision at coords ({X},{Y} in {t1} seconds)")

    elif t0 == t1:
        X = obj_a.coords[0] + (obj_a.speed[0] * t0)
        Y = obj_a.coords[1] + (obj_a.speed[1] * t0)
        print(f"Collision at coords ({X},{Y} in {t0} seconds)")
    else:
        print("Wont collide")

# point_one = objMov([1,0],[2,3])
# point_two = objMov([2,3],[1,4])

# point_one = objMov([0,0],[0,3])
# point_two = objMov([0,3],[0,-3])

# point_one = objMov([-1,14],[2,-3])
# point_two = objMov([7,3],[-1,4])

point_one = objMov([-10,10],[2,-2])
point_two = objMov([10,-10],[-2,2])

point_one.show_coords()
point_one.show_speed()

point_two.show_coords()
point_two.show_speed()


calculate_colision(point_one,point_two)