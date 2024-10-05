# Given a time moment which is a string under the format hh:mm:ss (in which hh (0 <= hh <= 23) is the hour, mm (0 <= mm <= 59) is the minute, and ss (0 <= ss <= 59) is the second). Convert this time moment in seconds (result = hh*3600 + mm*60 + ss).
# Input
# Line 1: contains a string s representing the time moment.
# Output
# if s is not under the format hh:mm:ss, then write INCORRECT. Otherwise, write value converted.
#
# Example
# Input
# 13:05:26
#
# Output
# 47126
#
#
# Input
# 13:05:6
#
# Output
# INCORRECT
#
# Input
# 13:05 26
#
# Output
# INCORRECT
T = input().split(':')
if len(T) != 3 or len(T[0]) != 2 or len(T[1]) != 2 or len(T[2]) != 2 or not T[0].isnumeric() or not T[1].isnumeric() or not T[2].isnumeric() or int(T[0]) > 23 or int(T[0]) < 0 or int(T[1]) > 59 or int(T[1]) < 0 or int(T[2]) > 59 or int(T[2]) < 0:
    print("INCORRECT")
else: print(int(T[0])*3600+int(T[1])*60+int(T[2]))
