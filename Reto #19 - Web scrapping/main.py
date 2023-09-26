# /*
#  * El día 128 del año celebramos en la comunidad el "Hola Mundo day"
#  * Vamos a hacer "web scraping" sobre su sitio web: https://holamundo.day
#  *
#  * Crea un programa que se conecte a la web del evento e imprima únicamente la agenda de eventos
#  * del día 8. Mostrando hora e información de cada uno.
#  * Ejemplo: "16:00 | Bienvenida"
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  *
#  */
from bs4 import BeautifulSoup
import requests

URL_BASE = 'https://holamundo.day/'

pedido_obtenido = requests.get(URL_BASE)
html_obtenido = pedido_obtenido.text

soup = BeautifulSoup(html_obtenido,'html.parser')
quotes = soup.find_all('blockquote')

for quote in quotes[21:]:
    print(quote.text)
