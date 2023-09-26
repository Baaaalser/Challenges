# /*
#  * Crea un programa que encuentre y muestre todos los pares de números primos
#  * gemelos en un rango concreto.
#  * El programa recibirá el rango máximo como número entero positivo.
#  * 
#  * - Un par de números primos se considera gemelo si la diferencia entre
#  *   ellos es exactamente 2. Por ejemplo (3, 5), (11, 13)
#  *
#  * - Ejemplo: Rango 14
#  *   (3, 5), (5, 7), (11, 13)
#  */



def prime_range(num:int):
    first_prime = 2
    prime_pair_list = []
    for number in range(2,num):
        result:float = 1
        for index in range(1,number):
            result *= index
        if((result + 1)%number == 0):
            if((number-first_prime)==2):
                prime_pair_list.append((first_prime,number))
            first_prime = number  
    print(prime_pair_list)


prime_range(14)