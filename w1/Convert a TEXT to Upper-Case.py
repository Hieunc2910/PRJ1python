
# Given a TEXT, write a program that converts the TEXT to upper-case.
#
# Input
# The TEXT
#
# Output
# The TEXT in which characters are converted into upper-case
#
# Example
# Input
# Hello John,
# How are you?
#
# Bye,
#
# Output
# HELLO JOHN,
# HOW ARE YOU?
#
# BYE,

import sys
input_text = sys.stdin.read()
print(input_text.upper())
