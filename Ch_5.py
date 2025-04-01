# Conditionals

# 5.1 Conditional Test
car = 'bmw'
print("Is car bmw?")
print(car == 'bmw')

# 5.3 to 6 Alien Colour (5.2 skipped)
a = 'green'
if a == 'green':
    print("Earned 5pts")
elif a == 'yellow':
    print("Warning")
elif a == 'read':
    print("dnager")
else:
    print("failure")

# 5.8 Admin List
ls = ['U1', 'U2', 'Admin']

if ls:
    for l in ls:
        if l == 'Admin':
            print("Greetings Admin")
        else:
            print(f"Hello {l}")