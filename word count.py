def count_words(text):
    words = text.split()
    return len(words)

def word_counter():
    user_input = input("Enter a sentence or paragraph: \n")

    if not user_input.strip():
        print("You entered an empty string. Please enter some text.")
    else:
        word_count = count_words(user_input)
        print(f"The number of words in the given text is: {word_count}")

#calling the function
word_counter()