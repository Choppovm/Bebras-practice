'''
Introduction
A tram travels along its route, stopping at various points. At each stop, passengers can board or alight the tram. At the final stop any remaining passengers will leave the tram. 

Task
Write a program that takes as input a single line of text containing pairs of numbers. Each pair consists of two integers: the first integer represents the number of passengers boarding the tram at a stop, and the second integer represents the number of passengers getting off the tram at that stop. The program should calculate and output the total number of passengers on the tram when it reaches its final stop. 

Input format
A single line of text containing pairs of numbers.

The first integer represents the number of passengers boarding the tram at a stop.
The second integer represents the number of passengers getting off the tram at that stop.
All numbers will be in the range 0 -  100.
The input will contain no more than 15 pairs of numbers.
Output format
A single number representing the number of passengers who are on the tram when it reaches its final stop. 
Example
Input:
25 0,15 19,34 10,17 6
Output:
56
[Note: For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''

string = input()
string = string.split(",")
stringLength = len(string)
for i in range(0,stringLength):
  string[i] = string[i].split(" ")
stringLength = len(string)
numOfPassenger = 0 
for i in range(0,stringLength):
  numOfPassenger += int(string[i][0])
  numOfPassenger -= int(string[i][1])
print(numOfPassenger)
