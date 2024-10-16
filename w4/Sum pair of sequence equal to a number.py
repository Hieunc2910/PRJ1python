# Cho dãy a1, a2, ..., an trong đó các phần tử đôi một khác nhau và 1 giá trị nguyên dương M. Hãy đếm số Q các cặp (i,j) sao cho 1 <= i < j <= n và ai + aj = M.
# Dữ liệu
# Dòng 1: ghi n và M (1 <= n, M <= 1000000)
# Dòng 2: ghi a1, a2, ..., an
# Kết quả
# Ghi ra giá trị Q
# Ví dụ
# Dữ liệu
# 5 6
# 5 2 1 4 3
# Kết quả
# 2
n,M = map(int, input().split())
a = list(map(int, input().split()))
b = {}
Q = 0
for i in range(n):
    if M - a[i] in b:
        Q += b[M - a[i]]
    if a[i] in b:
        b[a[i]] += 1
    else:
        b[a[i]] = 1
print(Q)