word_without_vowels = ""

# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word:\n")
user_word = user_word.upper()  # converting to uppercase

for letter in user_word:
    # Complete the body of the loop.
    if letter in "aeiou".upper():
        continue
    word_without_vowels += letter

# Print the word assigned to word_without_vowels.
print(word_without_vowels)
