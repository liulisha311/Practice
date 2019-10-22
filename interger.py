#!/usr/bin/env python3
days = int(input("enter days:"))
''' month = days // 30
days = days % 30
print("month = {}, days = {}".format(month,days)) '''
print("month = {}, days = {}".format(*divmod(days,30)))

