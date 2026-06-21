import emoji

def emojize_string(input_string):
    """
    Prompts the user for a string and outputs the emojized version.

    Args:
        input_string (str): The string to emojize.
    """
    emojized_string = emoji.emojize(input_string, language="alias")
    print(emojized_string)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    emojize_string(user_input)
