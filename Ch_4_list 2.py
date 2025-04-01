# 4.1 Pizza
# from userpath.cli import append

pizza = ['Pizza One', 'Pizza Two', 'Pizza Three']
print(pizza)

# Looping List
for p in pizza:
    print(p)

# List Sum
secondls = [1,2,3,4,5]
sum = sum(secondls)
print(sum)

# Extra Q: copy slice is a separate list
new_list = pizza[:]
print("Old List: ", pizza)
print("New List not linked: ", new_list)

# 4.2: Loop from 1 to 1 mil, return min/max()
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
count = 1
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

mid = (len(nums) // 2) - 1 # 5.0 - 1.0 to avoid off by one err
print(f"Nums to {nums[mid:]}")

# 4.11: My and Your Pizza
copy = pizza[:]
pizza.append('Asian Special')
copy.append('Extra Hot Special ')
print(pizza)
print(copy)

# 4.13 Buffet
# pt1: Loop to print each food
# pt2: Menu Change: Replace two after

print("\nTuples\n ")
foods = ('Cucumber', 'Mango', 'Kiwi')
for tup in foods:
    print(tup)

# Pt2
foods = ('Cucumber', 'Burger', 'Kiwi')
print()
for tup in foods:
    print(tup)

# Fun
tupply = (29,)
print(f"Example tupply = (20,) is valid w one element, not useful tho: {tupply}")