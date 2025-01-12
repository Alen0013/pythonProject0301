class Node:
    """
    Класс для представления узла в связанном списке.
    """

    def __init__(self, data, next_node=None):
        """
        Инициализация узла.

        :param data: Данные, которые должен хранить узел.
        :param next_node: Ссылка на следующий узел (по умолчанию None).
        """
        self.data = data
        self.next_node = next_node


class LinkedList:
    """
    Класс для представления связного списка.
    """

    def __init__(self):
        """Инициализация пустого связного списка."""
        self.head = None

    def insert_at_head(self, data):
        """
        Вставляет узел с данными в начало списка.

        :param data: Данные для вставки.
        :return: Сообщение об успешной вставке.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
        return f"Узел с данными {new_node.data} добавлен в начало списка"

    def insert_at_end(self, data):
        """
        Вставляет узел с данными в конец списка.

        :param data: Данные для вставки.
        :return: Сообщение об успешной вставке.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next_node:
            current_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен в конец списка"

    def remove_node_position(self, rm_position):
        """
        Удаляет узел на заданной позиции.

        :param rm_position: Позиция узла для удаления.
        :return: Сообщение об успешном удалении или предупреждение.
        """
        if rm_position == 1:
            removed_node = self.head
            self.head = self.head.next_node
            return f"Удален узел с данными {removed_node.data} позиции {rm_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < rm_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None or current_node.next_node is None:
            return "Ничего не удалено"
        removed_node = current_node.next_node
        current_node.next_node = current_node.next_node.next_node
        return f"Удален узел с данными {removed_node.data} позиции {rm_position}"

    def insert_at_position(self, data, node_position):
        """
        Вставляет узел с данными на заданную позицию.

        :param data: Данные для вставки.
        :param node_position: Позиция для вставки.
        :return: Сообщение об успешной вставке.
        """
        new_node = Node(data)
        if node_position == 1:
            self.insert_at_head(data)
            return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"
        current_node = self.head
        current_node_position = 1
        while current_node is not None and current_node_position < node_position - 1:
            current_node = current_node.next_node
            current_node_position += 1
        if current_node is None:
            return None
        new_node.next_node = current_node.next_node
        current_node.next_node = new_node
        return f"Узел с данными {new_node.data} добавлен на позицию {node_position}"

    def print_ll(self):
        """Выводит данные списка на экран."""
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next_node
        return "Данные списка выведены"

    def get(self, data):
        """
        Проверяет, существует ли узел с заданными данными.

        :param data: Данные для проверки.
        :return: Кортеж с результатом проверки и узлом.
        """
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return True, current_node
            current_node = current_node.next_node
        return False, None

    def change_data(self, node_data, change_data):
        """
        Изменяет данные узла с указанными данными.

        :param node_data: Данные узла, который нужно изменить.
        :param change_data: Новые данные.
        :return: Сообщение об успешном изменении или предупреждение.
        """
        current_node = self.head
        current_node_position = 1
        while current_node:
            if current_node.data == node_data:
                current_node.data = change_data
                return f"Заменены данные в узле № {current_node_position}"
            current_node = current_node.next_node
            current_node_position += 1
        return "Данные не обнаружены"
