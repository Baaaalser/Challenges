# /*
#  * Crea tres test sobre el reto 12: "Viernes 13".
#  * - Puedes copiar una solución ya creada por otro usuario en
#  *   el lenguaje que estés utilizando.
#  * - Debes emplear un mecanismo de ejecución de test que posea
#  *   el lenguaje de programación que hayas seleccionado.
#  * - Los tres test deben de funcionar y comprobar
#  *   diferentes situaciones (a tu elección).
#  */


import datetime
import pytest

def IsFriday13(year,month):
    year = int(year)
    month = int(month)
    if(year > 1900 and year < 3000 and month > 0 and month < 13):
        return (f'{datetime.date(year,month,13)} {"is friday" if(datetime.date(year,month,13).ctime()[0:3]=="Fri") else "is not Friday"}')

print(IsFriday13(2023,5))
print(IsFriday13('2023',2))
print(IsFriday13('2023','1'))
print(IsFriday13(20233,5))
print(IsFriday13('2023',5.4))

def test_variables_texto():
    """This must fail because only accepts ints or string with number in it
    """
    with pytest.raises(ValueError):
        IsFriday13('2 mil 23',5)
    
    with pytest.raises(ValueError):
        IsFriday13('2023','cinco')

    with pytest.raises(ValueError):
        IsFriday13('2023','2.7')
    
def test_year_over_boundaries():
    assert IsFriday13(20233,5) == None
    assert IsFriday13(3000,5) == None
    assert IsFriday13(3000,13) == None

def test_if_working_well():
    assert 'is friday' in IsFriday13('2023','1')
    assert 'is friday' in IsFriday13(2023,'1')
    assert 'is friday' in IsFriday13(2023,1)
    assert 'is friday' in IsFriday13('2023',1)
    assert 'is not Friday' in IsFriday13(2023,'2')
    assert 'is not Friday' in IsFriday13(2023,3.4)