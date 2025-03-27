# Variables and Usage

url = 'https://nostarch.com'
print(f"Was {url} now is: {url.removeprefix('https://')}")

# name_cases.py
# 2.3: PM var with formatted string
name = "Eric"
print(f"Hi {name}, we learning python!")

# 2.4 Print name in upper/lower/title case
print(f"Hi {name.upper()}, we learning python!")
print(f"Hi {name.lower()}, we learning python!")
print(f"Hi {name.title()}, we learning python!")

# 2.5 Famous quote
quote = "Verily after hardship comes ease, 'says God'"
print(quote)

# 2.6 Ignored

# 2.7 Stripping Names
name = " Eric "
print(f"{name.rstrip()}")
print(f"{name.lstrip()}")
print(f"{name.strip()}")

# 2.8 File .ext
filename = "notes.txt"
print(f"Was {filename} now is {filename.removesuffix('.txt')}")

# (division only) Int to Float -> always float
print(4/2)

# underscore assignment
salary = 1_000_000
print(salary)

# 2.8: four ops on each line should amount to 8
print(f"5 + 3 = {5+3}")
print(f"2 * 4 = {2*4}")
print(f"80 / 10 = {80/10}")
print(f"18 - 10 = {18-10}")
