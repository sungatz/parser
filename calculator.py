print ("hello, im ur own calculator")

a = int(input("введите первое число"))
b = int(input("введите второ число"))		 
def kosu(a, b):
	return a + b 
def azaity(a, b):
	return a - b 

while True:
	tanba = input ("выберите действие (kosu, azaity): ")

	if tanba.lower == "kosu":
		print (kosu(a, b ))
	elif tanba.lower == "azaity":
		print (azaity(a, b))
	else:
		print('please use the correct ')
