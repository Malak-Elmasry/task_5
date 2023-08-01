# 1
name = input('Your name:')
print('"Name: ' + name + '"')

age = input('Your age:')
print("Age: " + age)

# 2
street = input('Your street:')
city = input('your city:')
country = input('Your country:')
address = street + ", " + city + ", " + country
print('"Address: ' + address + '"')

# 3
welcome = 'Hello {' + name + '} ' + 'Your age is ' + age + ' years old, ' + 'Your address is ' + address
print(welcome)

# 4
print(type(name), type(age))
print(type(street), type(city))
print("      ", type(country))

# 5
welcome2 = f'''"Hello :{name} ,How Are You? \ """ Your Age Is :"{age}""
 + And Your Country Is :{country}'''
print(welcome2)


# 6
welcome3 = f'''"Hello :{name} ,How Are You? \ 
""" Your Age Is :"{age}""+ And 
Your City Is :{city}'''
print(welcome3)

# 7
name2 = 'Doaa  Reem'
print('First latter is', name2[0])
print('Third latter is', name2[2])
print('Last latter is', name2[-1])

# 8
print(name2[7:])
print(name2[0:4])
print(name2[2:-2:1])
print(name2[-1:-5:-1])
print(name2[0:-1:2])

# 9
name3 = "$&$&Mohammed$&$&"
print(name3.strip('$&'))

# 10
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7', 'love'))

# 11
name4 = 'malak elmasry'
print(name4.title())
print(name4.capitalize())

title = 'free palestine'
print(title.title())
print(title.capitalize())

# 12
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print('000' + num1)
print('00' + num2)
print('00' + num3)
print('0' + num4)
print(num6)

# 13
first_name = "Malak"
print(11*'*', first_name)
print(11*'*', first_name, 11*'*')
print(first_name, 11*'*')

# 14
name_one = "HaLA"
name_two = "shaHD"
name_one1=name_one.lower()
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())

# 15
print(name_one.islower())
print(name_two.isupper())

# 16
print(name_one.startswith('S'))
print(name_two.endswith('HD'))

# 17
msg = "I Love Python And Although I Love GSG with Zakaria"
print('Number of <Love> is:', msg.count('Love'))
print('Number of <t> is:', msg.count('t'))

# 18
name3 = "Zakaria"
print(name3.index('r'))

# 19
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace('%7', 'Love', 1))
