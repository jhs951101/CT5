name = input('city name : ')
str1 = ''

if name == '서울':
    str1 = name + ' : 605㎢'
elif name == '파리':
    str1 = name + ' : 105㎢'
elif name == '애든버러':
    str1 = name + ' : 264㎢'
else:
    str1 = 'Sorry'

print(str1)
