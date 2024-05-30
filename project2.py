# Word Counter Program
def count_words(text):
    """Counts the number of words in a given text.
    Args:
         text(str):The input text to count the words from.
    Returns:
         int: The number of words in the input text.
    """
    words = text.split() # This splits the text into a list of words.
    return len(words) #It returns the number of words.

def main():
    # Here we used main function to handle user input and display the word count.
    print("Welcome to the word counter program!")
    # Prompt the user to enter a senence or a paragraph
    user_input = input("Please enter a sentence or a paragraph:\n")

    # Check if the input is empty
    if not user_input.strip(): # Removes leading and trailing whitespace.
        print("Please enter a valid input.")
        return #Exits the program.

    # Count the number of words in the input text
    word_count = count_words(user_input)

    # Display the word count
    print(f"The input text contains {word_count} words.")
if __name__ == "__main__":
    main()
