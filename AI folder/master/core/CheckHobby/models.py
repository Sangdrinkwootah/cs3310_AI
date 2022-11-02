f = open("hobby.txt", "r")
hobby = f.read()
f.close()

# Chech hobby food, if no add to warehouse
f = open("C:\\Users\\Admin\\Foodlist.txt", "r")
food_list = f.read()
print(food_list)
list_str = []
food_ray = food_list.split("\n")
for i in range(len(food_ray)):
    list_str += food_ray[i].split(" ")

x = list_str.count(hobby)
if x:
    print("ok")
else:
    print('not ok')