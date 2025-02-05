#!/usr/bin/env python3

"""Write a program to calculate the number of perfect squares within a number range"""

__author__="Lydia Frame"
__date__="02/05/2025"

#prompt for first num
first=int(input("First? "))
print()

#prompt for second num - must be bigger than first
while True:
    second=int(input("Second? "))
    print()
    if second > first:
        second+=1
        break

# Calculate number of perfect squares in the range
count=0
for i in range(first, second):
    calculate = int(i**.5)
    if calculate**2 == i:
        print(str(calculate)+" * "+str(calculate)+" = "+str(i))
        count+=1

print("Total of "+str(count)+" perfect squares")