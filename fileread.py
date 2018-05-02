""" Code to open a file and print each sentence in new line """

with open('New Text Document.txt', 'r') as f:
	for i, line in enumerate(f):
		print('{}={}'.format(i+1,line.strip()))