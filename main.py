my_dict = {'Allan': 1988, 'Katya': 1987, 'Kristina': 2014}
print(my_dict)
print(my_dict['Allan'])
print(my_dict.get('Stefaniya'))
my_dict.update({'Nikita': 1988, 'Janna': 1958})
print(my_dict)
print(my_dict['Allan'])
del my_dict['Allan']
print(my_dict)

my_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6, 'Balalaika', False, (1, 2, 3, 4) }
print(my_set)
my_set.update({7, 'Bronevik'})
print(my_set)
print(my_set.remove('Balalaika'))
print(my_set)
