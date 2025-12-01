def odwroc_string(s):

    if len(s) <= 1:
        return s
    return odwroc_string(s[1:]) + s[0]

print(odwroc_string("ABCDEF"))
print(odwroc_string("Kod"))
