def main():
    text = input("Input: ")
    output = shorten(text)
    print(f"Output: {output}")

def shorten(word):
    words = words.lower()
    s_char = ["a", "e", "i", "o", "u"]
    shortened = []
    for char in word:
        if char not in s_char:
            shortened.append(char)
    output = str("".join(shortened))
    return output


if __name__ == "__main__":
    main()