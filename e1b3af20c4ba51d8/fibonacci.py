'''
In a Fibonacci sequence of numbers, the first two numbers are given and the next number in the sequence is the sum of the preceding two numbers.

The original Fibonacci sequence starts with 0, 1 and the Lucas sequence starts with 2, 1. But the same rule, “the next number in the sequence is the sum of the preceding two numbers”, can be used to generate sequences with any two starting numbers.

Example Fibonacci Series
0, 1, 1, 2, 3, 5, 8, ...
2, 1, 3, 4, 7, 11, 18, ...
7, 12, 19, 31, 50, 81, ...
You and your friend are fascinated with Fibonacci sequences. Your friend has made the extraordinary claim that any given positive starting pair of numbers will generate a sequence that contains, within the first 25 numbers, a number that is greater than 9 and is made up of a repeated single digit. For instance 13, 81 generates the sequence 13, 81, 94, 175, 269, 444.

You are sceptical about this claim, and decide to write a program to test it out.

Task:
Write a program that tests out your friend's claim.

Constraints:
[Note: You do not need to check constraints in your code for this competition - they are just for information about the range of test data values.]

All input integers will be between 0 and 5000 inclusive.
Input format:
The first two integers of the sequence are provided on two rows of input data.
Output format:
The first number that is made of a repeated single digit OR -1 if no such number is found in the first 25 numbers of the sequence.
Example:
Input:
13
81
Output:
444
[Note: For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''


def isRepeatedDigit(number):
    return len(set(str(number))) == 1

def findRepeatedDigitNumber(first, second):
    sequence = [first, second]
    for _ in range(23):
        nextNumber = sequence[-1] + sequence[-2]
        sequence.append(nextNumber)
    for number in sequence:
        if number > 9 and isRepeatedDigit(number):
            return number
    return -1

firstNumber = int(input())
secondNumber = int(input())
result = findRepeatedDigitNumber(firstNumber, secondNumber)
print(result)
