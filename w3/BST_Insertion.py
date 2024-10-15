# Given a BST initialized by NULL. Perform a sequence of operations on a BST including:
# insert k: insert a key k into the BST (do not insert if the key k exists)
# Input
# •Each line contains command under the form: “insert k”
# •The input is terminated by a line containing #
# Output
# •Write the sequence of keys of nodes visited by the pre-order traversal (separated by a SPACE character)
# Example
# Input
# insert 20
# insert 10
# insert 26
# insert 7
# insert 15
# insert 23
# insert 30
# insert 3
# insert 8
# #
# Output
# 20 10 7 3 8 15 26 23 30

import sys
a = sys.stdin.read().splitlines()
a = a[:a.index("#")]
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.key == key:
            return root
        elif root.key < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
def preOrder(root):
    if root:
        print(root.key, end=" ")
        preOrder(root.left)
        preOrder(root.right)
root = None
for i in a:
    _, k = i.split()
    root = insert(root, int(k))
preOrder(root)



