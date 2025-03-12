'''
An IPv4 address consists of four integers in the range 0 to 255 separated by a dots, for example 192.168.0.1 - this notation is referred to as dotted decimal notation.

Task
Write a program to check if an IPv4 address is valid. If the address is valid, display a "Valid IP address" message. Otherwise, display an "Invalid IP address" message.

Input format
A string of characters (the string length will be between 2 and 100 characters).
Output format
The message "Valid IP address" or "Invalid IP address"
Example
Input:
192.168.0.256
Output:
Invalid IP address
[Notes: Do not include text prompts for any inputs. For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''


string = input()
string = string.split(".")
stringLength = len(string)

for i in range(0,stringLength):
  string[i] = int(string[i])

if string[0] >= 0 and string[0] <= 255:
  if string[1] >= 0 and string[1] <= 255:
    if string[2] >= 0 and string[2] <= 255:
      if string[3] >= 0 and string[3] <= 255:
        valid = True
      else:
        valid = False
    else:
      valid = False
  else:
    valid = False
else:
  valid = False

if valid:
  print("Valid IP address")
else:
print("Invalid IP address")
