"""Unique char in string."""


def unique_char(str):
    """Get index of first unique char."""
    frequency = {}
    unique_chars = []
    for index, char in enumerate(str):
        if char in frequency:
            frequency[char] += 1
            unique_chars = [item for item in unique_chars if item[1] != char]
        else:
            frequency[char] = 1
            unique_chars.append((index, char))

    return unique_chars[0][0]


print(unique_char('alphabet'))
print(unique_char('barbados'))
print(unique_char('barbadosrd'))
