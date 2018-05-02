""" Code to find given age, salarya and phone number in the names.txt file (pre-requisite) and then write it in new file if the match is found"""

import sys
import re
f=open('names.txt','r')
flag=False
for line in f.readlines():
	if re.search("^"+sys.argv[1]+"$",line):
		line=line.replace('\n','')
		age =input("Enter the age")
		while(age.isdigit()==False):
			age=input("Enter age in digits")
		salary =input("Enter the salary")
		#print("salary = "+salary.isdigit())
		while(salary.isdigit()==False):
			salary=input("Enter salary in digits")
		Phnum =input("Enter the phone number")
		while(Phnum.isdigit()==False):
			Phnum=input("Enter phone number in digits")
		with open('userdata.txt','a+') as f1:
			f1.write("\n"+line+"-"+age+"-"+salary+"-"+Phnum)
		f1.close()
		flag=True
	
if(not flag):
	print("No match found")

f.close()
