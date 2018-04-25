import re

f = open('test.txt')
i = 0


def hash_function(str):
    h = 0
    for i in range(0, len(str)):
        h = (h * 13 + ord(str[i])) % 100000
    return h


for line in f:
    word = re.findall(r'^\w[A-Z,\-,\s]{1,}\;', line)
    if len(word) > 0:
        word = word[0]
    result = [hash_function(word), line]
    print(result)
    if result:
        i += 1

print(i)
