# Dictionaries

# Custom 6.1/2
dict = {
    'age' : 20,
    'name': 'Mohammed',
    'course': 'Comp Sci',
    'year': 3
}

print(dict['age'])
print(dict['age'] == 20)
print(f"dict.get(self, errMsg): -> dict.get('age', 'not found') -> returns {dict.get('age', 'not found')}\n")

# deletion of year
del dict['year']
print(dict)

# empty dictionary
newD = {}
ls = ['one', 'two', 'three', 'four', 'five']

for i in range(5):
    newD[ls[i]] = i + 1

# i iters 0 to 4 so it can index list at index 0 onwards
print(newD)


# item pairing loop
for k, v in dict.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")
print()

# key only loop
for k in dict.keys():
    print(f"Key: {k.title()}")
print()

# tmp sorted(key) loop
for n in sorted(dict.keys()):
    print(n.title())
print()

# value only loop
for n in dict.values():
    print(n)

# avoiding dupes in values
dict['name2'] = 'Mohammed'
print(f"{dict}\n")

for n in set(dict.values()):
    print(n)
print()

# list of dict(k,v)
d1 = {'clr': 'red', 'pts': 5}
d2 = {'clr': 'blue', 'pts': 10}
both = [d1,d2]

for d in both:
    print(d)
print()

# using range
a = []
for a_num in range(30):
    new_alien = {'clr': 'red', 'pts': 5}
    a.append(new_alien)
print()

for i in a[:5]:
    print(i)
print(len(a))


# list in a dict
dict = {
    'age' : 20,
    'name': ['mohammed', 'ahmed'],
    'course': 'Comp Sci',
    'year': 3
}
print(f"Full name {dict['name']}")

# dict in dict
dict = {
    'p1':{
        'age': 20,
        'name': ['mohammed', 'ahmed'],
        'course': 'Comp Sci',
        'year': 3
    },

    'p2':{
        'age': 9,
        'name': ['Ahmed', 'jr'],
        'course': 'junior school',
        'year': 4
    }
}
print()

for user, user_info in dict.items():
    print(f"User {user}")
    full_name = f"{user_info['name']}"
    age = f"{user_info['age']}"

    print(f"Full Name: {full_name}")
    print(f"age: {age}\n")