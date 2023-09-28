from main import countdown
import pytest

def test_values_not_positive_integer():
    with pytest.raises(ValueError):
        countdown(-1,3)
        countdown(1,-3)
        countdown('1.7',-3)

def test_working_well():
    assert countdown(3,1)
    assert countdown(2,5)