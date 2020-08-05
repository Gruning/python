age = 21
name = 'Matt'
todayIsCold = True

def helloFunction(name, age=0):
    return 'hello {0} you are {1} years old'.format(name, age)

helloFunction(name, age)

sentence = helloFunction('john')

print(sentence)

#list

dognames = ['fido', 'sean', 'sally', 'tobi']

dognames.insert(0, 'pluto')
print(dognames)
del(dognames[3])
print(dognames)
print(dognames[2])
dognames[0] = 'Frodo'
print(dognames)
print(len(dognames))
