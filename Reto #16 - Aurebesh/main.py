# /*
#  * Crea una función que sea capaz de transformar Español al lenguaje básico 
#  * del universo Star Wars: el "Aurebesh".
#  * - Puedes dejar sin transformar los caracteres que no existan en "Aurebesh".
#  * - También tiene que ser capaz de traducir en sentido contrario.
#  *  
#  * ¿Lo has conseguido? Nómbrame en twitter.com/mouredev y escríbeme algo en Aurebesh.
#  *
#  * ¡Que la fuerza os acompañe!
#  */

aurebesh_dict = {   "a":"aurek","b":"besh","c":"cresh","ch":"cherek","d":"dorn",
                    "e":"esk","ae":"enth","eo":"onit","f":"forn","g":"grek",
                    "h":"herf","i":"isk","j":"jenth","k":"krill","kh":"krenth",
                    "l":"leth","m":"mern","n":"nern","ng":"nen","o":"osk","oo":"orenth",
                    "p":"peth","q":"qek","r":"resh","s":"senth","sh":"shen","t":"trill",
                    "th":"thesh","u":"usk","v":"vev","w":"wesk","x":"xesh",
                    "y":"yirt","z":"zerek","s":"senth"," ":" "}

def aurebesh_translator(word):
    word = list(word.lower())
    translated = ''
    skip = False
    for index,letter in enumerate(word):
        if(skip):
            skip = False
            continue
        if letter in ('c','a','e','k','n','o','s','t') and index < len(word)-1:
            if letter+word[index+1] in ('ch','ae','eo','kh','ng','oo','sh','th'):
                skip = True
                translated += aurebesh_dict.get(letter+word[index+1])
                continue
        translated += aurebesh_dict.get(letter)
    return translated

print(aurebesh_translator('gato'))
print(aurebesh_translator('choo choo'))
print(aurebesh_translator('khantal'))
print(aurebesh_translator('energy'))
print(aurebesh_translator('renault kangoo'))
