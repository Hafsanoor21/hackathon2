# 8.Cafe Menu Price Lookup.
# create the dictionary.
menu_prices = {
    "coffee":2.50 ,
    "muffin":3.00 ,
    "sandwich":2.75
}

# Show the items, then ask the user to pick one.
print("Available items: Coffee, Sandwich, Muffin")
user_choice = input("Choose an item: ")

# use item dictionary key and print its price.
price = menu_prices[user_choice]
print("the price is:",price)

# update the prices and print the dictionary.
menu_prices ["muffin"]=12.7
print(menu_prices)

