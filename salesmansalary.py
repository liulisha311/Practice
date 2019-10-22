#!/usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
numberofcamera = int(input("enter the number of inputs sold:"))
price = float(input("enter the price of camera:"))
bonus = (bonus_rate * numberofcamera)
commission = (commission_rate * price * numberofcamera)
print("bonus = {:6.2f}".format(bonus))
print("commission = {:6.2f}".format(commission))
print("gross salary = {:6.2f}".format(basic_salary + bonus + commission))
