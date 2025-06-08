# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

dictionary = {
    "नमस्ते": "Hello",
    "धन्यवाद": "Thank you",
    "कृपया": "Please",
    "शुभकामनाएँ": "Best wishes",
    "सुप्रभात": "Good morning",
    "शुभ रात्रि": "Good night",
    "आप कैसे हैं?": "How are you?",
    "मुझे माफ करें": "Excuse me",
}
print("Welcome to the Hindi-English Dictionary!")
while True:
    hindi_word = input("Enter a Hindi word to look up (or type 'exit' to quit): ")
    if hindi_word.lower() == 'exit':
        print("Thank you for using the dictionary. Goodbye!")
        break
    translation = dictionary.get(hindi_word)
    if translation:
        print(f"The English translation of '{hindi_word}' is: {translation}")
    else:
        print(f"Sorry, the word '{hindi_word}' is not in the dictionary.")
    print("Available Hindi words:", ", ".join(dictionary.keys()))