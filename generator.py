from random import randint
import sys

if len(sys.argv) > 1 and sys.argv[1].isnumeric():
	file = open('generator.csv', 'w+')
	file.write('km,price\n')
	with open('variables.txt', 'r') as fd:
		line = fd.read()
		a = float(line.split(' ')[0])
		b = float(line.split(' ')[1])

	nbVal = int(sys.argv[1])
	while nbVal > 0:
		rand = randint(50000, 400000)
		price = int(rand * a + b)
		if (price < 0):
			continue
		file.write(str(rand) + ',' + str(price) + '\n')
		nbVal -= 1
	file.close()
else:
	print("Enter a numeric value")