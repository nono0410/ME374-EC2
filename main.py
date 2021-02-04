import math as m
import mech
import draw as D

# Read user input
l0 = float(input("Enter length L_0: "))
l1 = float(input("Enter length L_1: "))
l2 = float(input("Enter length L_2: "))
l3 = float(input("Enter length L_3: "))
assert (l0>0), 'l0 (%f) has to be positive' %l0
assert (l1>0), 'l1 (%f) has to be positive' %l1
assert (l2>0), 'l2 (%f) has to be positive' %l2
assert (l3>0), 'l3 (%f) has to be positive' %l3

ls = sorted([l0,l1,l2,l3]) # Sort list from low to high

mech.mech(ls,l0,l1,l2,l3)

D.draw(l0,l1,l2,l3)