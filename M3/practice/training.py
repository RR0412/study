
#1
for i in range(11):
    print(i)

counter = 0
while counter <= 10:
    print(counter)
    counter +=1


array = ["яблоко", "банан", "вишня"]

for element in array:
    print(element)


number = int(input())

if number < 0:
    print('Negative')
elif number > 0 :
    print('Positive')
else:
    print("Number is 0")

#2
array = [x**2 for x in range(10)]
print(array)

field = [['','','',],
         ['','','',],
         ['','','',]]

field = [['' for _ in range(3)] for _ in range(3)]

for element in field:
    print(element)
    print('\n')


counter = 0 
for row in field:
    for cell in row:
        if cell == '':
            counter +=1
print(counter)


for i in range(len(field)):
    for j in range(len(field[i])):
        if field[i][j] == '':
            field[i][j] = 'X'

# print(field)

print(field)


#3 
if all(cell == 'X' for row in field for cell in row):
        print('All cells are "X"')

if any(cell == 'O' for row in field for cell in row):
     print('There is "O" here')

if all(cell != '' for row in field for cell in row):
     print('Field is all full')


for row in field:
     if all(cell == 'X' for cell in row):
        print('Player with "X" won ! ')
        break


#4

field = [['','','',],
         ['','','',],
         ['','','',]]
symbol = input('Enter symbol:\n')


def check():
    for row in field:
        if all(cell == symbol for cell in row):
            print('Horizontal win')
    
    for col in range(len(field)):
        if  all(field[row][col] == symbol for row in range(len(field))):
            print('Vertical win')

    if all(field[i][i] == symbol for i in range(len(field))):
            print('Diagonal win 1 ! ')
    
    if all(field[i][len(field)-1-i] == symbol for i in range(len(field))):
            print('Diagonal win 2 !')
            




def turn():
    
    for i in range(9):
        try:
            x = int(input('Enter "X"\n'))
            y = int(input('Enter "Y"\n'))
        except ValueError as exc:
            print(exc)   
        field[x][y] = symbol
        for i in field:
            print (i)
            print ('\n')
            check()


turn()



