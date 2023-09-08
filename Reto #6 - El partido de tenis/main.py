# /*
#  * Escribe un programa que muestre cómo transcurre un juego de tenis y quién lo ha ganado.
#  * El programa recibirá una secuencia formada por "P1" (Player 1) o "P2" (Player 2), según quien
#  * gane cada punto del juego.
#  * 
#  * - Las puntuaciones de un juego son "Love" (cero), 15, 30, 40, "Deuce" (empate), ventaja.
#  * - Ante la secuencia [P1, P1, P2, P2, P1, P2, P1, P1], el programa mostraría lo siguiente:
#  *   15 - Love
#  *   30 - Love
#  *   30 - 15
#  *   30 - 30
#  *   40 - 30
#  *   Deuce
#  *   Ventaja P1
#  *   Ha ganado el P1
#  * - Si quieres, puedes controlar errores en la entrada de datos.   
#  * - Consulta las reglas del juego si tienes dudas sobre el sistema de puntos.   
#  */
    
class Player():
    score_list = ['Love','15','30','40','Deuce','advantage','win']
    
    def __init__(self, name : str):
        self.name = name
        self.score = 0

    def increase_score(self):
        self.score += 1
    
    def decrease_score(self):
        self.score -= 1
    
    def get_score(self):
        return self.score
    
    def show_score(self):
        return self.score_list[self.score]

    def reset_score(self):
        self.score = 0

    
def match(P1 : Player, P2 : Player, pointSeq : list):
    
    #show inital score
    print(f'{P1.show_score()} - {P2.show_score()}')

    for point in pointSeq:
        player_scores = None
        player_losing = None

        if(point.upper() == P1.name):
            player_scores = P1
            player_losing = P2
        else:
            player_scores = P2
            player_losing = P1

        player_scores.increase_score() #yep increase
        

        if(Player.score_list[player_scores.get_score()] == 'advantage' and Player.score_list[player_losing.get_score()] == 'advantage' ):# did player_scores deuce again?
            #deuce again
            player_scores.decrease_score()
            player_losing.decrease_score()
            print('Deuce')#yep 
            continue
        if(Player.score_list[player_scores.get_score()] == 'advantage' ):
            print(f'Ventaja el {player_scores.name}')
            continue
        if(Player.score_list[player_scores.get_score()] == '40' and Player.score_list[player_losing.get_score()] == '40' ):#deuce?
            print('Deuce')#yep 
            player_scores.increase_score()#put both in deuce
            player_losing.increase_score()
            continue
        if(Player.score_list[player_scores.get_score()] == 'win' or Player.score_list[player_scores.get_score()] == 'Deuce'):# did player_scores won?
            print(f'Ha ganado el {player_scores.name}') #yep show it
            player_scores.reset_score()#reset scores
            player_losing.reset_score()
            break
        print(f'{P1.show_score()} - {P2.show_score()}')

playerOne = Player('P1')
playerTwo = Player('P2')


match(playerOne,playerTwo,['P1', 'P1', 'P2', 'P2', 'P1', 'P2', 'P1', 'P1'])
print('\n')
match(playerOne,playerTwo,['P1', 'P1', 'P1', 'P2', 'P2', 'P2', 'P1', 'P2','P1','P2','p2','p1','p2','p2'])

