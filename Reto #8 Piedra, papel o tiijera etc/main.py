# /*
#  * Crea un programa que calcule quien gana más partidas al piedra,
#  * papel, tijera, lagarto, spock.
#  * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
#  * - La función recibe un listado que contiene pares, representando cada jugada.
#  * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
#  *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
#  * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
#  * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
#  * - Piedra > tijera, Tijera > papel , papel > piedra, piedra > lagarto, lagarto > spock, 
#  * - lagarto > papel, papel > spock, spock > piedra, spock > tijera, tijera > lagarto.
#  */



def paper_scissors_etc(seq:[]):
    who_win = { "🗿" : ["✂️","🦎",],
            "✂️" : ["🦎","📄",],
            "🦎" : ["📄","🖖"],
            "🖖" : ["✂️","🗿"],
            "📄" : ["🗿","🖖"]
    }
    p1 = 0
    p2 = 0
    for actual_round in seq:
        if(actual_round[1] in who_win[actual_round[0]]):
            p1 += 1
        else:
            p2 += 1
    if(p1==p2):
        print('tie')
    else:
        print(f'Player { "1" if (p1 > p2)  else "2"} wins')

paper_scissors_etc([("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")])
paper_scissors_etc([("🗿","🦎"), ("✂️","🖖"), ("📄","✂️")])
paper_scissors_etc([("🗿","🦎"), ("✂️","🖖"), ("📄","✂️"),("🖖","🗿"),("🦎","📄")])
paper_scissors_etc([("🗿","🦎"), ("✂️","🖖"), ("📄","✂️"),("🖖","🗿")])