from pint import UnitRegistry

# Unit registry - needed for calculations
ureg = UnitRegistry()

def calculate_speed(dist, dist_unit, time, time_unit):
    """Calculates speed and returns the result in m/s."""
    d = dist * ureg(dist_unit)
    t = time * ureg(time_unit)
    
    speed = d / t
    return speed.to(ureg.meter / ureg.second)

if __name__ == "__main__":
    # Quick manual test
    print("Result for 100m in 10s:", calculate_speed(100, "meters", 10, "seconds"))
