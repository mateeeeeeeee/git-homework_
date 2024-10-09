def asoebis_tvla(word):
    asoebis_raodenoba = {}
    for i in word:
        if i in asoebis_raodenoba:
            asoebis_raodenoba[i] += 1
        else:
            asoebis_raodenoba[i] = 1
    return asoebis_raodenoba

print(asoebis_tvla("hello"))