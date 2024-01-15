# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 16:06:41 2024

@author: Vicki C
"""
text = "abcdefghijklmnopqrstuvwxyz"
import string
alphab1 = list(string.ascii_lowercase)
alphab2 = list(string.ascii_lowercase)
alphab = "".join(alphab1 +alphab2)

message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'

message_split = message.split()
#print(message_split)
decoded =[]

for item in message_split:
    temp_new = []
    for x in range(len(item)):
        if text.find(item[x])<0:
            temp_new.append(item[x])
        else:
            location = text.find(item[x])
            temp_new.append(alphab[location +10])
        
    new_word= "".join(temp_new)
    decoded.append(new_word)
    
decoded_final = " ".join(decoded)
print(decoded_final)
            
        