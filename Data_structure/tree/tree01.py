"""
    tree.py
"""


# class Node:
#     def __init__(self, elem=-1, lchild=None, rchild=None):
#         self.elem = elem
#         self.lchild = lchild
#         self.rchild = rchild
#
#
# class Tree:
#     def __init__(self, root=None):
#         self.root = root
#
#     def add(self, elem):
#         node = Node(elem)
#         if self.root is None:
#             self.root = node
#         else:
#             queue = []
#             queue.append(self.root)
#             # 对已有的节点进行遍历
#             while queue:
#                 cur = queue.pop(0)
#                 if cur.lchild is None:
#                     cur.lchild = node
#                     return
#                 elif cur.rchild is None:
#                     cur.rchild = node
#                     return
#                 else:
#                     # 如果左右子树都不为空，加入队列继续判断
#                     queue.append(cur.lchild)
#                     queue.append(cur.rchild)
#
#     # 树的先序遍历
#     def preorder(self, root):
#         if root is None:
#             return
#         print(root.item)
#         self.preorder(root.lchild)
#         self.preorder(root.rchild)
#
#     # 树的中序遍历
#     def inorder(self, root):
#         if root is None:
#             return
#         self.inorder(root.lchild)
#         print(root.elem)
#         self.inorder(root.rchild)



