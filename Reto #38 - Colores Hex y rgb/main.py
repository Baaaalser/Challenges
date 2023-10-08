# /*
#  * Crea las funciones capaces de transformar colores HEX
#  * a RGB y viceversa.
#  * Ejemplos:
#  * RGB a HEX: r: 0, g: 0, b: 0 -> #000000
#  * HEX a RGB: hex: #000000 -> (r: 0, g: 0, b: 0)
#  */

def rgb_hex(rgb_color:str)->str:
    hexa_dict = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    return_string = '#'
    color_list = rgb_color.split(',')
    for element in color_list:
        wich_color,value = element.split(':')
        wich_color = wich_color.lower()
        if (wich_color != 'r' and wich_color != 'g' and wich_color != 'b' or 
        int(value) > 255 or int(value) < 0):
            return 'Error'
        #hex conversion
        hexa = ''
        cocient = 0
        residual = 0
        divisor = int(value)
        while(divisor >1):
            cocient = divisor / 16
            residual = int(divisor%16)
            hexa += hexa_dict.get(residual,str(residual))
            divisor = cocient
        return_string += hexa[::-1]
    return return_string

def hex_rgb(hex_color)->str:
    hexa_dict = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    rgb_dict = {1:'r:',3:', g:',5:', b:'}
    return_string = ''
    hex_color = str(hex_color.upper().replace('#',''))
    if  len(hex_color) == 6:
        hex_val = 0
        first_digit = 0
        second_digit= 0
        for index,letter in enumerate(hex_color):
            hex_val = hexa_dict.get(letter,letter)
            first_digit = int(hex_val) * pow(16,(index + 1)%2)
            second_digit += first_digit
            if ((index + 1)%2 == 0):
                return_string += rgb_dict.get(index)+str(second_digit)
                hex_val = 0
                first_digit = 0
                second_digit= 0
        # list_return = return_string.split(',')
        # return list_return[2]+', '+list_return[1]+', '+list_return[0]
        return return_string
    
    
    

print(rgb_hex('r:135,g:240,b:59'))
print(hex_rgb('#87F03B'))

print(rgb_hex('r:113,g:168,b:50'))
print(hex_rgb('71A832'))