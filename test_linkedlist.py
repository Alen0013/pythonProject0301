import unittest
from LinkedList import LinkedList

class TestLinkedList(unittest.TestCase):

    def setUp(self):
        """Создает новый связный список перед каждым тестом."""
        self.ll = LinkedList()

    def test_insert_at_head(self):
        """Проверяет вставку узла в начало списка."""
        self.ll.insert_at_head(1)
        self.assertEqual(self.ll.head.data, 1)
        self.ll.insert_at_head(2)
        self.assertEqual(self.ll.head.data, 2)

    def test_insert_at_end(self):
        """Проверяет вставку узла в конец списка."""
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.assertEqual(self.ll.head.next_node.data, 2)

    def test_remove_node_position(self):
        """Проверяет удаление узла по позиции."""
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(2)
        self.assertEqual(self.ll.remove_node_position(1), "Удален узел с данными 1 позиции 1")
        self.assertEqual(self.ll.head.data, 2)

    def test_insert_at_position(self):
        """Проверяет вставку узла по позиции."""
        self.ll.insert_at_end(1)
        self.ll.insert_at_end(3)
        self.ll.insert_at_position(2, 2)
        self.assertEqual(self.ll.head.next_node.data, 2)

    def test_change_data(self):
        """Проверяет изменение данных узла."""
        self.ll.insert_at_end(1)
        self.assertEqual(self.ll.change_data(1, 2), "Заменены данные в узле № 1")
        self.assertEqual(self.ll.head.data, 2)

    def test_get(self):
        """Проверяет поиск узла по данным."""
        self.ll.insert_at_end(1)
        found, node = self.ll.get(1)
        self.assertTrue(found)
        self.assertEqual(node.data, 1)

if __name__ == '__main__':
    unittest.main()
