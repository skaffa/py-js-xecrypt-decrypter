def XUcrypt(XEcryptString):
    XEcryptValues = XEcryptString[1:].split(".")
    XEcryptChars = []
    modeMap = {}
    maxCount = 1
    mode = None
    decoded = ""

    for i in range(len(XEcryptValues) // 3):
        j = 0
        for k in range(3):
            j += int(XEcryptValues[k + 3 * i])
        XEcryptChars.append(j)
        if j not in modeMap:
            modeMap[j] = 1
        else:
            modeMap[j] += 1
            if modeMap[j] > maxCount:
                maxCount = modeMap[j]
                mode = j

    key = mode - 32
    for char in XEcryptChars:
        decoded += chr(char - key)

    return decoded
