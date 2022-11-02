word = "Hello"


def reverser(word):
    reversed_word = ""
    for index in range(len(word) -1, -1, -1):
        reversed_word += word[index]
    return reversed_word

print(f'Hello reversed is: {reverser("Hello")}')