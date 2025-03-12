'''
Alesis is concerned about the CO2 emissions from his petrol car. According to his car manual, burning 1 litre of petrol produces 0.0024 tonnes of CO2.

Task
Write a program to calculate the total tonnes of CO2 produced by a car in a year, rounded down to the nearest whole number. The program should take as input a list of 12 numbers, each representing the liters of petrol used per month.

Sample calculation:
2136 litres used over a year
Annual CO2 = 2136 * 0.0024 = 5.1264
Annual CO2 = 5 tonnes (rounded down to nearest whole number)
Input format
A list of 12 numbers (positive integers) separated by spaces. The values will be in the range 0 to 200 inclusive. 
Output format
A number (positive integer) representing the tonnes of CO2 produced, rounded down to the nearest whole tonne.
Example
Input
142 150 120 182 202 205 231 258 214 162 148 122
Output
5
 
[Note: For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''

import math

string = input()
string = string.split(" ")

length = len(string)
total = 0

for i in range(0, length):
  string[i] = int(string[i])
  total += string[i]

tonnes = total * 0.0024
tonnes = math.floor(tonnes)

print(tonnes)
