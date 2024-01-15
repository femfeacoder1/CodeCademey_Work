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


###############################

name = "todd"
question = ""
if name == "" and not question == "":
  print (" Question:  " + question)
elif question == "" :
  print(" please add a question to the variable")
else:
  print(name + " asks  :" + question )