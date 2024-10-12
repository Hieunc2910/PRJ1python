# Given a string containing only characters (, ), [, ] {, }. Write a program that checks whether the string is correct in expression.
# Example
#  ([]{()}()[]): correct
#  ([]{()]()[]): incorrect
# Input
# One line contains the string (the length of the string is less than or equal to $10^6$)One line contains the string (the length of the string is less than or equal to 10
# 6
# )
# Output
# Write 1 if the sequence is correct, and write 0, otherwise
# Example
# Input
# (()[][]{}){}{}[][]({[]()})
# Output
a = input().strip()
b = []
matching_bracket = {')': '(', ']': '[', '}': '{'}

for i in a:
    if i in '({[':
        b.append(i)
    elif i in matching_bracket:
        if not b or b[-1] != matching_bracket[i]:
            print(0)
            break
        b.pop()
else:
    print(1 if not b else 0)