# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:24:32 2023

@author: Vicki C
"""
# Your code below:
single_digits = list(range(0,10))
squares = []
for numb in single_digits: 
  print(numb)
  squares.append(numb**2)
  
print(squares)

cubes = []
for numb in single_digits: cubes.append(numb**3)
print(cubes)

###########################################
def larger_sum(lst1,lst2):
  sum1 = 0 
  sum2 = 0
  for item in lst1: sum1 += item 
  for item in lst2: sum2 += item
  if sum1 >= sum2:
    return lst1
  else:
    return lst2 

print(larger_sum([1, 9, 5], [2, 3, 7]))
###########################################
a = 2
b = 330
print("A") if a > b else print("B")

###########################################
def over_nine_thousand(lst):
  sums = 0
  for item in lst: 
    if (sums + item <=9000):
        sums += item 
    else:
        break
  return sums

print(over_nine_thousand([8000, 900, 120, 5000]))
###########################################
def max_num(nums):
  maxm = nums[0]
  for item in nums:
    if item > maxm:
      maxm = item
  return maxm 
###########################################
def same_values(lst1, lst2):
  equals = []
  for x in range(0, len(lst1)):
    if lst1[x] == lst2[x]:
        equals.append(x) 
  return equals
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
###########################################
def reversed_list(lst1, lst2):
  for x in range(0,len(lst1)):
    if lst1[x]!=lst2[len(lst1)-1-x]:
      return False 
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))

