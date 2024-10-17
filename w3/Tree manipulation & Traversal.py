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
class Node:
    def __init__(self, id):
        self.id = id
        self.children = []

    def insert(self, u, v):
        if self.id == v:
            for child in self.children:
                if child.id == u:
                    return False
            self.children.append(Node(u))
            return True
        for child in self.children:
            if child.insert(u, v):
                return True
        return False

    def pre_order(self):
        result = [self.id]
        for child in self.children:
            result.extend(child.pre_order())
        return result

    def in_order(self):
        result = []
        if self.children:
            result.extend(self.children[0].in_order())
        result.append(self.id)
        for child in self.children[1:]:
            result.extend(child.in_order())
        return result

    def post_order(self):
        result = []
        for child in self.children:
            result.extend(child.post_order())
        result.append(self.id)
        return result

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    root = None
    for line in data:
        if line == "*":
            break
        parts = line.split()
        command = parts[0]
        if command == "MakeRoot":
            u = int(parts[1])
            root = Node(u)
        elif command == "Insert":
            u = int(parts[1])
            v = int(parts[2])
            if root:
                root.insert(u, v)
        elif command == "PreOrder":
            if root:
                print(" ".join(map(str, root.pre_order())))
        elif command == "InOrder":
            if root:
                print(" ".join(map(str, root.in_order())))
        elif command == "PostOrder":
            if root:
                print(" ".join(map(str, root.post_order())))

if __name__ == "__main__":
    main()