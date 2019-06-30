#CTI 110
# P3LAB Debuging
#30 June 2019
#Sean Mellers

def main():
#This program takes a number grade and outputs a letter grade.

#System uses 10-point grading scale
    A_score = 90
    B_score = 89
    C_score = 79
    D_score = 69
    F_score = 59

#Program Calculates Grades.
score = int(input('Enter score: '))

if score >= 90:
        print('Your grade is: A')
elif 89 >= score >= 80:
        print('Your grade is: B')
elif 79 >= score >= 70:
        print('Your grade is: C')
elif 69 >= score >=60:
        print('Your grade is: D')
else:
        print('Your grade is: F')

# program start
main()
