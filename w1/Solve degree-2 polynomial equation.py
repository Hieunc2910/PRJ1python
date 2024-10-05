# Given an equation ax^2 + bx + c = 0. Find solution to the given equation.
# Input
# Line 1 contains 3 integers a, b, c
# Output
# Write NO SOLUTION if the given equation has no solution
# Write x0 (2 digits after the decimal point) if the given equation has one solution x0
# Write x1 and x2 with x1 < x2 (2 digits after the decimal point) if the given equation has two distinct solutions x1, x2
#
# Example
# Input
# 1 1 8
# Output
# NO SOLUTION

# Input
# 1 -2 1
# Output
# 1.00
#
# Input
# 1 -7 10
# Output
# 2.00 5.00
a,b,c = map(int,input().split())
if a==0:
    if b==0:
        if c==0:
            print("NO SOLUTION")
        else:
            print("NO SOLUTION")
    else:
        print("{:.2f}".format(-c/b))
check = b*b - 4*a*c
if check<0:
    print("NO SOLUTION")
elif check == 0:
    print("{:.2f}".format(-b/(2*a)))
else: print("{:.2f} {:.2f}".format((-b-check**0.5)/(2*a),(-b+check**0.5)/(2*a)))
