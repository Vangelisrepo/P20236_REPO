alphabet="abcdefghijklmnopqrstuvwxyz"


def ROT13(lst):
    string = ""
    for x in lst:
        if x in alphabet:
            if alphabet.index(x)<13:
                string += alphabet[alphabet.index(x)+13]
            else: string += alphabet[alphabet.index(x)-13]
        else:
            if alphabet.upper().index(x) < 13:
                string += alphabet.upper()[alphabet.upper().index(x)+13]
            else: string +=alphabet.upper()[alphabet.upper().index(x)-13]
    return string
ROT13("sdDTWdsh")

