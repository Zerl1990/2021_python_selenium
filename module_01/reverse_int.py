"""Reverse an int/float value."""


def reverse(value):
    """Reverse int/float values."""
    reversed_str = str(value)[::-1]
    if type(value) == int:
        return int(reversed_str)
    elif type(value) == float:
        return float(reversed_str)
    else:
        raise ValueError(f'Reverse does not support type {type(value)}')


print(reverse(12345))
print(reverse(34.567))
