#Alternitavely you can import math and use the factorial method ---> math.factorial(x)
#This is my recursive implementation of factorials though

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)
