#Zachary Blackwell 1941472
import math
# (1) Wall area calculations
wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = int(wall_width * wall_height)
print('Wall area:', wall_area, 'square feet')
#(2) Paint gallons calculations
paint_needed = wall_area / 350
print('Paint needed:', '{:.2f}'.format(paint_needed), 'gallons')
#(3) Number of gallon cans needed
cans_needed = math.ceil(paint_needed)
print('Cans needed:', cans_needed, 'can(s)')
#(4) Color of paint
print()
color_paint = input('Choose a color to paint the wall:\n')
color_price = {'red': 35, 'blue': 25, 'green': 23}
total_cost = str(color_price[color_paint] * cans_needed)
print('Cost of purchasing', color_paint, 'paint:','$' + total_cost)