#CTI -110
#P3HW2 - Meal Tip and Tax
#Sean Mellers
#26 June 2019

#User provides meal charge.
charge = float(input('Enter meal charge: $'))

#User provides tip percentage.
tip = float(input('Enter tip percentage: %')) / 100

#Program discerns percentages.
if tip == 15 / 100:
    print('15% tip: $', format(charge * 0.15, '.2f'))
elif tip == 18 / 100:
    print('18% tip: $', format(charge * 0.18, '.2f'))
elif tip == 20 / 100:
    print('20% tip: $', format(charge * 0.20, '.2f'))
else:
    print('Please select a tip of: 15%, 18%, or 20%')

#Program calculates tax and total.
tax = charge * 0.07
tip = charge * tip
total = charge + tip + tax

print('Tax:', format(charge * 0.07, '.2f'))
print('Total:', format(charge + tip + tax, '.2f'))
