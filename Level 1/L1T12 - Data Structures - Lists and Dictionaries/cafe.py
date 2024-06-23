num_of_menu_items = int(input('Hi there! How many menu items would you like to input today?: '))

#check to make sure there are at least 4 menu items
while num_of_menu_items < 4:
    num_of_menu_items = int(input('There must be a minimum of 4 items on the menu. Please enter a new number: '))

#init lists
menu = []
price_list = []
stock_count_list = []

#gather user input and add to corresponding list
for i in range(num_of_menu_items):
    menu_items = input(f'Please enter the name for menu item {i + 1}: ')
    menu.append(menu_items)

    item_price = int(input(f'Please enter the price of menu item {menu[i]} (R): '))
    price_list.append(item_price)
    
    item_stock_count = int(input(f'Please enter the stock count for menu item {menu[i]}: '))
    stock_count_list.append(item_stock_count)

#create dictionaries using lists
stock = dict(zip(menu, stock_count_list))
price = dict(zip(menu, price_list))

#create total_stock variable and calculate the total stock value
total_stock = 0

for item in stock:
    total_stock += stock[item] * price[item]

print(f'The total stock value is: R{total_stock}')


