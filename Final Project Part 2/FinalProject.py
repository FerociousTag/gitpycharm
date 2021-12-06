# Zachary Blackwell 1941472
import csv
from datetime import datetime

# Initializing empty dictionary
Inventory = {}
csv_files = ['ManufacturerList.csv', 'ServiceDatesList.csv', 'PriceList.csv']
# Loop to read each csv file
for filename in csv_files:
        with open(filename, mode='r') as file:
                reader = csv.reader(file)
                for line in reader:
                        id = line[0]
                        if filename == csv_files[0]:
                                Inventory[id] = {}
                                Inventory[id]['id'] = id
                                Inventory[id]['brand'] = line[1]
                                Inventory[id]['item_type'] = line[2]
                                Inventory[id]['condition'] = line[3]
                        elif filename == csv_files[1]:
                                Inventory[id]['service_date'] = line[1]
                        elif filename == csv_files[2]:
                                Inventory[id]['price'] = line[1]
# Write full inventory csv file
with open('FullInventory.csv', 'w') as file:
        keys = sorted(Inventory.keys(), key= lambda x: Inventory[x]['brand'])
        # Loop that goes through each item id within the sorted inventory items
        for key in keys:
                file.write(Inventory[key]['id'] + ',' +
                           Inventory[key]['brand'] + ',' +
                           Inventory[key]['item_type'] + ',' +
                           Inventory[key]['price'] + ',' +
                           Inventory[key]['service_date'] + ',' +
                           Inventory[key]['condition'] + '\n')

# Filters items based on damaged condition
filtered_dictionary = {k:v for (k,v) in Inventory.items() if Inventory[k]['condition'] == 'damaged'}

# Write damaged inventory csv file
with open('DamagedInventory.csv', 'w') as file:
        #filters price highest to lowest
        keys = sorted(filtered_dictionary.keys(), key= lambda x: filtered_dictionary[x]['price'], reverse = True)
        for key in keys:
                file.write(Inventory[key]['id'] + ',' +
                           Inventory[key]['brand'] + ',' +
                           Inventory[key]['item_type'] + ',' +
                           Inventory[key]['price'] + ',' +
                           Inventory[key]['service_date'] + '\n')

# Converts current date into a specific format and string
today = datetime.today().strftime('%m/%d/%Y')

# Converts the string today back into a date in order to compare it to the service dates
current_date = datetime.strptime(today, '%m/%d/%Y')
# filters the items that have already been serviced compared to current date
filtered_dictionary_date = {k:v for (k,v) in Inventory.items() if datetime.strptime(Inventory[k]['service_date'],'%m/%d/%Y') < current_date}

# write service date csv files that have passed
with open('PastServiceDateInventory.csv', 'w') as file:
        keys = sorted(filtered_dictionary_date.keys(), key= lambda x: filtered_dictionary_date[x]['service_date'])
        for key in keys:
                file.write(Inventory[key]['id'] + ',' +
                           Inventory[key]['brand'] + ',' +
                           Inventory[key]['item_type'] + ',' +
                           Inventory[key]['price'] + ',' +
                           Inventory[key]['service_date'] + ',' +
                           Inventory[key]['condition'] + '\n')



# Creates list that we will use to hold each item type
items_lists = []
# Sorts all of the item types
keys = sorted(Inventory.keys(), key=lambda x: Inventory[x]['item_type'])
for key in keys:
        items_lists.append(Inventory[key]['item_type'])
# Removes the duplicate entries from the list
items_lists = list(dict.fromkeys(items_lists))





# Loop that creates a file for each item type
for item_type in items_lists:
        # Creates the file name fore each file type csv
        item_type_file_name = item_type.capitalize() + 'Inventory.csv'
        # Filters the items by the item type
        filtered_dictionary_item = {k: v for (k, v) in Inventory.items() if Inventory[k]['item_type'] == item_type}
        with open(item_type_file_name, 'w') as file:
                # Sorts the items by their 'id'
                keys = sorted(filtered_dictionary_item.keys(), key=lambda x: filtered_dictionary_item[x]['id'])
                for key in keys:
                        file.write(Inventory[key]['id'] + ',' +
                                Inventory[key]['brand'] + ',' +
                                Inventory[key]['price'] + ',' +
                                Inventory[key]['service_date'] + ',' +
                                Inventory[key]['condition'] + '\n')



types_list = []
brand_list = []
#this loop looks for every brand and item type and adds them to their lists if they are not already in them
for item in Inventory:
        brand = Inventory[item]['brand']
        type = Inventory[item]['item_type']
        if brand not in brand_list:
               brand_list.append(brand)
        if type not in types_list:
                types_list.append(type)


user_search = None
#this allows the user to quit the program with 'q'
while user_search != 'q':
        user_search = input("Enter an item manufacturer and item type or enter 'q' to quit :\n")
        if user_search == 'q':
                break
        else:
                selected_brand = None
                selected_type = None
                user_search = user_search.split()
                incorrect_input = False
                #loops that looks for word in list of brands and then looks for the type if it is in the inventory
                for word in user_search:
                        if word in brand_list:
                                if selected_brand:
                                        incorrect_input = True
                                else:
                                        selected_brand = word
                        elif word in types_list:
                                if selected_type:
                                        incorrect_input = True
                                else:
                                        selected_type = word

                if (not selected_brand) or (incorrect_input) or (not selected_type):
                        print("No such item in inventory")
                else:
                        keys = sorted(Inventory.keys(), key=lambda x: Inventory[x]['price'], reverse=True)

                        similar_items = {}
                        matched_item = {}
                        matched = False
                        for id in keys:
                                if Inventory[id]['item_type'] == selected_type:
                                        today = datetime.now().date()
                                        service_date = datetime.strptime(Inventory[id]['service_date'], "%m/%d/%Y").date()
                                        isExpired = service_date < today
                                        if Inventory[id]['brand'] == selected_brand:
                                                #Loop that looks if the item is expired, damaged, if its already been matched
                                                if (not matched) and (not isExpired) and (not Inventory[id]['condition']):
                                                        matched_item = Inventory[id]
                                                        matched_item['id'] = id
                                                        matched = True
                                        else:
                                                if (not isExpired) and (not Inventory[id]['condition']):
                                                        similar_items[id] = Inventory[id]
                        if matched_item:
                                print("Your item is: " +
                                        matched_item['id'] + ',' +
                                        matched_item['brand'] + ',' +
                                        matched_item['item_type'] + ',' +
                                        matched_item['price'] + '\n')
                                if similar_items:
                                        price = matched_item['price']
                                        closest_id = None
                                        price_difference = None
                                        #This finds the similar item with the closest price to what the user searches
                                        for id in similar_items:
                                                if (closest_id == None):
                                                        closest_id = id
                                                        price_difference = abs(int(price) - int(similar_items[id]['price']))
                                                elif price_difference > abs(int(price) - int(similar_items[id]['price'])):
                                                        closest_id = id
                                                        price_difference = abs(int(price) - int(similar_items[id]['price']))
                                        print("You may, also, consider: " +
                                              similar_items[closest_id]['id'] + ',' +
                                              similar_items[closest_id]['brand'] + ',' +
                                              similar_items[closest_id]['item_type'] + ',' +
                                              similar_items[closest_id]['price'] + '\n')
                        else:
                                print("No such item in inventory")
