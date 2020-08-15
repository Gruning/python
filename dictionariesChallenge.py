# dictionaries
dogs = {'fido': 8, 'sally': 17, 'lostDog': 5, 'sean': 2}

print(dogs)
print(dogs['sally'])
del(dogs['lostDog'])
print(dogs)
dogs['newDog'] = 1
print(dogs)
# will throw error
# print(dogs['lostDog'])

# dictionaries challenge
words = ["PoGo", "Spange", "Lie-Fi"]
definitions = ["Slang for Pokemon Go",
               "To collect spare change, either from couches, passerbys on the street or any numerous other ways and means",
               "When your phone or tablet indicates that you are connected to a wireless network, however you are still unable to load webpages or use any internet services with your device"]

coolDictionary = {}
for x in range(0, 3):
    coolDictionary[words[x]] = definitions[x]
print(coolDictionary)
