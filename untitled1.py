# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:24:41 2024

@author: Vicki C
"""

def letter_check(word, letter):
  for item in word:
    if item == letter:
      return True
      break
  return False
print(letter_check("lazy", "f"))