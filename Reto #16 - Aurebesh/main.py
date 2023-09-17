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

def back_from_aurebesh(word):
    word = list(word.lower())
    translated = ''
    skip = 0
    search_for = ''
    #tamaños aubesh = 5(aurek,cresh,jenth,krill,senth,trill,thesh,zerek,senth),
    # 4(besh,dorn,enth,onit,forn,grek,herf,leth,mern,nern,peth,resh,shen,wesk,xesh,yirt),
    # 6(cherek,krenth,orenth),
    # 3(esk,isk,nen,osk,gek,usk,vev)
    for index,letter in enumerate(word):
        if(skip > 0):
            skip -= 1
            continue
        skip = 0
        if(index+2 < len(word)):
            search_for = word[index]+word[index+1]+word[index+2]
            if (search_for in ('esk','isk','nen','osk','gek','usk','vev')):
                skip = 2
                translated += list(aurebesh_dict.keys())[list(aurebesh_dict.values()).index(search_for)]
                continue
        if(index+3 < len(word)):
            search_for += word[index+3]
            if (search_for in ('besh','dorn','enth','onit','forn','grek','herf','leth','mern','nern','peth','resh','shen','wesk','xesh','yirt')):
                skip = 3
                translated += list(aurebesh_dict.keys())[list(aurebesh_dict.values()).index(search_for)]
                continue
        if(index+4 < len(word)):
            search_for += word[index+4]
            if (search_for in ('aurek','cresh','jenth','krill','senth','trill','thesh','zerek','senth')):
                skip = 4
                translated += list(aurebesh_dict.keys())[list(aurebesh_dict.values()).index(search_for)]
                continue
        if(index+5 < len(word)):
            search_for += word[index+5]
            if ( search_for in ('cherek','krenth','orenth')):
                skip = 5
                translated += list(aurebesh_dict.keys())[list(aurebesh_dict.values()).index(search_for)]
                continue
        #espacio
        translated += letter
    return translated

print(aurebesh_translator('gato'))
print(aurebesh_translator('choo choo'))
print(aurebesh_translator('khantal'))
print(aurebesh_translator('energy'))
print(aurebesh_translator('renault kangoo'))

print(back_from_aurebesh(aurebesh_translator('gato')))
print(back_from_aurebesh(aurebesh_translator('choo choo')))
print(back_from_aurebesh(aurebesh_translator('khantal')))
print(back_from_aurebesh(aurebesh_translator('energy')))
print(back_from_aurebesh(aurebesh_translator('renault kangoo')))