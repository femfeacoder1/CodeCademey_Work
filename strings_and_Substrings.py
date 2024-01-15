# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 12:55:16 2024

@author: Vicki C
"""
first_name = "Rodrigo"
last_name = "Villanueva"
new_account = last_name[:5]
temp_password = last_name[2:6]
print(new_account + "  " + temp_password)
###############################################
first_name1 = "Julie"
last_name1 = "Blevins"
def account_generator(first_name, last_name):
  return first_name[:3] + last_name[:3]

print(account_generator(first_name, last_name))
new_account = account_generator(first_name1, last_name1)
##############################################################
company_motto = " Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]
######################
first_name = "Bob"
fixed_first_name = "R" + first_name[-2:]
#############################
#  escape charaters
password = "theycallme\"crazy\"91"
#######################################
def letter_check(word, letter):
  for item in word:
    if item == letter:
      return True
      break
  return False
print(letter_check("lazy", "f"))
####################################################
def contains(big_string, little_string):
  return little_string in big_string

print(contains( "watermellon", "water"))
print(contains( "watermellon", "color"))
print()
####################################################
def common_letters(string_one, string_two):
  common_letters1 = []
  for item in string_one:
    if item in common_letters1:
      continue
    elif item in string_two:
      common_letters1.append(item)
  return common_letters1

print(common_letters("manhattan", "san francisco"))
print()
#########################################################
def username_generator(first_name, last_name):
  user_name = first_name[:3]+last_name[:4]
  return user_name

def password_generator(user_name):
  password = user_name[-1]+user_name[-len(user_name):-1]
  return password
##########################################################   .join .strip
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']
for item in love_maybe_lines:
    item.strip()
love_maybe_lines_stripped = ",".join(love_maybe_lines)
#love_maybe_lines_stripped.strip()
print(love_maybe_lines_stripped)
print()
################################    .strip
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_temp = []
for item in love_maybe_lines:
  if len(item.strip())>0:
    love_maybe_lines_temp.append(item.strip())
  else:
    love_maybe_lines_temp.append(",")   
print(love_maybe_lines_temp)
print()

love_maybe_lines_stripped = " ".join(love_maybe_lines_temp)
print(love_maybe_lines_stripped)

###############################   join
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n'  ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for item in love_maybe_lines:
    love_maybe_lines_stripped.append(item.strip())
print(love_maybe_lines_stripped)
print()

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(love_maybe_full)
###############################
def poem_title_card(title, poet):
  return "The poem \"{}\" is written by {}.".format(title, poet)

print(poem_title_card( "today", "vicki"))
print()

###############################################
def poem_description(publishing_date, author, title, original_work):
  poem_desc = "The poem \"{title}\" by {author} was originally published in \"{original_work}\" in {publishing_date}.".format(publishing_date=publishing_date, author=author, title=title, original_work=original_work)
  return poem_desc


my_beard_description = poem_description("1974", "Shel Silverstein", "My Beard", "Where the Sidewalk Ends")

print(my_beard_description)
print()
###########################
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
print()
#########################
highlighted_poems = "Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"
highlighted_poems_list = highlighted_poems.split(',') 
highlighted_poems_stripped = []
for item in highlighted_poems_list:
  highlighted_poems_stripped.append(item.strip())
highlighted_poems_details = []
for item in highlighted_poems_stripped:
  highlighted_poems_details.append(item.split(':'))

titles = []
poets = []
dates = []
for item in highlighted_poems_details:
  titles.append(item[0])
  poets.append(item[1])
  dates.append(item[2])

for x in range(len(titles)):
  print("The poem {} was published by {} in {}. ".format(titles[x], poets[x], dates[x]))