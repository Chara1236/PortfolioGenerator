import csv
import random
file = open("example_tickers3.csv", "r")
data = list(csv.reader(file))
##file.close()

generate_amount = 40

with open('temp_tickers.csv', 'w') as myfile:
    for i in range(0, generate_amount):
        stock = data[(random.randint(0, len(data)-1))]
        myfile.write(stock[0]+"\n")
        data.remove(stock)


myfile.close()




file.close()