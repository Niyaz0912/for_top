class Node:
    """Класс для создания  очереди. В атрибутах данные хранящиеся в узле и ссылка на следующий узел очереди
    (по умолчанию None)"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс представляет очередь данных"""
    def __init__(self, head=None, tail=None):
        """Функция инициализирует очередь. С головой head и хвостом tail (по умолчанию None)"""
        self.head = head
        self.tail = tail

    def enqueue(self, data):
        """Функция добавляет новый элемент (данные) в конец очереди. Если очередь пуста узел становится головой очереди"""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next_node = new_node
        self.tail = new_node

    def dequeue(self):
        """Функция удаляет и возвращает элемент с головы очереди. если очередь пуста возвращает None """
        if self.head is None:
            return None
        else:
            dequeue_item = self.head
            self.head = self.head.next_node
        return dequeue_item.data
