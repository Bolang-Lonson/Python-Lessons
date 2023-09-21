def mysplit(strng):
    result = []
    if strng.isspace() or strng == '':
        return result
    spaces = strng.count(" ")
    for i in range(spaces + 1):
        substr = strng[:strng.find(" ")]
        strng = strng[strng.find(" ")+1:]
        strng.strip()
        if substr != "":
            result.append(substr)
    return result
def mysplit2(strng):
    result = []
    if strng.isspace() or strng == '':
        return result
    if not strng.endswith(' '):
        strng += " "
    if strng.startswith(" "):
        strng = strng.lstrip()
    word = ""
    for elem in strng:
        while not elem.isspace():
            word += elem
            break
        else:
            result.append(word)
            word = ""
    return result


print(mysplit2("To be or not to be, that is the question"))
print(mysplit2("To be or not to be,that is the question"))
print(mysplit2("   "))
print(mysplit2(" abc "))
print(mysplit2(""))
