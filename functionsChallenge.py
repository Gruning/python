age = 21
name = 'Matt'
todayIsCold = True

def helloFunction(name, age=0):
    return 'hello {0} you are {1} years old'.format(name, age)

helloFunction(name, age)

sentence = helloFunction('john')

print(sentence)

#list

dognamesList = ['fido', 'sean', 'sally', 'tobi']

dognamesList.insert(0, 'pluto')
print(dognamesList)
del(dognamesList[3])
print(dognamesList)
print(dognamesList[2])
dognamesList[0] = 'Frodo'
print(dognamesList)
print(len(dognamesList))


