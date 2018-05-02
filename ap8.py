""" This code is to get the name from the dictionary and print the corresponding value """

dict = {'Apple':'20','Orange':'10','Grapes':'25'}
name = input("Enter the fruit name to know the price")
val=dict.get(name)
print(val)