#Tip Calculator
#23 June 2018
#CTI 110 P2HW2 - Meal Tip Calculator
#Sean Mellers

#User enters bill total
total_bill = float(input('Enter bill total: '))

#User selects 15%
Fifteen = total_bill * .15

#User selects 18%
Eighteen = total_bill * .18

#User selects 20%
Twenty  = total_bill * .20

#User percentage options results
print('Fifteen Percent is $', format(Fifteen, ',.2f'), sep='')
print('Eighteen Percent is $', format(Eighteen, ',.2f'), sep='')
print('Twenty Percent is $', format(Twenty, ',.2f'), sep='')
