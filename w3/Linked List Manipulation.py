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
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_first(self, key):
        if not self.contains(key):
            new_node = Node(key)
            new_node.next = self.head
            self.head = new_node

    def add_last(self, key):
        if not self.contains(key):
            new_node = Node(key)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node

    def add_after(self, u, v):
        if not self.contains(u) and self.contains(v):
            new_node = Node(u)
            current = self.head
            while current:
                if current.key == v:
                    new_node.next = current.next
                    current.next = new_node
                    break
                current = current.next

    def add_before(self, u, v):
        if not self.contains(u) and self.contains(v):
            new_node = Node(u)
            if self.head.key == v:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    if current.next.key == v:
                        new_node.next = current.next
                        current.next = new_node
                        break
                    current = current.next

    def remove(self, key):
        if self.head and self.head.key == key:
            self.head = self.head.next
        else:
            current = self.head
            while current and current.next:
                if current.next.key == key:
                    current.next = current.next.next
                    break
                current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def contains(self, key):
        current = self.head
        while current:
            if current.key == key:
                return True
            current = current.next
        return False

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.key)
            current = current.next
        return result

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n = int(data[0])
    initial_keys = list(map(int, data[1].split()))

    linked_list = LinkedList()
    for key in initial_keys:
        linked_list.add_last(key)

    for line in data[2:]:
        if line == "#":
            break
        parts = line.split()
        command = parts[0]
        if command == "addfirst":
            linked_list.add_first(int(parts[1]))
        elif command == "addlast":
            linked_list.add_last(int(parts[1]))
        elif command == "addafter":
            linked_list.add_after(int(parts[1]), int(parts[2]))
        elif command == "addbefore":
            linked_list.add_before(int(parts[1]), int(parts[2]))
        elif command == "remove":
            linked_list.remove(int(parts[1]))
        elif command == "reverse":
            linked_list.reverse()

    print(" ".join(map(str, linked_list.to_list())))

if __name__ == "__main__":
    main()

