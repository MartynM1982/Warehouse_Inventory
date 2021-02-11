# inventory is a list of items found in the warehouse.
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

# Number of items the warehouse contains.
inventory_len = (len(inventory))

# Selecting the first item in inventory.
first = inventory[1]

# Selecting the last item in inventory.
last = inventory[-1]

# Selecting inventory items at index 2 and up to, but not including index 6.
inventory_2_6 = inventory[2:6]

# Selecting the first 3 items in the inventory.
first_3 = inventory[0:3]

# Calculating the number of 'twin bed' in the inventory.
twin_beds = inventory.count('twin bed')

# Inventory sorted alphabetically
inventory.sort()
