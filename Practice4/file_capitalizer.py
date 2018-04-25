file = open('test.txt', 'r')
key = 'ZOPILOTE'
def get_val(key):
    for line in file:
        if line.__contains__(key):
            return line

print(get_val('ZOPILOTE')[len(key) + 2:])


# list_test = []
# word_add = ''
# for line in file:
#     # print('the line is: ' + line)
#     words = line.split(' ')
#     # print(words)
#     for word in words:
#         # print('The word is: ' + word)
#         for letter in word:
#             # print('the letter is: ' + letter)
#             if letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#                 word_add = word_add + letter
#                 # print(word)
#             else:
#                 word_add = ''
#
#         if word_add is not '' and len(word_add) > 2:
#             list_test.append(word_add)
#
# print(list_test)
