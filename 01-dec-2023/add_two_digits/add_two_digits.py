# You are given a two-digit integer n. Return the sum of its digits.
# Example
# For n = 29, the output should be
# addTwoDigits(n) = 11.
# Input/Output

def solution(n):
  return sum([int(i) for i in str(n)])    

