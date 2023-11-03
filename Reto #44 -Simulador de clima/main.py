# /*
#  * Crea una función que simule las condiciones climáticas (temperatura y probabilidad de lluvia)
#  * de un lugar ficticio al pasar un número concreto de días según estas reglas:
#  * - La temperatura inicial y el % de probabilidad de lluvia lo define el usuario.
#  * - Cada día que pasa:
#  *   - 10% de posibilidades de que la temperatura aumente o disminuya 2 grados.
#  *   - Si la temperatura supera los 25 grados, la probabilidad de lluvia al día 
#  *     siguiente aumenta en un 20%.
#  *   - Si la temperatura baja de 5 grados, la probabilidad de lluvia al día 
#  *     siguiente disminuya en un 20%.
#  *   - Si llueve (100%), la temperatura del día siguiente disminuye en 1 grado.
#  * - La función recibe el número de días de la predicción y muestra la temperatura
#  *   y si llueve durante todos esos días.
#  * - También mostrará la temperatura máxima y mínima de ese periodo y cuántos días va a llover.
#  */

import random

def clime(place:str,temp:float,rain_prob:int,days:int):
    temp_min = temp
    temp_max = 0
    rainy = False
    rainy_counter = 0
    for day in range(1,days):
        prob = random.randint(1,10)#entre 1 y 10 cada uno es un 10% de probabilidad
        if prob == 1 and not rainy:
            temp += 2
        if prob == 2 or rainy:
            temp -= 2
        if temp > 25:
            rain_prob +=2
        if temp < 5 and rain_prob > 0:
            rain_prob -=2
            if rain_prob < 0 : rain_prob = 0
        prob = random.randint(1,10)
        if (rain_prob >= prob):
            rainy = True
            rainy_counter +=1
        else:
            rainy = False
        if temp > temp_max:
            temp_max = temp
        if temp < temp_min:
            temp_min = temp
        print(f"el día {day} {'llueve' if rainy else 'no llueve'}, la temperatura será de {temp}° en {place}")
    print(f'La máxima para el período indicado será de {temp_max} y la temperatura mínima será de {temp_min} y loverá {rainy_counter} días.')

clime("un lugar ficticio",5,3,15)