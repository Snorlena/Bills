bills = {}

sallary = int(input('Enter your sallary: '))
csn = int(input('Enter CSN: '))
other_income = int(input('Other income: '))

total_income = sallary + csn + other_income

print('Enter Q to quit')
while True:
    bill_name = input('Enter the name of bill: ')
    if bill_name.upper() == 'Q':
        break
    else:
        bill_amount = int(input('Enter the amount to pay: '))
        bills[bill_name] = bill_amount

for row in bills:
    print(row, bills[row])

summa = sum(bills.values())
print('You will have', total_income - summa, 'left after paying the bills.')