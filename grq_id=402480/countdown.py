'''
Task:
Write a program that displays a rocket countdown sequence starting from a given number. At the end of the countdown, display the words "lift off".

Input format:
A whole number in the range 1 to 100.
Output format:
A series of numbers, each on a separate row, followed by the words "lift off".
Example:
Input:
3
Output:
3
2
1
lift off
[Notes: Do not include text prompts for any inputs. For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''

string = int(input())

for i in range(0, string):
  print(string - i)
print("lift off")
