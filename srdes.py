"""Code to open file using arguments and write in the file with given choice for overwrite or not """

import sys
import os.path
try:
	with open(sys.argv[1], 'r') as f:
    	 contents = f.read()
except FileNotFoundError:
	print ("File does not exist")
else:
	if (os.path.isfile(sys.argv[2])):
		val=input("File already exists. Want to overwrite?(Yes/No)")
		if val in ['yes', 'Yes']:
			with open(sys.argv[2], 'w') as b:
				b.write(contents)
		else:
			with open(sys.argv[2],'a+') as c:
				c.write(contents)
	else:
		with open(sys.argv[2], 'w+') as e:
			e.write(contents)