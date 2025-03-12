# warning: this code is bound to give any programmer stage 10 brain cancer

'''
Introduction
Magic squares consist of 9 digits arranged in a 3x3 grid. What makes them magical is that the sum of the numbers in each row, each column, and both diagonals is always the same. This sum is always 15.

Example Magic Square
8 1 6
3 5 7
4 9 2
Task
Write a program that takes the three rows of a magic square as input and checks whether it is a valid magic square. The program should output "magic" if the square is valid and "muggle" if it is not.

Input format
Three lines of three integers separated by spaces.
Each integer value will be in the range 1 to 9.
Output format
The word "magic" (if the square is a magic square) or the word "muggle" (if the square is not a magic square)
Example
Input:
8 1 6
3 5 7
4 9 2
Output:
magic
[Note: For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''

string1 = input()
string2 = input()
string3 = input()

string1 = string1.split(" ")
string2 = string2.split(" ")
string3 = string3.split(" ")

stringLength = len(string1)

for i in range(0, stringLength):
  string1[i] = int(string1[i])
  string2[i] = int(string2[i])
  string3[i] = int(string3[i])

if string1[0] + string2[0] + string3[0] == 15:
  valid = True
  if string1[1] + string2[1] + string3[1] == 15:
    valid = True
    if string1[2] + string2[2] + string3[2] == 15:
      valid = True
      if string1[0] + string1[1] + string1[2] == 15:
        valid = True
        if string2[0] + string2[1] + string2[2] == 15:
          valid = True
          if string3[0] + string3[1] + string3[2] == 15:
            valid = True
            if string1[0] + string2[1] + string3[2] == 15:
              valid = True
              if string1[2] + string2[1] + string3[0] == 15:
                valid = True
              else:
                valid = False
            else:
              valid = False
          else:
            valid = False
        else:
          valid = False
      else:
        valid = False
    else:
      valid = False
  else:
    valid = False
else:
  valid = False

if valid == True:
  print("magic")
else:
print("muggle")
