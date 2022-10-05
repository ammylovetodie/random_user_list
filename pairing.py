import sys,random,json

default_created_list = ""
with open('ssondh.json', 'r') as file:
  default_created_list = json.load(file)

last_created_list = ""
with open('last_created_pairs.json', 'r') as file:
  last_created_list = json.load(file)

random.shuffle(default_created_list)

list_len=len(default_created_list)
start_num=0
pairs = {}

new_created_pair_list = []
while len(default_created_list) > 1:
  first_element = int(list(default_created_list[start_num].values())[0])
  second_element = int(list(default_created_list[start_num + 1].values())[0])
  compare_sum = first_element + second_element
  if compare_sum not in last_created_list:
    pairs[list(default_created_list[start_num].keys())[0]] = list(default_created_list[start_num + 1].keys())[0]
    new_created_pair_list.append(compare_sum)
    default_created_list.remove(default_created_list[start_num])
    default_created_list.remove(default_created_list[start_num])
  else:
    random.shuffle(default_created_list)

print(last_created_list)
for i,j in pairs.items():
    print(i,j)
print(new_created_pair_list)

with open('last_created_pairs.json', 'w') as file:
  json.dump(new_created_pair_list, file)
