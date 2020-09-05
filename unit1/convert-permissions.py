def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]

    # Iterate over each of the digits in octal
    for c in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if c >= value:
                result += letter
                c -= value
            else:
                result += "-"

    return result


print(octal_to_string(755))
print(octal_to_string(644))
print(octal_to_string(750))
