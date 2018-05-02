""" Code to enter name, numbwe and salary of an employee """

class Employee(object):
	"""docstring for Customer"""
	def __init__(self,num,name,salary):
		self.__empNo = num
		self.__empName = name
		self.__empBasic = salary

	def display(self):
		with open('emp.txt','r') as f1:
			contents=f1.read()
			print(contents)
def getdetails():
	num = input("Enter your Employee Id")
	name = input("Enter your name")
	salary = input("Enter your basic salary number")
	emp=Employee(num,name,salary)
	with open('emp.txt','w') as f:
		f.write("\n"+num+"-"+name+"-"+salary)
	emp.display()
getdetails()


