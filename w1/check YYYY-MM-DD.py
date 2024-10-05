# Given a date which is a string under the format YYYY-MM-DD (in which YYYY is the year, MM is the month (the month í from 1 to 12), and DD is the date (the date is from 1 to 31)). Extract the year, month and date.
# Input
# Line 1: contains a string s
# Output
# if s is not under the format YYYY-MM-DD, then write INCORRECT. Otherwise, write year, month, and date separated by a SPACE character
#
# Example
# Input
# 2023-10-04
# Output
# 2023 10 4
#
#
# Input
# 2023-10-4
# Output
# INCORRECT
#
# Input
# 2023-10 04
# Output
# INCORRECT
S= input().split("-")
if len(S) != 3 or len(S[1]) != 2 or len(S[2]) != 2 or not S[1].isnumeric() or not S[2].isnumeric() or int(S[1]) > 12 or int(S[1]) < 1 or int(S[2]) > 31 or int(S[2]) < 1:
    print("INCORRECT")
else:print(S[0],int(S[1]),int(S[2]))