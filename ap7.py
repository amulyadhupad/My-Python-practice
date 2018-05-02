""" This code is to enter flowers list and sort the same and print it """

flowerlist =[]
print("Enter 5 flower names")
for i in range(5):
	flowerlist.append(input())
flowerlist.sort()
print(flowerlist)