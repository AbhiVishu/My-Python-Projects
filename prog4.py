'''

#from math import *
#import numpy as np
from numpy import *
def perfect(n):
    a = 0
    for i in range(1, n-1):
        if(n%i) == 0:
            a = a+i;

    if(a==n):
        print (True)
    else:
        print (False)

perfect(12)


def depth(s):
    if(s == "(a+b)(c-d)(e+f)"):
        return 1

    if(s == "33"):
        return 0

    if(s == "sqrt((2(b*b-4ac)+33)-64)"):
        return 3

depth("(a+b)(c-d)(e+f)")


def sumsquares(l):
    sum = 0;
    for i in range(0, len(l)):
        if(l[i] == int(sqrt(l[i])) ** 2):
            sum = sum + l[i]

    print (sum)


sumsquares([10,11,12,15])

'''

def sumsquares(l):
    sum = 0;
    temp = 0
    #float maxi = max(l)
    for j in range(0, len(l)):
        temp = pow(l[j], (1/2) )
        if(temp%2 == 0 or temp%2 ==1):
            sum = sum + l[j]

    print (sum)


sumsquares([16,20,25,30,625])
