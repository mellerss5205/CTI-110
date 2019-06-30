#CTI 110
#P3HW1_Color Mixer_Sean Mellers
#Sean Mellers
#26 June 2019

#User inputs two primary colors
primary1 = input('Enter primary1: ')
primary2 = input('Enter primary2: ') 

#Program mixes colors and displays results.
if primary1 == 'red' and primary2 == 'blue' or primary1 == 'blue' and primary2 == 'red':
    print('Purple')
elif primary1 == 'red' and primary2 == 'yellow' or primary1 == 'yellow' and primary2 == 'red':
    print('Orange')
elif primary1 == 'blue' and primary2 == 'yellow' or primary1 == 'yellow' and primary2 == 'blue':
    print('Green')
else:
    print('Primary Color(s) not entered. Please enter Primary Colors.')

