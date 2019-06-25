#CTI-110
#P3T1 Area of Rectangle
#Sean Mellers
#25 June 2019

#User provides dimensions of rectangle 1
length1 = int(input('Enter length of rectangle 1: '))
width1 = int(input('Enter width of rectangle 1: '))

#User provides dimensions of rectangle 2
length2 = int(input('Enter length of rectangle 2: '))
width2 = int(input('Enter width of rectangle 2: '))

#Calculate dimensions
area1 = length1 * width1
area2 = length2 * width2

#Confirm results
if area1 > area2:
    print('Rectangle1 has the greater area.')
elif area1 < area2:
    print('Rectangle2 has the gtreater area.')
else:
    print('Both Rectanlges have the same area.')
