#zachary blackwell 1941472

class FoodItem:
    def __init__(self, item_name = 'None', item_fat = 0.0, item_carbs = 0.0, item_protein = 0.0):
        self.name = item_name
        self.fat = item_fat
        self.carbs = item_carbs
        self.protein = item_protein


    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;

        return calories

    def display_calories(self, calories):
        format_servings = '{:.2f}'.format(num_servings)
        format_calories = '{:.2f}'.format(calories)
        print('Number of calories for', format_servings, 'serving(s):', format_calories)

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
if __name__ == "__main__":
    #User item info
    item = FoodItem()

    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    num_servings = float(input())

    item.name = name
    item.fat = fat
    item.carbs = carbs
    item.protein = protein

    #blank default value
    none_Item = FoodItem()
    none_Item_display = none_Item.print_info()


    #blank calories display
    none_item_calors = none_Item.get_calories(num_servings)
    none_itemDisplay = none_Item.display_calories(none_item_calors)
    print()

    item_info = item.print_info()

    #calories display
    item_calors = item.get_calories(num_servings)
    itemDisplay = item.display_calories(item_calors)



