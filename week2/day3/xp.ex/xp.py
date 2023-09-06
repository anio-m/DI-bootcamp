# 🌟 Exercise 1 :

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# allage = zip(keys, values)
# print(list(allage))

# 🌟 Exercise 2 :

# name_person = input("excuse me sir what your name please ?").split()
# ages = input("excuse me sir what your age please ?").split()
# zip_family = zip(name_person, ages)
# family = dict(zip_family)
# print(family)

# # family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# price = 0
# for name, age in family.items():
#     if int(age) <3 :
#         print(f"{name} your ticke is free")
#     elif  3< int(age) <=12 :
#        print(f"{name} yor price ticket is 10$")
#        price += 10
#     elif int(age) > 12 :
#        print(f"{name} the price your tiket is 15$")
#        price += 15
# print(price) 


# 🌟 Exercise 3 :
zara = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ('pink', 'green')}
}

# zara['number_stores'] =2
# zara['type_of_clothes']=print("'men', 'women', 'children', 'home'")
# zara.update( {'spain' : 49} )
# if 'international_competitors' in zara:
#  zara['international_competitors'].append('Desigual')
#  print(zara['international_competitors'] )
# del zara['creation_date']
# print(zara['international_competitors'])
        
        



