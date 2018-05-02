""" Calculator code with import feature from other class """

import calculator
nlist=input("Enter numbers to get their sum")
nlist=[int(x) for x in nlist.split(',')]
calculator.add(nlist)
r1=calculator.add(nlist)
print("Sum is:",r1)
n1=input("Enter first number")
n2=input("Enter second number")
calculator.sub(n1,n2)
r2=calculator.sub(n1,n2)
print("Difference is:",r2)
calculator.mul(n1,n2)
r3=calculator.mul(n1,n2)
print("Product is:",r3)
calculator.div(n1,n2)
r4=calculator.div(n1,n2)
print("Quotient is:",r4)