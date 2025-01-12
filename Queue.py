class Queue:
    """Класс для представления очереди."""

    def __init__(self, max_size=5):
        """
        Инициализация очереди.

        :param max_size: Максимальный размер очереди (по умолчанию 5).
        """
        self.max_size = max_size
        self.queue = []

    def is_empty(self):
        """Проверяет, пустая ли очередь."""
        return len(self.queue) == 0

    def is_full(self):
        """Проверяет, заполнена ли очередь."""
        return len(self.queue) >= self.max_size

    def enqueue(self, item):
        """
        Добавляет элемент в очередь.

        :param item: Элемент для добавления в очередь.
        """
        if self.is_full():
            return "Очередь переполнена"
        self.queue.append(item)

    def dequeue(self):
        """
        Удаляет элемент из очереди и возвращает его.

        :return: Удаленный элемент или сообщение, если очередь пуста.
        """
        if self.is_empty():
            return "Очередь пуста"
        return self.queue.pop(0)

    def show(self):
        """Отображает все элементы в очереди."""
        return self.queue.copy()  # возвращаем копию для безопасности


# Пример использования класса Queue
queue = Queue()
queue.enqueue("A")
queue.enqueue("B")
print(queue.show())  # Вывод: ['A', 'B']
