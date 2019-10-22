#!/usr/bin/env python3
import math
a = int(input("enter value of a:"))
b = int(input("enter value of b:"))
c = int(input("enter value of c:"))
d = b * b -4 * a * c #公式爲：x=[-b±?(b^2-4ac)]/2a
if d < 0:
    print("roots are imaginary")
else:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
    print("root 1 = ", root1)
    print("root 2 = ", root2)
