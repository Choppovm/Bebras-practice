'''
Introduction
A student is saving her earnings from a part-time job to buy an e-bike. She spends £20 per day on food and bus fares. She wants to calculate how many days she will need to work to afford the bike, which costs £1,000.

Task
Write a program that calculates how many days it will take for the student to save £1,000. The program should total for her daily earnings and subtract £20 per day for expenses.

Input format
A list of 20 integers separated by spaces, representing daily earnings.

Each value will range from 0 to 200.
The total earnings over 20 days will always be sufficient to save £1,000 after accounting for expenses.
Output format
An number representing the number of days it will take to save £1,000.
Example
Input
80 150 200 90 110 150 150 77 59 200 100 190 205 190 115 150 160 97 102 100
Output
10
[Note: For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''

string = input()
string = string.split(" ")

length = len(string)
for i in range(0, length):
  string[i] = int(string[i])

total = 0
valid = False
count = 0
while not valid:
  total = string[count] + total
  if total >= 1000:
    valid = True
    pass
  else:
    pass
  count = count + 1
  total = total - 20

print(count)
