def roman2Dec(romStr):
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    # Analyze string backwards
    romanBack = list(romStr.upper())[::-1]  # Convert to uppercase and reverse
    value = 0

    # To keep track of order
    rightVal = roman_dict[romanBack[0]]

    for numeral in romanBack:
        leftVal = roman_dict[numeral]

        # Check for subtraction
        if leftVal < rightVal:
            value -= leftVal
        else:
            value += leftVal
            rightVal = leftVal

    return value

romanStr = input("Enter a Roman Number: ")

print("Decimal Value:", roman2Dec(romanStr))
