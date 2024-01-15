# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 14:42:09 2023

@author: Vicki C
"""

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
c=3*10**8
train_distance = 100
bomb_mass = 1

# Write your code below: 
def f_to_c(f_temp):
  c_temp = round((f_temp-32)*5/9,1)
  return c_temp
f100_in_celsius = f_to_c(100)
print("100 F =" + str(f100_in_celsius))

def c_to_f(c_temp):
  f_temp = round((c_temp*9/5 + 32),2)
  return f_temp
c0_in_fahrenheit = c_to_f(0)
print("0 C =" + str(c0_in_fahrenheit))

def get_force(mass, acceleration):
  return mass*acceleration
train_force = get_force(train_mass,train_acceleration)
print("The GE train supplies " + str(train_force) + " Newtons of force.")

def get_energy(mass, C):
  return mass*C**2
bomb_energy = get_energy(bomb_mass,c)
print("A 1kg bomb supplies "+ str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
  return get_force(mass, acceleration)*distance
train_work = get_work(train_mass, train_acceleration, train_distance)

print("The GE train does " + str(train_work)+ " Joules of work over "+ str(train_distance) + " meters.")

  


