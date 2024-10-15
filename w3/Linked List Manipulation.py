# Viết chương trình thực hiện công việc sau:
# Xây dựng danh sách liên kết với các khóa được cung cấp ban đầu là dãy a
# 1
# , a
# 2
# , …, a
# n
# , sau đó thực hiện các thao tác trên danh sách bao gồm: thêm 1 phần tử vào đầu, vào cuối danh sách, hoặc vào trước, vào sau 1 phần tử nào đó trong danh sách, hoặc loại bỏ 1 phần tử nào đó trong danh sách
#
# Input
# Dòng 1: ghi số nguyên dương n (1 <= n <= 1000)
# Dòng 2: ghi các số nguyên dương a1, a2, …, an.
# Các dòng tiếp theo lần lượt là các lệnh để thao tác (kết thúc bởi ký hiệu #) với các loại sau:
# addlast  k: thêm phần tử có key bằng k vào cuối danh sách (nếu k chưa tồn tại)
# addfirst  k: thêm phần tử có key bằng k vào đầu danh sách (nếu k chưa tồn tại)
# addafter  u  v: thêm phần tử có key bằng u vào sau phần tử có key bằng v trên danh sách (nếu v đã tồn tại trên danh sách và u chưa tồn tại)
# addbefore  u  v: thêm phần tử có key bằng  u vào trước phần tử có key bằng v trên danh sách (nếu v đã tồn tại trên danh sách và u của tồn tại)
# remove  k: loại bỏ phần tử có key bằng k khỏi danh sách
# reverse: đảo ngược thứ tự các phần tử của danh sách (không được cấp phát mới các phần tử, chỉ được thay đổi mối nối liên kết)
# Output
# Ghi ra dãy khóa của danh sách thu được sau 1 chuỗi các lệnh thao tác đã cho
import sys
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.prev = None
class LinkedList:
    def __init__(self):
        self.head = None
        self.next = None
    def addLast(self,key):
        if self.head == None:
            self.head = Node(key)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(key)
            cur.next.prev = cur
    def addFirst(self,key):
        if self.head == None:
            self.head = Node(key)
        else:
            cur = self.head
            self.head = Node(key)
            self.head.next = cur
            cur.prev = self.head
    def addAfter(self,u,v):
        cur = self.head
        while cur != None:
            if cur.key == v:
                temp = cur.next
                cur.next = Node(u)
                cur.next.next = temp
                cur.next.prev = cur
                if temp != None:
                    temp.prev = cur.next
                break
            cur = cur.next
    def addBefore(self,u,v):
        cur = self.head
        while cur != None:
            if cur.key == v:
                temp = cur.prev
                cur.prev = Node(u)
                cur.prev.prev = temp
                cur.prev.next = cur
                if temp != None:
                    temp.next = cur.prev
                break
            cur = cur.next
    def remove(self,k):
        cur = self.head
        while cur != None:
            if cur.key == k:
                if cur.prev != None:
                    cur.prev.next = cur.next
                else:
                    self.head = cur.next
                if cur.next != None:
                    cur.next.prev = cur.prev
                break
            cur = cur.next
    def reverse(self):
        cur = self.head
        while cur != None:
            temp = cur.next
            cur.next = cur.prev
            cur.prev = temp
            if temp == None:
                self.head = cur
            cur = temp

input_text = sys.stdin.read().splitlines()
a = list(map(int,input_text[1].split()))
ll = LinkedList()
for i in a:
    ll.addLast(i)
for i in input_text[2:]:
    if i.startswith('addlast'):
        _,k = i.split()
        ll.addLast(int(k))
    elif i.startswith('addfirst'):
        _,k = i.split()
        ll.addFirst(int(k))
    elif i.startswith('addafter'):
        _,u,v = i.split()
        ll.addAfter(int(u),int(v))
    elif i.startswith('addbefore'):
        _,u,v = i.split()
        ll.addBefore(int(u),int(v))
    elif i.startswith('remove'):
        _,k = i.split()
        ll.remove(int(k))
    elif i == 'reverse':
        ll.reverse()
cur = ll.head
while cur != None:
    print(cur.key,end=" ")
    cur = cur.next

