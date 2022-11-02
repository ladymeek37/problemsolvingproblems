# 1. Choose the word or phrase you want to be reversed.
# 2. Give that word a variable that will be used later in a function.
# 3. Write a function that holds a variable for the reversed word, create a for loop that captures each letter for the word backwards to forwards.
# 4. Return each letter.
# 5. Print your reversed letters to the terminal using your new reverser function.




def reverser(word):
    reversed_word = ""
    for index in range(len(word) -1, -1, -1):
        reversed_word += word[index]
    return reversed_word

