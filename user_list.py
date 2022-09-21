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
  if user in user_list["group2"]:
    user_list["group1"].remove(user)
  if combine_list[loop] in user_list["group3"]:
    user_list["group3"].remove(combine_list[loop])
  if combine_list[loop] in user_list["group2"]:
    user_list["group2"].remove(combine_list[loop])
  loop = loop + 1

#####
def rest_element_compare(first_list,second_list):
  loop=0
  combine_list = random_list_fun(second_list)
  for user in random_list_fun(first_list):
    print("data",user,combine_list[loop])
    if user in user_list["group2"]:
      user_list["group2"].remove(user)
    if combine_list[loop] in user_list["group3"]:
      user_list["group3"].remove(combine_list[loop])
    loop = loop + 1

def randon_pair_with_rest_element(list_name):
  # print(user_list[list_name])
  loop=0
  while len(user_list[list_name]) > 2:
  #for user in user_list[list_name]:
    print(user_list[list_name][0],user_list[list_name][1])
    user_list[list_name].remove(user_list[list_name][0])
    user_list[list_name].remove(user_list[list_name][0])
    #loop = loop + 1
  print(user_list[list_name])
  if len(user_list[list_name]) == 2:
    print(user_list[list_name][0],user_list[list_name][1])
    user_list[list_name].remove(user_list[list_name][0])
    user_list[list_name].remove(user_list[list_name][0])
  elif len(user_list[list_name]) == 1:
    print(user_list[list_name][0],user_list[list_name][1])
    user_list[list_name].remove(user_list[list_name][0])
  elif len(user_list[list_name]) == 3:
    print(user_list[list_name][0],user_list[list_name][1],user_list[list_name][2])
    user_list[list_name].remove(user_list[list_name][0])
    user_list[list_name].remove(user_list[list_name][0])
    user_list[list_name].remove(user_list[list_name][0])

##checking the length of the list
if len(user_list['group2']) < len(user_list['group3']):
  print("group2 having less users",user_list['group2'])
  print("group3 having less users",user_list['group3'])
  print(rest_element_compare("group2","group3"))
  #print(user_list["group3"])
  randon_pair_with_rest_element("group3")
elif len(user_list['group2']) > len(user_list['group3']):
  print("group3 having less users",user_list['group3'])
  print("group2 having less users",user_list['group2'])
  print(rest_element_compare("group3","group2"))
  #print(user_list["group2"])
  randon_pair_with_rest_element("group2")
elif len(user_list['group2']) == len(user_list['group3']):
  print("both having same users")
  print(rest_element_compare("group2","group3"))
