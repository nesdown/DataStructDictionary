# Класс отдельного узла
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# Класс односвязного списка
class LinkedList:
    # Конструктор класса - первая ссылка, последняя, длинна списка
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        # Выведем на экран содержимое списка
        if self.first is not None:
            current = self.first
            out = 'LinkedList [\n' + str(current.value) + '\n'
            while current.next is not None:
                current = current.next
                out += str(current.value) + '\n'
            return out + ']'

    # Очистим список
    def clear(self):
        self.__init__()

    # Добавление элементов
    def add(self, x):
        self.length += 1
        # Если элемент первый, то делаем замыкание на вход и выход
        if self.first is None:
            self.last = self.first = Node(x, Node)
        # Иначе добавляем в новую ячейку памяти - присваивание произошло
        else:
            self.last.next = self.last = Node(x, None)

    # Добавление элемента в конкретную часть списка
    def ins_concrete(self, i, x):
        if self.first is None:
            self.last = self.first = Node(x, Node)
            return
        if i == 0:
            self.first = Node(x, self.first)
            return
        curr = self.first
        count = 0
        while curr is not None:
            count += 1
            if count == i:
                curr.next = Node(x, curr.next)
                if curr.next.next is None:
                    self.last = curr.next
                break
            curr = curr.next
