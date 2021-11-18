import sys
import math


def add(x,y):
    return x + y

def sub(x,y):
    return x - y
        

def mult(x,y):
    return x*y
      
def div(x,y):
    if y == 0:
        raise ValueError('Cant divide by zero')
    return x/y
       
def mod(x,y):
    if(x == 0 or y == 0):
        raise ValueError('Cant calculate modulus if one no is zero')
    return x % y
                
def log(x):
    if(x == 0 or x<0):
        raise ValueError('Cant find log of negative number or zero')
    log = math.log10(x)    
    return log 

def exp(x,y):
    return x**y

def sqrt(x):
    if(x == 0 or x< 0):
        raise ValueError('Cant find root of zero or negative number')
    return math.sqrt(x) 

def reciprocal(x):
    if x == 0:
        raise ValueError('Cant find reciprocal of zero')
    return 1/x       
    
def fact(x):
    if x<0:
        raise ValueError('Cant find factorial of negative number')
    fact=1
    if(x==0 or x==1):
        return 1
    else:
        for i in range (x,1,-1):
            fact=fact*i
        return fact
        
def sine(x):
    return math.sin(x) 
    
    
def sinh(x):
    return math.sinh(x)
    
   

