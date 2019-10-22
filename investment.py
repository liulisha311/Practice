#!/usr/bin/env python3
amount = float(input("enter amount:")) # 輸入金額
inrate = float(input("enter interest rate:")) # 輸入利率
period = int(input("enter period:")) # 輸入期限
value = 0
year = 1
while year <= period:
    value = amount + (inrate * amount)
    print("Year {} Rs. {:.2f}".format(year,value))
    amount = value
    year = year + 1

