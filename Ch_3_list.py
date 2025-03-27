# Lists in python

# 3.1 Names
names = ['mo', 'shaf', 'semab']
print(names)
print(names[0])
print(names[1])
print(names[2])

# 3.2 Greetings
msg = "hey there"
print(f"{msg}, {names[0]}")
print(f"{msg}, {names[1]}")

# 3.3 Own List
cars = ['bugatti', 'lambo', 'porshce']
print(f"I would like to own a {cars[0]}")

# Ops on lists elements
# 3.4 to 3.7 Custom Guest List
guest = ['G1', 'G2', 'G3']
guest.append('G4') # add one
print(guest)

guest.insert(0, 'G0') # insert one at 0
print(guest)

# pop one (LIFO)
print(f"Last one in: {guest.pop()}")

# del pos 1
del guest[1]
print(guest)

# 3.8 See the world: think of 5 places
places = ['Rome','Paris','London','Madrid','Lisbon']
print(places)
print(sorted(places)) # temp sorting not permanent
print(f"{places}\n")

print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse() # change again
print(places)

places.sort()
print(places)
places.sort() # sort again
print(places)

# 3.9 Dinner
print(f"Dinner Guests Total {len(guest)}")

# 3.10 .11 ignored
# Off-by-error avoid
print()
n = len(places)
n = n - 1
print(n)
print(places)
print(places[n])