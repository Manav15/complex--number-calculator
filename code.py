# --------------
import pandas as pd
import numpy as np
import math


#Code starts here
class complex_numbers():
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def __repr__(self):

            if self.real == 0.0 and self.imag == 0.0:
                return "0.00"
            if self.real == 0:
                return "%.2fi" % self.imag
            if self.imag == 0:
                return "%.2f" % self.real
            return "%.2f %s %.2fi" % (self.real, "+" if self.imag >= 0 else "-",
            abs(self.imag))

    def __add__(self,other):
        
        sum_imag=self.imag+other.imag
        sum_real=self.real+other.real
        return complex_numbers(sum_real,sum_imag)

    def __sub__(self,other):

        sub_imag=self.imag-other.imag
        sub_real=self.real-other.imag
        return complex_numbers(sub_real,sub_imag)

    def __mul__(self,other):
        if(other.imag==0):
            mul_real=self.real*other.real
            mul_imag=self.imag*other.real
            return complex_numbers(mul_real,mul_imag)
        else:
            mul_real=(self.real*other.real)-(self.imag*other.imag)
            mul_imag=(self.imag*other.real)+(self.real*other.imag)
            return complex_numbers(mul_real,mul_imag)
    
   
    def __truediv__(self,other):

        div_real=((self.real*other.real)+(self.imag*other.imag))/(pow(other.real,2)+pow(other.imag,2))
        div_imag=((self.imag*other.real)-(self.real*other.imag))/(pow(other.real,2)+pow(other.imag,2))
        return complex_numbers(div_real,div_imag)

    def absolute(self):
        a=(pow(self.real,2)+pow(self.imag,2))
        s=pow(a,0.5)
        return s

    def argument(self):
        pi=3.14159
        argu=180*math.atan(self.imag/self.real)/pi
        return argu

    def conjugate(self):
        y=-self.imag
        x=self.real
        return complex_numbers(x,y)


print(complex_numbers(3,5).__repr__())

comp_1=complex_numbers(3,5)
comp_2=complex_numbers(4,4)

comp_sum=comp_1.__add__(comp_2)
comp_diff=comp_1.__sub__(comp_2)
comp_prod=comp_1.__mul__(comp_2)
comp_quot=comp_1.__truediv__(comp_2)
print(comp_quot)
comp_abs=comp_1.absolute()
comp_arg=comp_1.argument()
print(comp_arg)
comp_conj=comp_1.conjugate()


