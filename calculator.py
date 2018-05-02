""" Calculator code with import feature from this file """

def add(nlist):
	sum1=0
	for i in nlist:
		sum1 = sum1+i
	return sum1

def sub(n1,n2):
	difference = int(n1)-int(n2)
	return difference

def mul(n1,n2):
	product = int(n1)*int(n2)
	return product

def div(n1,n2):
	if n1 > n2:
		quotient = int(n1)/int(n2)
		return quotient
	else:
		print("Enter n1 > n2")
	
