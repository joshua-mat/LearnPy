# Given two integer numbers, write a Python program to return their product only if
#the product is equal to or lower than 1000. Otherwise, return their sum.
#Given : Number 1 = 60
#        Number 2 = 30

x = 40
y = 30
p = x * y
s = x +y
if p <= 1000 :
    print(p)
else :
    print(s)