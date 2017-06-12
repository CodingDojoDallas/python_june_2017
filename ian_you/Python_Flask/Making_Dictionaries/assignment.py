name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_dict = {}
    for i in range (0,len(arr1)):
        new_dict[str(arr1[i])]= str(arr2[i])
    print new_dict
    return new_dict

make_dict(name, favorite_animal)


#Hacker Challenge

names = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar", "James", "Paolo", "Ian", "Authman", "Matt"]
animals = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def unevenDict(arr3, arr4):
    new_dict1 = {}
    if len(arr3) > len(arr4):
        keyList = arr3
        valList = arr4
    elif len(arr3) < len(arr4):
        keyList = arr4
        valList = arr3
    for i in range (0, len(valList)):
        new_dict1[str(keyList[i])]=str(valList[i])
    for j in range (len(valList), len(keyList)):
        new_dict1[str(keyList[j])]=""

    print new_dict1
    return new_dict1

unevenDict(names, animals)
