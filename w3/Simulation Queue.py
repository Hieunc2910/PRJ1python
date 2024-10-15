# Perform a sequence of operations over a queue, each element is an integer:
# PUSH v: push a value v into the queue
# POP: remove an element out of the queue and print this element to stdout (print NULL if the queue is empty)
# Input
# Each line contains a command (operration) of type
# PUSH  v
# POP
# Output
# Write the results of POP operations (each result is written in a line)
# Example
# Input
# PUSH 1
# PUSH 2
# PUSH 3
# POP
# POP
# PUSH 4
# PUSH 5
# POP
# #
# Output
# 1
# 2
# 3
#
# Input
# PUSH 1
# POP
# POP
# PUSH 4
# POP
# #
# Output
# 1
# NULL
# 4
import sys
a = sys.stdin.read().splitlines()
a = a[:a.index("#")]
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def push(self, key):
        if self.head == None:
            self.head = Node(key)
            self.tail = self.head
        else:
            self.tail.next = Node(key)
            self.tail = self.tail.next
    def pop(self):
        if self.head == None:
            print("NULL")
        else:
            print(self.head.key)
            self.head = self.head.next
q = Queue()
for i in a:
    if i[:4] == "PUSH":
        _, k = i.split()
        q.push(int(k))
    else:
        q.pop()
