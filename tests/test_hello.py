import pytest
from hello_world.core import calculate_speed, ureg

def test_simple_speed():
    # Checking if 100m in 10s is 10m/s
    v = calculate_speed(100, "m", 10, "s")
    assert v.magnitude == 10
    assert v.units == ureg.meter / ureg.second

def test_unit_conversion():
    # Checking km/h to m/s
    v = calculate_speed(36, "km", 1, "hour")
    assert v.magnitude == 10.0

