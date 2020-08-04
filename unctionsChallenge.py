age = 21
name = 'Matt'
todayIsCold = True

def helloFunction(name, age=0):
    return 'hello {0} you are {1} years old'.format(name, age)

helloFunction(name, age)

sentence = helloFunction('john')

print(sentence)