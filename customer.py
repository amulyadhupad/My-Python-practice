""" Code for adding name, id and phone number of a customer """

class Customer(object):
	"""docstring for Customer"""
	def __init__(self,num,name,pnum):
		self.__custNo = num
		self.__custName = name
		self.__custPhone = pnum

	def displayCustomer(self):
		print("CustomerId:",self.__custNo)
		print("CustomerName:",self.__custName)
		print("Customerphone number:",self.__custPhone)
class MyError(Exception):
 
    # Constructor or Initializer
    def __init__(self, value):
        self.value = value
def getdetails():
	num = input("Enter your customer id")
	name = input("Enter your name")
	pnum = input("Enter your phone number")
	try:
		if len(pnum)==10:
			cust = Customer(num,name,pnum)
			cust.displayCustomer()
		else:
			raise (MyError("InvalidPhoneNumber"))
	except MyError as error:
    		print("A New Exception occured: ",error.value)
getdetails()
