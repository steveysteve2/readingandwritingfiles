import csv

#customers = open('customers.csv', 'r')

pay = open('sales.csv', 'r')

outfile = open('salesreport.csv', 'w')

#csv_file = csv.reader(customers)

pay_file = csv.reader(pay)

next(pay_file) #skips a row for headers

payin = '250'
total = 0

outfile.write(f"Customer_ID, Total\n")

for rec in pay_file:
    if payin == rec[0]:
        total += float(rec[3]) + float(rec[4]) + float(rec[5])
    else:
        outfile.write(payin + ',' + str(round(total,2)) + '\n')
        payin = rec[0]
        total = float(rec[3]) + float(rec[4]) + float(rec[5])
        
pay.close()

outfile.write(payin + ',' + str(round(total,2)) + '\n')

print('done')

outfile.close()