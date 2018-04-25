import re
import llist

class Hash:
    def __init__(self, value=None, word=None):
        self.value = 0
        self.word = None

    def get_word(self):
        self.word = input('Enter the word: ')

    def hash_function(self, data=None):
        self.__init__()
        # self.get_word()

        for i in range(0, len(data)):
            self.value = (self.value * 13 + ord(data[i])) % 100000

        return self.value

    def get_value(self):
        f = open('test.txt')
        i = 0
        # print('Opened!')
        for line in f:
            word = re.findall(r'^\w[A-Z,\-,\s]{1,}\;', line)
            if len(word) > 0:
                word = word[0]
                # print(word)
            result = llist.LinkedList()
            result.add(self.hash_function(word))
            result.add(line)
            print(result)
            if result:
                i += 1
        print(i)


