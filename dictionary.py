
# acronyms = {
#     'LOL': 'laugh out loud',
#     'IDK': "I don't know",
#     'TBH': 'to be honest'
# }

# print(acronyms)
# print(acronyms['LOL'])
# print(acronyms.get('LOL'))


menus = [
    ['Egg Sandwich', 'Bagel', 'Coffe'],
    ['BLT', 'PB&J', 'Turkey Sandwich'],
    ['Soup', 'Salad', 'Spaghetti', 'Taco']
]


print(menus[0])
# print(menus[1])
# print(menus[2])

print(menus[0][1])


menus = {
    'Breakfat': ['Egg Sandwich', 'Bagel', 'Coffe'],
    'Lunch': ['BLT', 'PB&J', 'Turkey Sandwich'],
    'Dinner': ['Soup', 'Salad', 'Spaghetti', 'Taco']
}

print('Breakfast menu:\t', menus['Breakfat'])
print('Lunch menu:\t', menus['Lunch'])
print('Dinner menu:\t', menus['Dinner'])

# loops through keys only
for menu in menus:
    print(menu)

# loops through keys and values
for name, menu in menus.items():
    print(name, ':', menu)


person = {
    'name': 'Vishnu Vardhan',
    'city': 'Hyderabad',
    'age': 38
}
print(person)
