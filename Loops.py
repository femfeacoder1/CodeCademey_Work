# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:48:55 2024

@author: Vicki C
"""
def divisible_by_ten(nums):
  counter=0
  for item in nums:
    if item %10 == 0:
      counter +=1
  return(counter)
#U
print(divisible_by_ten([20, 25, 30, 35, 40]))
#######################################################
def add_greetings(names):
  greetings = []
  for item in names:
    greetings.append("Hello, "+ item)
  return greetings

#Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

#########################################################
def delete_starting_evens(my_list):
 while (len(my_list) > 0 and my_list[0] % 2 == 0):
    my_list = my_list[1:]

 return my_list
      
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))