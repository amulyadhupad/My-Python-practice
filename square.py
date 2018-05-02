""" Code to print square of the given number"""

def square(num):
	res =int(num) * int(num)
	return res
num=input("Enter a number")
ans=square(num)
print("square of "+str(num)+" "+"is:"+str(ans))