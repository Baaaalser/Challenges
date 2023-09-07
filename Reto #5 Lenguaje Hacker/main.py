# Enunciado:
# /*
#  * Escribe un programa que reciba un texto y transforme lenguaje natural a
#  * "lenguaje hacker" (conocido realmente como "leet" o "1337"). Este lenguaje
#  *  se caracteriza por sustituir caracteres alfanuméricos.
#  * - Utiliza esta tabla (https://www.gamehouse.com/blog/leet-speak-cheat-sheet/) 
#  *   con el alfabeto y los números en "leet".
#  *   (Usa la primera opción de cada transformación. Por ejemplo "4" para la "a")
#  */

def convert_to_hacker_language(text_to_covert : str):

    dictionary = {"a":"4","b":"I3","c":"[","d":")",
                    "e":"3","f":"|=","g":"&","h":"#",
                    "i":"1","j":",_|","k":">|","l":"1",
                    "m":"/\/\\","n":"^/","o":"0","p":"|*",
                    "q":"(_,)","r":"I2","s":"5","t":"7",
                    "u":"(_)","v":"\/","w":"\/\/","x":"><",
                    "y":"j","z":"2"," ":" "}
    
    #first i need to lowercase te word so i can check against the dict
    text_to_covert = text_to_covert.lower()
    #now is ready for conversion
    #printing one by one for comparisson
    for letter in text_to_covert:
        print(dictionary[letter],letter)
    #the join version
    return "".join(dictionary[letter] for letter in text_to_covert)    
mytext = 'Hola Mundo'
print(convert_to_hacker_language(mytext))