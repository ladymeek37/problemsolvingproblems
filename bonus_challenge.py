# 1. Think of a word the is spelled the same forwards and backwards.
# 2. Give that word a variable that will be used later in a function.
# 3. Write a function that holds a variable for the reversed word, create a for loop that captures each letter for the word backwards to forwards.
# 4. Return each letter.
# 5. Print your palindrome word to the terminal using your variables and reverser function you created!


word = "radar"


def reverser(word):
    reversed_word = ""
    for index in range(len(word) -1, -1, -1):
        reversed_word += word[index]
    return reversed_word
    print(f'{word} reversed is: {reverser(word)}')