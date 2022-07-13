import csv, sys
import matplotlib.pyplot as plt

LEARNING_RATE = 0.00001
if len(sys.argv) > 2:
	firstColor = sys.argv[1]
	secondColor = sys.argv[2]
else:
	print("You can personalize the colors that will be printed on the graph! See https://matplotlib.org/stable/gallery/color/named_colors.html for more details.")
	firstColor = 'blue'
	secondColor = 'red'

def derivateA(real, a, b, input, n):
	return -(2/n) * input * (real - (a * input + b))

def derivateB(real, a, b, input, n):
	return -(2/n) * (real - (a * input + b))

def gradientDescent(km, price, a, b):
	sumA = 0
	sumB = 0
	n = len(km)

	for i in range(n):
		sumA += derivateA(price[i], a, b, km[i], n)
		sumB += derivateB(price[i], a, b, km[i], n)

	retA = a - sumA * LEARNING_RATE
	retB = b - sumB * LEARNING_RATE
	return retA, retB

def gradientLoop(km, price, normalKm, normalPrice, refValues):
	a = -1
	b = 0

	for i in range(1000):
		a, b = gradientDescent(km, price, a, b)

	a = a / (refValues['maxKm'] - refValues['minKm']) * (refValues['maxPrice'] - refValues['minPrice'])
	b = ( (a+b) * (refValues['maxPrice'] - refValues['minPrice']) + refValues['minPrice']) - (a * refValues['maxKm'])
	
	with open('variables.txt', 'w+') as fd:
		fd.write("{0} {1}".format(a, b))

	try:
		plt.scatter(normalKm, normalPrice, color=firstColor, label="Actual values")
	except:
		print("Bad color input: ", firstColor)
		plt.scatter(normalKm, normalPrice, color="blue", label="Actual values")

	try:
		plt.plot(list(range(0, max(normalKm))), [a * x + b for x in range(0, max(normalKm))], color=secondColor, label="Excepted values from Linear Regression")
	except:
		print("Bad color input: ", secondColor)
		plt.plot(list(range(0, max(normalKm))), [a * x + b for x in range(0, max(normalKm))], color="red", label="Excepted values from Linear Regression")

	plt.xlabel("Kilometers")
	plt.ylabel("Price")
	plt.legend()
	plt.show()

def startGradient():
	try:
		file = open('data.csv')
	except:
		print("Can't open data.csv")
		return

	content = csv.reader(file)
	header = next(content)
	values = []
	km = []
	price = []
	for e in content:
		values.append(e)
		km.append(int(e[0]))
		price.append(int(e[1]))

	minKm, maxKm = min(km), max(km)
	minPrice, maxPrice = min(price), max(price)
	normalizedKm = []
	normalizedPrice = []
	for i in range(len(values)):
		normalizedKm.append((km[i] - minKm) / (maxKm - minKm))
		normalizedPrice.append((price[i] - minPrice) / (maxPrice - minPrice))

	gradientLoop(normalizedKm, normalizedPrice, km, price, {'minKm': minKm, 'maxKm': maxKm, 'minPrice': minPrice, 'maxPrice': maxPrice})

if __name__ == '__main__':
	startGradient()