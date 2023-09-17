# /*
#  * Crea una función que sea capaz de detectar si existe un viernes 13
#  * en el mes y el año indicados.
#  * - La función recibirá el mes y el año y retornará verdadero o falso.
#  */

import datetime

def IsFriday13(year,month):
    year = int(year)
    month = int(month)
    if(year > 1900 and year < 3000 and month > 0 and month < 13):
        return (f'{datetime.date(year,month,13)} {"is friday" if(datetime.date(year,month,13).ctime()[0:3]=="Fri") else "is not Friday"}')

print(IsFriday13(2023,5))
print(IsFriday13('2023',2))
print(IsFriday13('2023','1'))