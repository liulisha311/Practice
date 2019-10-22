#!/usr/bin/env python3
N = 10
sum = 0
count = 0
print("please input 10 numbers:")
while count < 10:
    num = float(input())
    sum = sum + num
    count += 1
average = sum / N
print("N = {}, sum = {}".format(N,sum))
print("Average = {:.2f}".format(average))
