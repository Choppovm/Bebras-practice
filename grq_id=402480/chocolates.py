'''
Introduction
You are given an even number of packets of chocolates to share with a friend, following these rules:

You choose two packets of chocolates from the pile. 
Your friend chooses one of the two packets, and you take the other.
This process is repeated until all packets are distributed.
Each packet contains a different number of chocolates. Your goal is to collect as many chocolates as possible, but your friend has the same goal and will always choose the packet with the most chocolates.

Task
Write a program that takes a list of integers as input, where each integer represents the number of chocolates in a packet. The program should output the maximum number of chocolates you can collect if you choose the pairs of packets wisely.

Input format
A list of integers separated by spaces. There will always be an even number of integers.

Output format
A single number (integer) representing the maximum number of chocolates you can collect.

Example
Input:
8 4 7 9 2 5
Output:
15
[Notes: Do not include text prompts for any inputs. For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''

def maxChocolates(chocolates):
    chocolates.sort()
    total = 0
    for i in range(0, len(chocolates), 2):
        total += chocolates[i]
    return total

inputChocolates = list(map(int, input().split()))
print(maxChocolates(inputChocolates))
