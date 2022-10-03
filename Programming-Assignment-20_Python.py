#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Python3 code to demonstrate
# Prefix Separation
# Using list comprehension + startswith()

# initializing list
test_list = ['sapple', 'orange', 'smango', 'grape']

# initializing start Prefix
start_letter = 's'

# printing original list
print("The original list : " + str(test_list))

# using list comprehension + startswith()
# Prefix Separation
with_s = [x for x in test_list if x.startswith(start_letter)]
without_s = [x for x in test_list if x not in with_s]

# print result
print("The list without prefix s : " + str(without_s))
print("The list with prefix s : " + str(with_s))


# In[2]:


list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 3
list_numbers.index(element)


# In[3]:


''' Python3 program to calculate Volume and
	Surface area of Cone'''

# Importing Math library for value Of PI
import math
pi = math.pi

# Function to calculate Volume of Cone
def volume(r, h):
	return (1 / 3) * pi * r * r * h

# Function To Calculate Surface Area of Cone
def surfacearea(r, s):
	return pi * r * s + pi * r * r

# Driver Code
radius = float(5)
height = float(12)
slat_height = float(13)
print( "Volume Of Cone : ", volume(radius, height) )
print( "Surface Area Of Cone : ", surfacearea(radius, slat_height) )


# In[4]:


# Function to find the missing element
def getMissingNo(arr, n):
	total = (n + 1)*(n + 2)/2
	sum_of_A = sum(arr)
	return total - sum_of_A

# Driver code
if __name__ == '__main__':
	arr = [1, 2, 3, 5]
	N = len(arr)
	
	# Function call
	miss = getMissingNo(arr, N)
	print(miss)
	


# In[ ]:




