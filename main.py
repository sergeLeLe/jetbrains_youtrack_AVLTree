class Node:
    def __init__(self, key):
        self.key = key
        self.left = None  # AVLTree
        self.right = None  # AVLTree

    def __str__(self):
        return str(self.key)


class AVL_Tree:
    def __init__(self):
        self.node = None  # root
        self.height = -1
        self.balance = 0

    def display(self, node=None, level=0):

        if not self.node:
            return

        if not node:
            node = self.node
        if node.right.node:
            self.display(node.right.node, level + 1)
            print(('\t' * level), ('    /'))
        print(('\t' * level), node)
        if node.left.node:
            print(('\t' * level), ('    \\'))
            self.display(node.left.node, level + 1)

    def search(self, key):

        tree = self.node
        while tree != None and key != tree.key:
            if key < tree.key:
                tree = tree.left.node
            else:
                tree = tree.right.node
        return tree

    def min_node(self):

        if not self.node:
            return

        tree = self.node
        while tree.left.node != None:
            tree = tree.left.node
        return tree

    def max_node(self):

        if not self.node:
            return

        tree = self.node
        while tree.right.node != None:
            tree = tree.right.node
        return tree

    def insert(self, key, balance=True):

        if self.node == None:
            self.node = Node(key)
            self.node.left = AVL_Tree()
            self.node.right = AVL_Tree()
        elif key < self.node.key:
            self.node.left.insert(key)
        elif key > self.node.key:
            self.node.right.insert(key)
        else:
            print("Key [" + str(key) + "] already in tree.")

        if balance:
            self.rebalance()

    def rebalance(self):

        self.update_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.rotate_l()
                    self.update_heights()
                    self.update_balances()
                self.rotate_r()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rotate_r()
                    self.update_heights()
                    self.update_balances()
                self.rotate_l()
                self.update_heights()
                self.update_balances()

    def rotate_r(self):

        old_root = self.node
        new_root = self.node.left.node
        new_left_sub = new_root.right.node

        self.node = new_root
        old_root.left.node = new_left_sub
        new_root.right.node = old_root

    def rotate_l(self):

        old_root = self.node
        new_root = self.node.right.node
        new_left_sub = new_root.left.node

        self.node = new_root
        old_root.right.node = new_left_sub
        new_root.left.node = old_root

    def update_heights(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height,
                              self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node == None:
            if recurse:
                if self.node.left != None:
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def postOrderTraversal(self):
        traversal = []

        if not self.node:
            return traversal

        traversal.extend(self.node.left.postOrderTraversal())
        traversal.extend(self.node.right.postOrderTraversal())
        traversal.append(self.node.key)

        return traversal

    def get_height(self):
        if self.node:
            return self.height + 1
        else:
            return 0


def test_AVLTree():
    arrs = [[5, 1, 2, 3], [10, 14, 13, 4, 3, 6, 5, 7, 4], [], [1], [5, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]]
    for arr in arrs:
        tree = AVL_Tree()
        for i in arr:
            tree.insert(i)
        tree.display()

        print('Height: {}'.format(tree.get_height()))
        print('Search node with key {}. Result - Key or None: {}'.format(2, tree.search(2)))
        print('Search node with key {}. Result - Key or None: {}'.format(15, tree.search(15)))
        print('Node with min key. Result - Key: {}'.format(tree.min_node()))
        print('Node with max key. Result - Key: {}'.format(tree.max_node()))
        print('PostOrder Traversal: {}'.format(tree.postOrderTraversal()) + '\n')
        print('----------------------------------------------------------------')
        print('----------------------------------------------------------------')


def test_tree_without_balance():
    arrs = [[5, 1, 2, 3], [10, 14, 13, 4, 3, 6, 5, 7, 4], [], [1], [5, 2], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]]
    for arr in arrs:
        tree = AVL_Tree()
        for i in arr:
            tree.insert(i, False)
        tree.display()

        print('Height: {}'.format(tree.get_height()))
        print('Search node with key {}. Result - Key or None: {}'.format(2, tree.search(2)))
        print('Search node with key {}. Result - Key or None: {}'.format(15, tree.search(15)))
        print('Node with min key. Result - Key: {}'.format(tree.min_node()))
        print('Node with max key. Result - Key: {}'.format(tree.max_node()))
        print('PostOrder Traversal: {}'.format(tree.postOrderTraversal()) + '\n')
        print('----------------------------------------------------------------')
        print('----------------------------------------------------------------')

