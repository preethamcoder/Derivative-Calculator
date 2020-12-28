from sympy.utilities.lambdify import lambdify
from sympy import *
from numpy import *
from scipy.integrate import *
import math, scipy
import sympy as sym
from scipy import integrate
import numpy as np
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sym.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
print("Welcome to the DERIVATIVE calculator. This calculator is capable of differentiating single and multi-variable functions. Don't worry about the conditions, just enter the functions and variables!")
print("Enter the function you want to differentiate along the differentiating variable!")
aba = input("Function now:\n")
diff_var = input("Variable now:\n")
abc = aba.replace("^", "**").replace("sin", "sym.sin").replace("cos", "sym.cos").replace("ln", "sym.ln").replace("log", "sym.log")
#print(aba)
# Define function g
def g(x):
    func = eval(abc)
    return func
print("The derivative of " + str(g(x)) + " with respect to " +diff_var+" is: ")
xa = str(sym.diff(g(x), diff_var))
orderivative = xa.replace("**", "^")
print(orderivative.replace("**", "^"))
