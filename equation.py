import math

def quadratic(a, b, c):
    d=b*b-4*a*c
    result1=(-b+math.sqrt(d))/2*a
    result2=(-b-math.sqrt(d))/2*a
    return(result1,result2)
