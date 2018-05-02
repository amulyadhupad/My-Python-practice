""" This code is to print emtered mail address valid or not valid """

import re
mail = input("Enter your email address")
re_mail = re.compile(r".*@.*\..*")
if re_mail.match(mail):
	print("Valid Email address")
else:
	print ("Invalid email address")