# Given a Text, write a prorgam to count the number Q of words (ignore characters SPACE, TAB, LineBreak) of this Text
#
# Input
# The Text
#
# Output
# Write the number Q of words
#
# Example
# Input
# Hanoi University Of Science and Technology
# School of Information and Communication Technology
import sys
input_text = sys.stdin.read()
words = input_text.split()
count = len(words)
print(count)