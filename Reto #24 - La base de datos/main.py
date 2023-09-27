# /*
#  * Realiza una conexión desde el lenguaje que hayas seleccionado a la siguiente base de datos MySQL:
#  * - Host: mysql-5707.dinaserver.com
#  * - Port: 3306
#  * - User: mouredev_read
#  * - Password: mouredev_pass
#  * - Database: moure_test
#  * 
#  * Una vez realices la conexión, lanza la siguiente consulta e imprime el resultado:
#  * - SELECT * FROM `challenges`
#  *
#  * Se pueden usar librerías para realizar la lógica de conexión a la base de datos.
#  */

import pymysql.cursors
import pymysql

# Connect to the database
connection = pymysql.connect(host='mysql-5707.dinaserver.com',
                            user='mouredev_read',
                            password='mouredev_pass',
                            db='moure_test',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)


try:

    with connection.cursor() as cursor:
        sql = "SELECT * FROM `challenges`"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
        #{'id': 1, 'name': 'EL FAMOSO "FIZZ BUZZ"', 'difficulty': 'Fácil', 'date': datetime.date(2022, 12, 26)}
finally:
    connection.close()