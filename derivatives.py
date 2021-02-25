from sympy.utilities.lambdify import lambdify
from sympy import *
from numpy import *
import sympy as sym
from scipy.integrate import *
import math, scipy
from scipy import integrate
import numpy as np
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z = sym.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')
resp = "y"
print("Welcome to the DERIVATIVE calculator. This calculator is capable of differentiating single and multi-variable functions. Don't worry about the conditions, just enter the functions and variables.")
print("Enter the function you want to differentiate along the differentiating variable.")
aba = input("Function now:\n")
diff_var = input("Variable now:\n")
def differentiate(aba):
    def g(x):
        func = eval(abc)
        return func
    #print(aba)
    abc = aba.replace("^", "**").replace("sin", "sym.sin").replace("cos", "sym.cos").replace("ln", "sym.ln").replace("log", "sym.log").replace("tan", "sym.tan").replace("csc", "sym.csc").replace("sec", "sym.sec").replace("cot", "sym.cot").replace("asym.tan", "sym.atan").replace("asym.sin", "sym.asin").replace("asym.cos", "sym.acos").replace("asym.csc", "sym.acsc").replace("asym.sec", "sym.asec").replace("asym.cot", "sym.acot")
    # Define function g
    print("The derivative of " + str(g(x)).replace("**", "^") + " with respect to " +diff_var+" is: ")
    xa = str(sym.diff(g(x), diff_var))
    orderivative = xa.replace("**", "^")
    print(orderivative)
differentiate(aba)
