def replace_chars(string, char, replace):
    out = ""
    for letter in string:
        if letter == char:
            out += replace
        else:
            out += letter
    return out


print replace_chars("hello leon", "e", "yaya")
