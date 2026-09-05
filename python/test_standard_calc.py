from standard_calc import bound_to_180, is_angle_between

## Utilities for testing

""" Tests for bound_to_180() """

## Edge and base cases

def test_bound_basic1():
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == -180
    assert bound_to_180(-180) == -180

def test_bound_basic2():
    assert bound_to_180(179) == 179
    assert bound_to_180(181) == -179

def test_bound_basic3(): 
    assert bound_to_180(-179) == -179
    assert bound_to_180(-181) == 179
    
def test_bound_basic4():
    assert bound_to_180(90) == 90
    assert bound_to_180(-90) == -90
    
def test_bound_basic5():
    assert bound_to_180(360) == 0
    assert bound_to_180(-360) == 0

def test_bound_basic6():
    assert bound_to_180(720) == 0
    assert bound_to_180(740) == 20

def test_bound_rounding1():
    assert bound_to_180(160.3333) == 160.333
    assert bound_to_180(-170.4444) == -170.444
    
def test_bound_rounding2():
    assert bound_to_180(120.2235) == 120.224
    assert bound_to_180(90.1245) == 90.125

""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
