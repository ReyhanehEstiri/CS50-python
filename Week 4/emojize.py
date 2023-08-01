import emoji

def main():
    emojize()

def emojize():
    input_emoji = input("Input:")
    print("Output:",emoji.emojize(input_emoji))

if __name__ == "__main__":
    main()
