# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 11:24:26 2024

@author: Vicki C
"""
def middle_element(my_list):
  if len(my_list) %2 > 0:     
      return my_list[(int(len(my_list)-1))/2]
  else:
      sum = my_list[(int(len(my_list)/2))] + my_list[int(len(my_list)/2-1)]
      return sum/2
                
print(middle_element( [5,2,-10,-4,4,5]))
        

        