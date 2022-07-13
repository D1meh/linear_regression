import csv
import sys

def precision(data, a, b):
	content = csv.reader(data)
	next(content)

	errors = []
	for e in content:
		expected = int(e[0]) * a + b
		diff = abs(expected - int(e[1]))
		errVal = diff / int(e[1]) * 100
		errors.append(errVal)

	totalErr = sum(errors)
	mean = float(totalErr / len(errors))
	print('Accuracy of the gradient: ', 100 - mean, '%', sep='')

if __name__ == '__main__':
	try:
		if len(sys.argv) > 1:
			dataFile = sys.argv[1]
		else:
			dataFile = 'data.csv'

		data = open(dataFile)
		file = open('variables.txt')
		line = file.read()
		a = float(line.split(' ')[0])
		b = float(line.split(' ')[1])
		if a == 0 and b == 0:
			raise Exception
		file.close()
		precision(data, a, b)

	except:
		print("Data file not found and/or gradient.py not launched yet")
