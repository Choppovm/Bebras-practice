'''
Introduction
In an Ultrarun season, each runner has to compete in five races. The runners are awarded points calculated by a number of factors such as how long it took to complete, their overall finishing position, how hilly the run was, etc..

Every runner aims to improve their performance throughout the season by getting more points than in their previous races in the same season. A runner is said to be a "happy runner" if they achieve this in every race throughout the season.

Task
Write a program that outputs the number of "happy runners" at the end of the season from the data provided.

Input format
On the first line, an integer, n, representing the number of runners.
On each of the next n lines, a set of five integers representing the points scored by a single runner in each race, in chronological order starting with the first race. 
The fewest points a runner can be awarded in a race is 0 and the maximum is 100.
Output format
A number representing the number of "happy runners" at the end of the season.
Example
Input:
4
50 50 70 80 100
65 50 70 85 85
60 70 75 80 90
70 70 65 70 75
Output
1
[Notes: Do not include text prompts for any inputs. For languages such as Java/C# which require a class definition, the main class should be called: solution.]
'''

n = int(input())
scores = []

for i in range(n):
    temp = list(map(int, input().split()))
    scores.append(temp)

happy = 0

for runner in scores:
    if runner[0] < runner[1] < runner[2] < runner[3] < runner[4]:
        happy += 1

print(happy)
