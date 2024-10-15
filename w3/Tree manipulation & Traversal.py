# Mỗi nút trên cây có trường id (identifier) là một số nguyên (id của các nút trên cây đôi một khác nhau)
# Thực hiện 1 chuỗi các hành động sau đây bao gồm các thao tác liên quan đến xây dựng cây và duyệt cây
# · MakeRoot u: Tạo ra nút gốc u của cây
# · Insert u v: tạo mới 1 nút u và chèn vào cuối danh sách nút con của nút v (nếu nút có id bằng v không tồn tại hoặc nút có id bằng u đã tồn tại thì không chèn thêm mới)
# · PreOrder: in ra thứ tự các nút trong phép duyệt cây theo thứ tự trước
# · InOrder: in ra thứ tự các nút trong phép duyệt cây theo thứ tự giữa
# · PostOrder: in ra thứ tự các nút trong phép duyệt cây theo thứ tự sau
# Dữ liệu: bao gồm các dòng, mỗi dòng là 1 trong số các hành động được mô tả ở trên, dòng cuối dùng là * (đánh dấu sự kết thúc của dữ liệu).
# Kết quả: ghi ra trên mỗi dòng, thứ tự các nút được thăm trong phép duyệt theo thứ tự trước, giữa, sau của các hành động PreOrder, InOrder, PostOrder tương ứng đọc được từ dữ liệu đầu vào
# Ví dụ
# Dữ liệu
# MakeRoot 10
# Insert 11 10
# Insert 1 10
# Insert 3 10
# InOrder
# Insert 5 11
# Insert 4 11
# Insert 8 3
# PreOrder
# Insert 2 3
# Insert 7 3
# Insert 6 4
# Insert 9 4
# InOrder
# PostOrder
# *
# Kết quả
# 11 10 1 3
# 10 11 5 4 1 3 8
# 5 11 6 4 9 10 1 8 3 2 7
# 5 6 9 4 11 1 8 2 7 3 10
import sys
class Node:
    def __init__(self):
        self.id = None
        self.left = None
        self.right = None
    def MakeRoot (self,u):
        self.id=u
    def Insert(self, u, v):
        if self.id == v:
            if self.left == None:
                self.left = Node()
                self.left.MakeRoot(u)
            elif self.right == None:
                self.right = Node()
                self.right.MakeRoot(u)
        else:
            if self.left != None:
                self.left.Insert(u,v)
            if self.right != None:
                self.right.Insert(u,v)
    def PreOrder(self):
        print(self.id, end=" ")
        if self.left != None:
            self.left.PreOrder()
        if self.right != None:
            self.right.PreOrder()
    def InOrder(self):
        if self.left != None:
            self.left.InOrder()
        print(self.id, end=" ")
        if self.right != None:
            self.right.InOrder()
    def PostOrder(self):
        if self.left != None:
            self.left.PostOrder()
        if self.right != None:
            self.right.PostOrder()
        print(self.id, end=" ")
root = Node()
input_text = sys.stdin.read().splitlines()
for i in input_text:
    if i == "*":
        break
    if i.startswith("MakeRoot"):
        _, u = i.split()
        root.MakeRoot(int(u))
    elif i.startswith("Insert"):
        _, u, v = i.split()
        root.Insert(int(u), int(v))
    elif i == "PreOrder":
        root.PreOrder()
        print()
    elif i == "InOrder":
        root.InOrder()
        print()
    elif i == "PostOrder":
        root.PostOrder()
        print()