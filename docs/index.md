# Hello World RSE - Bartek

Assignment project using the **Pint** library for unit conversion.

## How to use?

The `calculate_speed` function takes distance and time along with their units (e.g., 'km', 'h', 'm', 's') and always returns the result in meters per second.

### Example:
```python
from hello_world.core import calculate_speed

# How many meters per second?
v = calculate_speed(100, "km", 2, "hours")
print(v)
```

## Installation
```bash
pip install pint
```
