# There are two jugs, a-litres jug and b-litres jug (a, b are positive integers). There is a pump with unlimited water. Given a positive integer c, how to get exactly c litres.
# Input
#    Line 1: contains positive integers a,   b,  c  (1 <= a, b, c <= 900)
# Output
#   write the number of steps or write -1 (if no solution found)
# Example
#
# Input
# 6  8  4
# Output
# 4
from collections import deque

def water_jug_solver(a, b, c):
    if c > a + b:
        return -1
    if c % gcd(a, b) != 0:
        return -1

    visited = set()
    queue = deque([(0, 0, 0)])  # (jug1, jug2, steps)

    while queue:
        jug1, jug2, steps = queue.popleft()

        if jug1 == c or jug2 == c or jug1 + jug2 == c:
            return steps

        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))

        # Fill jug1
        queue.append((a, jug2, steps + 1))
        # Fill jug2
        queue.append((jug1, b, steps + 1))
        # Empty jug1
        queue.append((0, jug2, steps + 1))
        # Empty jug2
        queue.append((jug1, 0, steps + 1))
        # Pour jug1 to jug2
        pour_to_jug2 = min(jug1, b - jug2)
        queue.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2, steps + 1))
        # Pour jug2 to jug1
        pour_to_jug1 = min(jug2, a - jug1)
        queue.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1, steps + 1))

    return -1
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
a, b, c = map(int, input().split())
print(water_jug_solver(a, b, c))
