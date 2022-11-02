# def compress(string):
#     index = 0
#     compressed = ""
#     len_string = len(string)
#     while index != len_string:
#         count = 1 
#         while (index < len_string - 1) and (string[index] == string[index+1]):
#             count = count + 1 
#             index = index + 1
#         if count == 1:
#             compressed += str(string[index])
#         else:
#             compressed += str(string[index])+ str(count)
#         index = index + 1
#     return compressed

# string = "lllaaaaadddddyy"
# print (compress(string))

# 1. Write a function that will pick the first character from the string.
# 2. Add it to the compressed string. 
# 3. Count the number of repeated occurences of the letter and add that number to the compressed string.
# 4. Repeat the same method with the next defferent letter and keep going until the end of the string is reached. 
# 5. Print the compressed string to thr terminal.


def compress(string):
    index = 0
    compressed = ""
    len_string = len(string)
    while index != len_string:
        count = 1
        while (index < len_string -1) and (string[index] == string[index + 1]):
            count += 1
            index += 1
        if count == 1:
            compressed += str(string[index])
        else:
            compressed += str(string[index])+ str(count)
        index = index + 1
    return compressed

string = "hhhheeeelllloollladddyy"
print (compress(string))