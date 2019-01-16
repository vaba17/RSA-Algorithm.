#!/usr/bin/python

import random
import sys
from time import time
def gcd( a, b ):
	while b != 0:
		c = a % b
		a = b
		b = c
		#a is returned if b == 0
	return a
def pow(x, y):
	"""Raise x to the power y, where y must be a nonnegative integer."""
	result = 1
	for _ in range(y):   # using _ to indicate throwaway iteration variable
    	result = x
	return result


t1 = time()
try:
	p=int(input('p:'))
	q=int(input('q:'))
except ValueError:
	print ("Not a number")
n = p * q

print ("product of two numbers is :", n)

p_1 = p-1
q_1 = q-1
pq = (p_1) * (q_1)
if (p == q):
	print ("Given values are same. Enter another values")
else:
	print("you choosed wright no's.", pq)


for x in range(1):
	g = int(input("Enter a number between 1 & pq"))
	print ("random number is g:", g)
	if (gcd(g , pq == 1)):
		print ("generated random number is public Key")
	else:
    	g= random.randit(1,pq)
        print ("random number is g:", g)

#private key

k = input("enter a no. less than g k:")
print("random integer less than g:", k)
ram = int(k * pq)
J =int (ram +1)
print ("ravan=", J)
d =  int(J )//int( g)
print ("private key is d:", d)

#Encryption

try:
	m=int(input('m:'))

except ValueError:
	print ("Not a number")

alpha= int(m ** g)
c= (alpha% pq)
print ("encryption of given message is c:", c)
size2 = c.bit_length()
size1 = m.bit_length()
print("message size is",size1)
print("encryption size is ",size2)


#decryption

t2= time()
print (" encryption time is :", t2-t1)

beta = pow(c, d)
print ("beta =",beta)

dec = (beta% pq)

print("decryption of given encryption is:", dec)
t4 = time()
print (" encryption time is :", t2-t1)
print (" decryption time is :", t4-t1)
