#!/usr/local/bin/python
import yaml
import random
import os,sys
with open(r'users.yaml') as file:
    user_list = yaml.load(file, Loader=yaml.FullLoader)

combine_list=[]
random_group_a=[]

def random_list_fun(single_list):
  random_group_a=random.sample(user_list[single_list],len(user_list[single_list]))
  return(random_group_a)

def combine_random_list_fun(second_list,third_list):
  combine_list=random.sample(user_list[second_list] + user_list[third_list],len(user_list[second_list] + user_list[third_list]))
  return(combine_list)

loop=0
combine_list = combine_random_list_fun("group2","group3")

for user in random_list_fun("group1"):
  print(user,combine_list[loop])
  loop = loop + 1

group1_element=len(user_list['group1'])

###remove used element
#def remove_element(first_group,second_group):
counter = 0
while counter != group1_element:
  if combine_list[counter] in user_list["group2"]:
    user_list["group2"].remove(combine_list[counter])
  elif combine_list[counter] in user_list["group3"]:
    user_list["group3"].remove(combine_list[counter])
  counter = counter + 1

#remove_element("group2","group3")
#####
def rest_element_compare(first_list,second_list):
  loop=0
  combine_list = random_list_fun(second_list)
  for user in random_list_fun(first_list):
    print(user,combine_list[loop])
    loop = loop + 1

##checking the length of the list
if len(user_list['group2']) < len(user_list['group3']):
  print("group2 having less users",user_list['group2'])
  print(rest_element_compare("group2","group3"))
elif len(user_list['group2']) > len(user_list['group3']):
  print("group3 having less users",user_list['group3'])
  print(rest_element_compare("group3","group2"))
elif len(user_list['group2']) == len(user_list['group3']):
  print("both having same users")
  print(rest_element_compare("group2","group3"))
