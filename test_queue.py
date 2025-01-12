import unittest
from Queue import Queue


class TestQueue(unittest.TestCase):

    def setUp(self):
        """Создает новую очередь перед каждым тестом."""
        self.queue = Queue(max_size=3)

    def test_is_empty(self):
        """Проверяет, пустая ли очередь."""
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue("A")
        self.assertFalse(self.queue.is_empty())

    def test_is_full(self):
        """Проверяет, заполнена ли очередь."""
        self.assertFalse(self.queue.is_full())
        self.queue.enqueue("A")
        self.queue.enqueue("B")
        self.queue.enqueue("C")
        self.assertTrue(self.queue.is_full())

if __name__ == '__main__':
    unittest.main()
