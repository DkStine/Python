def missingCharacters(s):
    new_str = ""

    for i in "0123456789":
        if i not in s:
            new_str += i
    
    for j in "abcdefghijklmnopqrstuvwxyz":
        if j not in s:
            new_str += j

    return new_str