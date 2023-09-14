# /*
#  * Dada una URL con parámetros, crea una función que obtenga sus valores.
#  * No se pueden usar operaciones del lenguaje que realicen esta tarea directamente.
#  *
#  * Ejemplo: En la url https://retosdeprogramacion.com?year=2023&challenge=0
#  * los parámetros serían ["2023", "0"]
#  */

def get_params(url:str)-> []:
    params = url.split('?')[1]
    p_data = []
    for param in (params.split('&')):
        p_data.append(param.split('=')[1])
    return p_data

print(get_params('https://retosdeprogramacion.com?year=2023&challenge=0'))
print(get_params('https://retosdeprogramacion.com?year=2023'))
print(get_params('https://retosdeprogramacion.com?year=2023&challenge=0&param1=1&param2=2432'))