hexNumbers = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
}

# Converts a string hexadecimal number into an integer decimal
# If hexNum is not a valid hexadecimal number, returns None
def hexToDec(hexNum):
    result = 0

    for char in hexNum:
        if char not in hexNumbers:
            return None
        else:
            result = result * 16 + hexNumbers[char]

    return result


# 10
print(hexToDec('A'))

# 0
print(hexToDec('0'))

# 27
print(hexToDec('1B'))

# 960
print(hexToDec('3C0'))

# None
print(hexToDec('A6G'))

# None
print(hexToDec('ZZTOP'))