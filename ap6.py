""" This code is to calculate a person age after 8,10 and 24 years and print the same """

import datetime
age = input("Enter your age")
now = datetime.datetime.now()
print (now)
n8 = now+datetime.timedelta(days=8*365)
a8 = int(age)+8
n10 = now+datetime.timedelta(days=10*365)
a10 = int(age)+10
n24 = now+datetime.timedelta(days=24*365)
a24 = int(age)+24
print ("At " + str(n8.date()), "you will be " +str(a8))
print ("At " + str(n10.date()), "you will be " +str(a10))
print ("At " + str(n24.date()), "you will be " +str(a24))