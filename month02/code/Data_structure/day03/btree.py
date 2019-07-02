"""
    二叉树
    先序遍历、中序遍历、后序遍历
"""
from squeue import SQueue

class Node:
    def __init__(self, item=None, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


class BTree:
    def __init__(self, root):
        self.root = root

    # def add(self, item):
    #     node = Node(item)
    #     if self.root is None:
    #         self.root = node
    #     else:
    #         queue = []
    #         queue.append(self.root)
    #         # 对已有的节点进行遍历
    #         while queue:
    #             cur = queue.pop(0)
    #             if cur.lchild is None:
    #                 cur.lchild = node
    #                 return
    #             elif cur.rchild is None:
    #                 cur.rchild = node
    #                 return
    #             else:
    #                 # 如果左右子树都不为空，加入队列继续判断
    #                 queue.append(cur.lchild)
    #                 queue.append(cur.rchild)

    # 先序遍历
    def preorder(self, root):
        if root is None:
            return
        print(root.item)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    # 中序遍历
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.lchild)
        print(root.item)
        self.inorder(root.rchild)

    # 后序遍历
    def postorder(self, root):
        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.item)

    # 层次遍历
    def levelorder(self, node):
        """
            使用队列操作，初始节点进入队列，先进先出，打印出队元素，
            再让其左右孩子入队，知道队列为空
        :param node:
        :return:
        """
        sq = SQueue()
        sq.enqueue(node)
        while not sq.is_empty():
            node = sq.dequeue()
            print(node.item)
            if node.lchild:
                sq.enqueue(node.lchild)
            if node.rchild:
                sq.enqueue(node.rchild)


if __name__ == "__main__":
    # 按后序遍历顺序传入节点
    b = Node('b')
    f = Node('f')
    g = Node('g')
    d = Node('d', f, g)
    i = Node('i')
    h = Node('h')
    e = Node('e', i, h)
    c = Node('c', d, e)
    a = Node('a', b, c)
    btree = BTree(a)
    # btree.preorder(btree.root)
    # btree.inorder(btree.root)
    # btree.postorder(btree.root)
    btree.levelorder(btree.root)
