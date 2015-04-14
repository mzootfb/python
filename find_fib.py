import math
n = input("Which Fibonacci number would you like? :")
sqt = math.sqrt(5)
Phi = (1+sqt)/2
lil_phi = -1/Phi
an = (Phi**n - (lil_phi)**n)/sqt
print an
