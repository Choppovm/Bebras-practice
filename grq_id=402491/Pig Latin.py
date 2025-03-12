'''
Introduction
Pig Latin is a language where words are made by modifying English words. The rules are as follows:

If the letter starts with a consonant:
Step 1: Remove the first letter of the word.
Step 2: Add a “-” to the end of the word.
Step 3: Add the letter you removed in step 1 to the end of the word.
Step 4: Add ”ay” to the end of the word. 
If the letter starts with a vowel:
Just add “-yay“ to the end of the word.
Task
Write a program that translates a word into Pig Latin.

Input format
A single English word. The word will only consist of uppercase and lowercase letters.
Output format
The same word in Pig Latin. 
Example 1
Input
Hello
Output
ello-Hay
Example 2
Input
Egg
Output
Egg-yay
[Notes: Do not include text prompts for any inputs. For languages such as Java/C# which require a class definition, the main class should be called: Solution.]
'''

v = ["A", "E", "I", "O", "U"]

string = input()
stringArray = []
lengthString = len(string)
for i in range(0, lengthString):
  stringArray.append(string[i])

if stringArray[0] == v[0] or stringArray[0] == v[1] or stringArray[0] == v[2] or stringArray[0] == v[3] or stringArray[0] == v[4]:
  string = string + "-" + "yay"
else:
  temp = stringArray.pop(0)
  string = ""
  lengthArray = len(stringArray)
  for i in range(0, lengthArray):
    string = string + stringArray[i]
  string = string + "-" + temp + "ay"
print(string)
