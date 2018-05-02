""" This code is to find average using class and functions """

class Average(object):

	def print_avg(self,totalsum,totalnumber):
		self.totalsum=totalsum
		self.totalnumber=totalnumber
		res=avg.compute_avg(totalsum,totalnumber)
		print(res)

	def compute_avg(self,sum,number):
		try:
			if int(sum)>int(number):
				com=int(sum)/int(number)
				return com
		except ZeroDivisionError:
			print("ZeroDivisionError handled, enter number greater than zero")
avg=Average()
total=input("Enter the total to calculate Average")
number=input("Enter the number")
avg.print_avg(total,number)