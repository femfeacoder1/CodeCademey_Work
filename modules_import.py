# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 19:24:31 2024
"""
from datetime import datetime
current_time = datetime.now()
birthday = datetime(1965, 10, 15 , 4, 35)
print(birthday)
print(datetime.now() - datetime(1984, 2, 15))

print("day is", birthday.day)
parsed_date = datetime.strptime('Jan 15, 2024', %b %d, %Y)
######################################## random.randint, random.choice
"""import random:
random_list = []
for x in range(1,101):
  random_list.append(random.randint(1,100))
print(random_list, len(random_list))
print()
# Create randomer_number below:
randomer_number = random.choice(random_list)
print(randomer_number)
##########################################
from matplotlib import pyplot as plt
import codecademylib3_seaborn
import random
numbers_a = range(1,13)
print(numbers_a)
numbers_b = random.sample(numbers_a,12)
print(numbers_b)
plt.plot(numbers_a, numbers_b)
plt.show()
"""