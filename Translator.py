def translate(phrase):
    result = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                result += "Z"
            else:
                result += "z"
        else:
            result += letter
    return result


print("\nZ Translator: \n")
word = input("Enter a phrase: ")
translation = translate(word)
print(f"{word} --> {translation}")
