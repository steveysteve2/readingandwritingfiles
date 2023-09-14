import csv

#customers = open('customers.csv', 'r')

pay = open('EmployeePay.csv', 'r')

#csv_file = csv.reader(customers)

pay_file = csv.reader(pay)

next(pay_file) #skips a row for headers

for rec in pay_file:
    print(f"First Name: {rec[1]}\nLast Name: {rec[2]}")
    sal = int(rec[3])
    bonus = sal * float(rec[4])
    total = sal + bonus
    print(f"Salary:    $  {sal:10,.2f}")
    print(f"Bonus:     $  {bonus:10,.2f}")
    print(f"Total Pay: $  {total:10,.2f}")
    input()

pay.close()