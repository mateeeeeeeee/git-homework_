def unikaluri(word):
    listi = []
    for i in word:
        if i in listi:
            return False
        elif i not in listi:
            listi.append(i)
    return True

