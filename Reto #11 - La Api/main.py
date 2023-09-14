# /*
#  * Llamar a una API es una de las tareas más comunes en programación.
#  *
#  * Implementa una llamada HTTP a una API (la que tú quieras) y muestra su
#  * resultado a través de la terminal. Por ejemplo: Pokémon, Marvel...
#  *
#  * Aquí tienes un listado de posibles APIs: 
#  * https://github.com/public-apis/public-apis
#  */
import requests

BASE_URL = 'https://cat-fact.herokuapp.com'

response = requests.get(f"{BASE_URL}/facts/random")
print(response.status_code)
print(response.json())