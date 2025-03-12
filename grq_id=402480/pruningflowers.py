'''
Task
Write a program that takes, as input, a string of flower names and outputs a new string with any duplicate names removed.

Input format
A list of flower names separated by a single space. Each name will be a single word. 
Output format
The output must contain the names of the flowers in the same order with any duplicates removed.
Example
Input
daisy ivy rose ivy tulip
Output
daisy ivy rose tulip
[Notes: Do not include text prompts for any inputs. For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''

string = input()
string = string.split(" ")

seen = set()
result = []

for i in string:
    if i not in seen:
        result.append(i)
        seen.add(i)
output = " ".join(result)

print(output)
