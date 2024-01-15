# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:59:23 2023

@author: Vicki C
"""

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]
prices = [30, 25, 40, 20, 20, 35, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
for price in prices: total_price += price
average_price = total_price/len(prices)

print("Average Haircut Price:")
print(average_price)

new_prices =[price -5 for price in prices]

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += new_prices[i]*last_week[i]

print("Total Revenue new prices = ", total_revenue)
average_daily_revenue = total_revenue/7
print("Average daily revenue = ", average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if new_prices[i]<30]

print(cuts_under_30)
###################################################

def append_size(my_list):
  for i in range(len(my_list)):
    my_list.append(my_list[i])
  return my_list
### Better!!
def append_size2(my_list):
  my_list.append(len(my_list))
  return my_list3

print(append_size([23, 42, 108]))

#########################################################
def append_sum (my_list):
    print(my_list[-1] + my_list[-2])
    my_list.append(my_list[-1]+my_list[-2])
    return my_list
print(append_sum([1, 1, 2]))
########################################################
def larger_list(my_list1, my_list2):
  if len(my_list1) >len(my_list2):
     return my_list1[-1] 
  if len(my_list1) < len(my_list2):
     return my_list2[-1]   
  else:
    return "no winner"
print(larger_list([4, 10, 2, 5,7], [-10, 2, 5, 10]))

######################################
#  COUNTING NUMBER OF ITEMS IN A LIST
def more_than_n(my_list, item, n):
  if my_list.count(item) > n:
    return True
  else:
    return False
  
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 1, 3))
######################################################
#  COMBINING AND SORTING A LIST
def combine_sort(my_list1, my_list2):
  unsorted = my_list1 + my_list2
  sortedlist = sorted(unsorted)
  return sortedlist

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
##########################################
##  CREATING A LIST FROM SCRATCH

def every_three_nums2(start):
  return list(range(start, 101, 3))
  
print(every_three_nums2(91))
########################################
def exponents(bases, powers):
  newlist = []
  for index in range(len(bases)):
      newlist.append(int(bases[index])**int(powers[index]))
  return newlist

print(exponents([2, 3, 4], [1, 2, 3]))
###################################################
