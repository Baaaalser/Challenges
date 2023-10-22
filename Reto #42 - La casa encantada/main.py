# /*
#  * Este es un reto especial por Halloween.
#  * Te encuentras explorando una mansión abandonada llena de habitaciones.
#  * En cada habitación tendrás que resolver un acertijo para poder avanzar a la siguiente.
#  * Tu misión es encontrar la habitación de los dulces.
#  *
#  * Se trata de implementar un juego interactivo de preguntas y respuestas por terminal.
#  * (Tienes total libertad para ser creativo con los textos)
#  *
#  * - 🏰 Casa: La mansión se corresponde con una estructura cuadrada 4 x 4
#  *   que deberás modelar. Las habitaciones de puerta y dulces no tienen enigma.
#  *   (16 habitaciones, siendo una de entrada y otra donde están los dulces)
#  *   Esta podría ser una representación:
#  *   🚪⬜️⬜️⬜️
#  *   ⬜️👻⬜️⬜️
#  *   ⬜️⬜️⬜️👻
#  *   ⬜️⬜️🍭⬜️
#  * - ❓ Enigmas: Cada habitación propone un enigma aleatorio que deberás responder con texto.
#  *   Si no lo aciertas no podrás desplazarte.
#  * - 🧭 Movimiento: Si resuelves el enigma se te preguntará a donde quieres desplazarte.
#  *   (Ejemplo: norte/sur/este/oeste. Sólo deben proporcionarse las opciones posibles)
#  * - 🍭 Salida: Sales de la casa si encuentras la habitación de los dulces.
#  * - 👻 (Bonus) Fantasmas: Existe un 10% de que en una habitación aparezca un fantasma y
#  *   tengas que responder dos preguntas para salir de ella.
#  */

import random
from enum import Enum

class Mansion():
    def __init__(self):
        self.actual_room = [0,0]
        self.door = [0,0]
        self.candy = [0,0]
        self.row = 0
        self.col = 0
        self.__generate_door_candy()
        self.questions = {
            0:{
                "pregunta":"Es duro y redondo y se mete hasta el fondo. ¿Qué es?",
                "respuesta": "El anillo"
            },
            1:{
                "pregunta":"Desaparezco en cuanto me nombras. ¿Qué soy?",
                "respuesta": "El silencio"
            },
            2:{
                "pregunta":"Tengo agujas y no se coser, tengo números y no se leer. ¿Qué soy?",
                "respuesta": "El reloj"
            },
            3:{
                "pregunta":"Qué es lo que puedes encontrar una vez en un minuto, dos veces en un momento y ninguna vez en cien años?",
                "respuesta": "La letra M"
            },
            4:{
                "pregunta":"Qué se agranda en cuánto más le quitas?",
                "respuesta": "Un Agujero"
            },
            5:{
                "pregunta":"Van en la sopa pero no se comen ¿Qué es?",
                "respuesta": "La cuchara y el plato"
            },
            6:{
                "pregunta":"Entra en los mares y ríos, pero no se moja ¿Qué es?",
                "respuesta": "Los rayos de sol"
            },
            7:{
                "pregunta":"No muerde ni ladra, tiene dientes y cuida la casa ¿Qué es?",
                "respuesta": "La llave"
            },
            8:{
                "pregunta":"Silba sin labios,corre sin pies te toca y no lo ves ¿Qué es?",
                "respuesta": "El viento"
            },
            9:{
                "pregunta":"Es algo y nada a la vez ¿Qué es?",
                "respuesta": "El pez"
            },

        }
        
        
    def __generate_door_candy(self):
        are_same = True
        self.door[0] = random.randint(0,3)
        if self.door[0]==0 or self.door[0]==3:
            self.door[1]=random.randint(0,3)
        else:
            self.door[1]= random.choice([0,3])
        while are_same:
            self.candy[0] = random.randint(0,3)
            if self.candy[0]==0 or self.candy[0]==3:
                self.candy[1]=random.randint(0,3)
            else:
                self.candy[1]= random.choice([0,3])
            if self.door != self.candy:
                are_same = False
        self.actual_room = self.door
        return
    
class Movement(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


class play_mansion():
    def __init__(self) -> None:
        self.mansion = Mansion()
        self.won = False
        self.ghost = False
        self.start_game()
    
    def move(self,where:int):
        print(type(self.mansion.actual_room[0]))
        if where == Movement.UP.value and self.mansion.actual_room[0] != 0:
                self.mansion.actual_room[0] -= 1
        elif where == Movement.DOWN.value and self.mansion.actual_room[0] != 3:
                self.mansion.actual_room[0] += 1
        elif where == Movement.RIGHT.value and self.mansion.actual_room[1] != 3:
                self.mansion.actual_room[1] += 1
        elif where == Movement.LEFT.value and self.mansion.actual_room[1] != 0:
                self.mansion.actual_room[1] -= 1 
        else:
            print('No hay más habitaciones')
        if self.mansion.actual_room == self.mansion.candy:
            self.won = True
        return

    def get_question(self):
        if (random.randint(1,10) > 1): 
            return
        else:#%10
            self.ghost = True
            return
    def ask_questions(self,num:int):
        while num > 0:
            question = random.choice(self.mansion.questions)
            response = 'Nada'
            while response.lower() not in question['respuesta'].lower():
                response = input(question['pregunta'])
            num -= 1
        self.ghost = False
        return

    def start_game(self):
        menu = """Ingrese una de las siguientes opciones:
        1.Ir hacia arriba
        2.Ir hacia abajo
        3.Ir a la izquierda
        4.Ir a la derecha
        """
        while not self.won:
            resp = input(menu)
            if not resp.isnumeric() or int(resp) < 1 or int(resp) > 4 :
                continue
            else:
                self.move(int(resp))
                if not self.won:
                    self.get_question()
                    if self.ghost:
                        self.ask_questions(2)
                    else:
                        self.ask_questions(1)
                else:
                    print('You won!!!')
                        


game = play_mansion()
