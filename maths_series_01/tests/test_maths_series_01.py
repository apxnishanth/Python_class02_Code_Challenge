from maths_series_01.maths_series_package import fibonacci
from maths_series_01.maths_series_package import lucas
from maths_series_01.maths_series_package import common_series


def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_fibonacci_0():
    assert fibonacci(0) == 0

def test_fibonacci_2():
    assert fibonacci(2) == 1

def test_fibonacci_3():
    assert fibonacci(3) == 2   

def test_fibonacci_8():
   assert fibonacci(8) == 21   

def test_fibonacci_1():
    assert fibonacci(1) == 1

def test_lucas_0():
    assert lucas(0) == 2  

def test_lucas_1():
    assert lucas(1) == 1

def test_lucas_7():
    assert lucas(7) == 29

def test_common_series_0():
    assert common_series('f',0) == 0

def test_common_series_3():
    assert common_series('f',3) == 2

def test_common_series_7():
    assert common_series('l',7) == 29   
     
