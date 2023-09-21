dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval", "computer": "ordinateur"}

for english, french in dictionary.items():
    print(english, "->", french)

for french in sorted(dictionary.values()):
    print(french)

dictionary.update({'duck': 'canard'})       # method to 'append' or add key and value
dictionary['bird'] = 'oiseau'   # adding key-value pair
del dictionary['computer']      # deleting particular key, use key only and not its value

dictionary.popitem()        # deleting the last key-value, before python 3.6.7 it would delete a random key-value pair

for eng, fr in dictionary.items():
    print(eng,'-->',fr)
