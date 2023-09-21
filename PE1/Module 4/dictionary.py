dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
Contacts = {'boss': 5551234567, 'Suzy': 22657854310, 'Mum': 677666343, 'Dad': 651318638}
empty_dictionary = {}

print(dictionary)

print("Contacts")
for contact in Contacts.keys():
    print(contact, ':', Contacts[contact])

names = tuple(Contacts.keys())
numbers = list(Contacts.values())
print("names", names)
print("numbers", numbers)

pol_eng_dictionary = {
    "kwiat": "flower",
    "woda": "water",
    "gleba": "soil"
    }

item_1 = pol_eng_dictionary["gleba"]    # ex. 1
print(item_1)    # outputs: soil

item_2 = pol_eng_dictionary.get("woda")
print(item_2)    # outputs: water

