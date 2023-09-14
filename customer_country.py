import csv

customers = open('customers.csv', 'r')

country = open('customer_country.csv', 'w')

csv_file = csv.reader(customers)

next(csv_file) #skips a row for headers

count = 0
country.write("FirstName,LastName,Country\n")

for rec in csv_file:
    country.write(f"{rec[1]}, {rec[2]}, {rec[4]}\n")
    count += 1

country.close()

print("total number of customers:", count)
