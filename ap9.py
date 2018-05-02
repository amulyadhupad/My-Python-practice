""" This code is to get user input with specified number of attempts """

for i in range(1,4):
	un=input("Enter number between 1 to 10")
	if int(un)>1 and int(un)<10:
		print(un)
		break
	else:
		if 3-i != 0:
			print("Left with"+ " "+str(3-i)+" "+"chance")
		else:
			print("Sorry! you ran out of chances")