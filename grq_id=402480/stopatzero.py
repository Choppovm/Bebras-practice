'''
Introduction
A simple horizontal graph is drawn from a stream of integers. Each line of the graph consists of a series of dashes (-), where the number of dashes corresponds to the value of the integer represented on that line. For example, the line ----- represents the number 5.

The input stream is in strictly decreasing order (each integer is less than the previous one). The input stream terminates when a value less than zero is encountered. This negative integer is a termination signal and is not included in the graph.

Task
Write a program that generates the graph. For each input value greater than zero, generate a line of dashes to represent that number. Your program should stop generating lines of dashes when it encounters a value that is less than zero. 

Input format
An unspecified number of rows - 'the input stream' - with a single number in each row.
No value in the input stream will be greater than 100.
The input stream will always have at least one integer that is greater than 0.
The input stream will always have at least one integer that is less than 0.
Output format
A horizontal line graph (as described in the introduction above)
Example
Input
7
5
2
1
-2
Output
-------
-----
--
-
[Note: For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''

while True:
  string = int(input())

  stringdash = ""

  if string > 0:
    for i in range(0, string):
      stringdash += "-"
  else:
    pass

  print(stringdash)
