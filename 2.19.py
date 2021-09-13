#Zachary Blackwell 1941472
import math

# user inputs amount
lemon_juice = float(input('Enter amount of lemon juice (in cups):'))
print()
water = float(input('Enter amount of water (in cups):'))
print()
agave_nectar = float(input('Enter amount of agave nectar (in cups):'))
print()
servings = float(input('How many servings does this make?'))
print()
print()

# ingredients
format_servings = ("{:.2f}".format(servings))
format_lemon_juice = ("{:.2f}".format(lemon_juice))
format_water = ("{:.2f}".format(water))
format_agave_nectar = ("{:.2f}".format(agave_nectar))
print('Lemonade ingredients - yields', format_servings, 'servings')
print(format_lemon_juice, 'cup(s) lemon juice')
print(format_water, 'cup(s) water')
print(format_agave_nectar, 'cup(s) agave nectar\n')
# adjust serving size
adjusted_servings = float(input('How many servings would you like to make?'))
print()
print()
format_servings = ("{:.2f}".format(adjusted_servings))
format_lemon_juice = ("{:.2f}".format(lemon_juice * (adjusted_servings / servings)))
format_water = ("{:.2f}".format(water * (adjusted_servings / servings)))
format_agave_nectar = ("{:.2f}".format(agave_nectar * (adjusted_servings / servings)))
print('Lemonade ingredients - yields', format_servings, 'servings')
print(format_lemon_juice, 'cup(s) lemon juice')
print(format_water, 'cup(s) water')
print(format_agave_nectar, 'cup(s) agave nectar\n')

# convert to gallons
format_servings = ("{:.2f}".format(adjusted_servings))
cups_to_gallons = 16
format_lemon_juice = ("{:.2f}".format((lemon_juice * (adjusted_servings / servings)) / 16))
format_water = ("{:.2f}".format((water * (adjusted_servings / servings)) / 16))
format_agave_nectar = ("{:.2f}".format((agave_nectar * (adjusted_servings / servings)) / 16))
print('Lemonade ingredients - yields', format_servings, 'servings')
print(format_lemon_juice, 'gallon(s) lemon juice')
print(format_water, 'gallon(s) water')
print(format_agave_nectar, 'gallon(s) agave nectar')





