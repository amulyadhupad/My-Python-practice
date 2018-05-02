""" Code to print the total score of the student """

name=input("Enter the name of the student")
score_list=input("Enter scores of the student")
score_list=[int(x)for x in score_list.split(',')]
def total_score(name,score_list):
	total=0
	for i in score_list:
		total += i
	print("Hi " +str(name) + ","+" your total score is ",total)

total_score(name,score_list)