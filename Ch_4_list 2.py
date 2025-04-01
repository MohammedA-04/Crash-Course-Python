# 4.1 Pizza
from userpath.cli import append

pizza = ['Pizza One', 'Pizza Two', 'Pizza Three']
print(pizza)

for p in pizza:
    print(p)

secondls = [1,2,3,4,5]
sum = sum(secondls)
print(sum)

# Extra Q: copy slice / separate list
new_list = pizza[:]
print("Old List: ", pizza)
print("New List not linked: ", new_list)

# 4.2: Sum a million
list = []
for i in range(1, 1_000_001):
    list.append(i)

print(f"Min {min(list)}")
print(f"Max {max(list)}")

# 4.3: Odd List
odd = []
for i in range(1,21, 2):
    odd.append(i)
print(f"Odd {odd}")

# 4.4 Multiple of 3's
three = []
for i in range(3, 33, 3):
    three.append(i)
print(f"Three {three}")

# 4.5 Cubes
count =  1
cubes = []
while count < 11:
    cubes.append(f"{count} ** 3")
    count += 1
print(f"Cube {cubes}")

# 4.6 Cube Compression
# name = [ logic for i in range(x,y)]
ls = [i**3 for i in range(1,11)]
print(ls)

# 4.10: Print 1:3, Print Middle List, Print last three
nums = [ i for i in range(1,11)]
print(f"Nums to select from: {nums}")
print(f"Nums to {nums[0:3]}")

mid = len(nums) // 2
print(f"Nums to {nums[mid-1:]}")

# 4.11: My and Your Pizza
copy = pizza[:]
pizza.append('Asian Special')
copy.append('Extra Hot Special ')
print(pizza)
print(copy)

# 4.13
tuple = ('Cucumber', 'Mango', 'Kiwi', 'Strawberry', 'Raspberry')
print(tuple)
# make reassinment
tuple = ('Cucumber', 'Burger', 'Kiwi', 'Pizza', 'Raspberry')
print(tuple)