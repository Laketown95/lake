def convert(text):
    text = text.replace(":)","🙂")
    text = text.replace(":(","🙁")
    return text

def main():
    text = input()

    print(convert(text))
if __name__ == "__main__":
# Call the main function directly
    main()
