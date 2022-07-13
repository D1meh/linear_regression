if __name__ == '__main__':

	try:
		file = open('variables.txt', 'r')
		line = file.read()
		a = float(line.split(' ')[0])
		b = float(line.split(' ')[1])
	except:
		a = 0
		b = 0
	
	try:
		x = float(input('Insert a mileage: '))
		print('Predicted price:', a * x + b)
	except:
		print('Input has to be numeric')

