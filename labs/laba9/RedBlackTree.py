"""Красно-чёрное дерево"""


class Node:
    def __init__(self, item):
        self.item = item
        self.color = "red"
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = "black"
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def insert(self, item):
        insert_node = Node(item)
        insert_node.left = self.TNULL
        insert_node.right = self.TNULL

        previous_node = None
        current_node = self.root

        self.print()
        # ищем узел для вставки
        while current_node != self.TNULL:
            previous_node = current_node
            if insert_node.item < current_node.item:
                current_node = current_node.left
            else:
                current_node = current_node.right

        # корневой узел
        insert_node.parent = previous_node

        # условие для первой вставки - корневой узел
        if previous_node is None:
            self.root = insert_node
        # вставка это левый или правый дочерний узел
        elif insert_node.item < previous_node.item:
            previous_node.left = insert_node
        else:
            previous_node.right = insert_node

        # изменение цвета корневого узла при первой вставке
        if insert_node.parent is None:
            insert_node.color = "black"
            return

        # условие отсутствия необходимости балансировки
        if insert_node.parent.parent is None:
            return

        self.__fix_insert(insert_node)

    # Операция балансировки
    def __fix_insert(self, insert_node):
        # пока родитель нового узла красный
        while insert_node.parent.color == 'red':

            # если родитель является правым ребёнком
            if insert_node.parent == insert_node.parent.parent.right:
                uncle_node = insert_node.parent.parent.left
                # если дядя красный
                if uncle_node.color == 'red':
                    uncle_node.color = 'black'
                    insert_node.parent.color = 'black'
                    insert_node.parent.parent.color = 'red'
                    # фиксация на уровне деда
                    insert_node = insert_node.parent.parent
                # если дядя черный
                else:
                    # если ребёнок является левым
                    if insert_node == insert_node.parent.left:
                        insert_node = insert_node.parent
                        # правое вращение вокруг родителя
                        self.__rotate_right(insert_node)
                    insert_node.parent.color = 'black'
                    insert_node.parent.parent.color = 'red'
                    # левое вращение вокруг деда
                    self.__rotate_left(insert_node.parent.parent)

            # если родитель является левым ребёнком
            else:
                uncle_node = insert_node.parent.parent.right
                # если дядя красный
                if uncle_node.color == 'red':
                    uncle_node.color = 'black'
                    insert_node.parent.color = 'black'
                    insert_node.parent.parent.color = 'red'
                    # фиксация на уровне деда
                    insert_node = insert_node.parent.parent
                else:
                    # если ребёнок является правым
                    if insert_node == insert_node.parent.right:
                        insert_node = insert_node.parent
                        # левое вращение вокруг родителя
                        self.__rotate_left(insert_node)
                    insert_node.parent.color = 'black'
                    insert_node.parent.parent.color = 'red'
                    # правое вращение вокруг деда
                    self.__rotate_right(insert_node.parent.parent)

            # условие для первой вставки
            if insert_node == self.root:
                break
        # корень всегда должен быть черным
        self.root.color = 'black'

    def __rotate_left(self, node):
        # установка как правого ребёнка
        swap_node = node.right
        # перемещение левого ребёнка
        node.right = swap_node.left
        # обновление родительской ссылки у левого ребёнка
        if swap_node.left != self.TNULL:
            swap_node.left.parent = node
        # обновление родительской ссылки
        swap_node.parent = node.parent
        # условие на установку коря
        if node.parent is None:
            self.root = swap_node
        # если node был левым ребёнком, то swap_node становится левым
        elif node == node.parent.left:
            node.parent.left = swap_node
        # если node был правым ребёнком, то swap_node становится правым
        else:
            node.parent.right = swap_node
        # node становится левым ребёнком swap_node
        swap_node.left = node
        # swap_node становится родителем node
        node.parent = swap_node

    def __rotate_right(self, node):
        # установка как левого ребёнка
        swap_node = node.left
        # перемещение правого ребёнка
        node.left = swap_node.right
        # обновление родительской ссылки у левого ребёнка
        if swap_node.right != self.TNULL:
            swap_node.right.parent = node
        # обновление родительской ссылки
        swap_node.parent = node.parent
        # условие на установку корня
        if node.parent is None:  # Если node был корнем
            self.root = self
        # если node был правым ребёнком, то swap_node становится правым
        elif node == node.parent.right:
            node.parent.right = swap_node
        # если node был левым ребёнком, то swap_node становится левым
        else:
            node.parent.left = swap_node
        # node становится правым ребёнком swap_node
        swap_node.right = node
        # swap_node становится родителем node
        node.parent = swap_node

    def print(self):
        self.__print_helper(self.root)
        print()

    def __print_helper(self, node):
        if node != self.TNULL:
            self.__print_helper(node.left)
            print(node.item, end=' ')
            self.__print_helper(node.right)


def main():
    tree = RedBlackTree()
    nums = [4, 6, 9, 48, 12, 7, 5, 10, 13, 2, 1]

    for num in nums:
        tree.insert(num)
    tree.print()


if __name__ == "__main__":
    main()
