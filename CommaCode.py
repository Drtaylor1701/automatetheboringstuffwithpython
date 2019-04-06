spam = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(listValue):
    stringValue = ""
    for item in listValue:
        if item == listValue[-1]:
            stringValue = stringValue + "and " + item
            break
        stringValue = stringValue + item + ", "
    return stringValue

print(commaCode(spam))
