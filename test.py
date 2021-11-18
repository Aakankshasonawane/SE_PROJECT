import unittest
import sys
from calculator import *

def setUpModule():
    print('Start testing module: ')

def tearDownModule():
    print('End the testing module.')

class Tests(unittest.TestCase):


    #Test_case for Addition
    def test_add_positive_nos_1(self):
        x = 2
        y = 3
        self.assertEqual(add(x,y), 5, msg=None)

    def test_add_negative_nos_1(self):
        x = -2
        y = -3
        self.assertEqual(add(x,y), -5, msg=None)

    def test_add_zero_nos_1(self):
        x = -2 
        y = 0
        self.assertEqual(add(x,y), -2, msg=None)

    def test_add_negative_positive_1(self):
        x = -2
        y = 3
        self.assertEqual(add(x,y), 1, msg=None) 

    #Test_case for Subtraction
    def test_sub_positive_nos_1(self):
        x = 21
        y = 3
        self.assertEqual(sub(x,y), 18, msg=None)

    def test_sub_negative_nos_1(self):
        x = -20
        y = -32
        self.assertEqual(sub(x,y), 12, msg=None)

    def test_sub_zero_nos_1(self):
        x = -2 
        y = 0
        self.assertEqual(sub(x,y), -2, msg=None)

    def test_sub_negative_positive_1(self):
        x = 2
        y = -3
        self.assertEqual(sub(x,y), 5, msg=None)

    #Test_case for Multiplication
    def test_mul_positive_nos_1(self):
        x = 2
        y = 3
        self.assertEqual(mult(x,y), 6, msg=None)

    def test_mul_negative_nos_1(self):
        x = -2
        y = -3
        self.assertEqual(mult(x,y), 6, msg=None)

    def test_mul_zero_nos_1(self):
        x = -2 
        y = 0
        self.assertEqual(mult(x,y), 0, msg=None)

    def test_mul_negative_positive_1(self):
        x = 2
        y = -3
        self.assertEqual(mult(x,y), -6, msg=None)

    #Test_case for Division
    def test_div_positive_nos_1(self):
        x = 21
        y = 3
        self.assertEqual(div(x,y), 7, msg=None)

    def test_div_negative_nos_1(self):
        x = -21
        y = -3
        self.assertEqual(div(x,y), 7, msg=None)

    def test_div_zero_nos_1(self):#doubt
        x = 2 
        y = 0
        self.assertEqual(div(x,y), 1/0, msg=None)

    def test_div_negative_positive_1(self):
        x = -27
        y = 3
        self.assertEqual(div(x,y), -9, msg=None)

    #Test_case for Modulus
    def test_mod_positive_nos_1(self):
        x = 24
        y = 12
        self.assertEqual(mod(x,y), 0, msg=None)

    def test_mod_negative_nos_1(self):
        x = -21
        y = -3
        self.assertEqual(mod(x,y), 0, msg=None)

    def test_mod_zero_nos_1(self):#doubt
        x = 2 
        y = 0
        self.assertEqual(mod(x,y), 0, msg=None)

    def test_mod_negative_positive_1(self):
        x = 12
        y = -5
        self.assertEqual(mod(x,y), -3, msg=None) 

    #Test_case for Naturl-Log function
    def test_log_positive_nos_1(self):
        x = 10
        self.assertEqual(log(x), 1, msg=None)

    def test_log_negative_nos_1(self):#error
        x = -2
        self.assertEqual(log(x), ValueError, msg=None)

    def test_log_zero_nos_1(self):#doubt
        x = 0
        self.assertEqual(log(x), -(1/0), msg=None)
     
    #Test_case for Exponential
    def test_exp_positive_nos_1(self):
        x = 2
        y = 3
        self.assertEqual(exp(x,y), 8, msg=None)

    def test_exp_negative_nos_1(self):
        x = -2
        y = -2
        self.assertEqual(exp(x,y), 0.25, msg=None)

    def test_exp_zero_nos_1(self):#doubt
        x = 2 
        y = 0
        self.assertEqual(exp(x,y), 1, msg=None)

    def test_exp_negative_positive_1(self):
        x = -2
        y = 3
        self.assertEqual(exp(x,y), -8, msg=None) 

    #Test_case for Square-root function
    def test_sqrt_positive_nos_1(self):
        x = 4
        self.assertEqual(sqrt(x), 2, msg=None)

    def test_sqrt_negative_nos_1(self):
        x = -4
        self.assertEqual(sqrt(x), ValueError, msg=None)

    def test_sqrt_zero_nos_1(self):#doubt
        x = 0
        self.assertEqual(sqrt(x), 0, msg=None)
    
    #Test_case for Reciprocal function
    def test_reciproc_positive_nos_1(self):
        x = 4
        self.assertEqual(reciprocal(x), 0.25, msg=None)

    def test_reciproc_negative_nos_1(self):
        x = -4
        self.assertEqual(reciprocal(x), -0.25, msg=None)

    def test_reciproc_zero_nos_1(self):#doubt
        x = 0
        self.assertEqual(reciprocal(x), ValueError, msg=None)

     #Test_case for Factorial function
    def test_fact_positive_nos_1(self):
        x = 4
        self.assertEqual(fact(x), 24, msg=None)

    def test_fact_negative_nos_1(self):
        x = -4
        self.assertEqual(fact(x), ValueError, msg=None)

    def test_fact_zero_nos_1(self):
        x = 0
        self.assertEqual(fact(x), 1, msg=None)

    #Test_case for Sine function
    def test_sin_positive_nos_1(self):
        x = math.pi/2
        self.assertEqual(sine(x), 1, msg=None)

    def test_sine_negative_nos_1(self):
        x = -(math.pi/2)
        self.assertEqual(sine(x), -1, msg=None)

    def test_sine_zero_nos_1(self):
        x = 0
        self.assertEqual(sine(x), 0, msg=None)   

       

     #Test_case for Sine-hyperbolic function
    def test_sinh_positive_nos_1(self):
        x = 1
        self.assertEqual(sinh(x), 1.1752011936438014, msg=None)

    def test_sinh_negative_nos_1(self):
        x = -1
        self.assertEqual(sinh(x), -1.1752011936438014, msg=None)

    def test_sinh_zero_nos_1(self):
        x = 0
        self.assertEqual(sinh(x), 0, msg=None)   

   


if __name__=='__main__':
     unittest.main()
            
