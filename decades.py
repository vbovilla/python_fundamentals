age  = input('How old are you?\n')
# print(age)
# decades = age / 10

decades = int(age) / 10 #float
decades = int(age) // 10 #integer
years = int(age) % 10 #remainder

# print('You are '+str(decades)+" decades old")
# print('You are',decades,"decades old")

print('You are '+str(decades)+" decades and "+str(years)+" years old")