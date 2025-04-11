print("=-=-= Best Buy Retail Store =-=-=")
print("=-=-= Cashier Logged In... =-=-=")

#dictionary stores list of products
products = {
    "Product_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Product": ["Bread", "1LB of Rice", "1 Dozen Eggs", "1LB of Chicken", "Milk", "1 Dozen Bananas", "1LB of Tomatoes", "1LB of Potatoes", "1LB of of Onions", "1L of Flour"],
    "Price": [500, 150, 700, 750, 2100, 200, 200, 200, 100, 250],
    "Stock": [10, 10, 120, 50, 20, 100, 50, 50, 50, 100]
    }

#main menu display    
def main_menu():
    print("=-=-= Main Menu =-=-=")
    print("\n=-=-= What would you like to do? =-=-=")
    print("=-=-= Select Options 1 - 6 =-=-=")
    print("1. View Stock")
    print("2. Add Product")
    print("3. View Cart")
    print("4. Remove Product")
    print("5. Check Out")
    print("6. Exit")

#displays the stock available
def view_stock():
    stock = len(products["Product_ID"])
    for inventory in range(stock):
        #stores each value in a variable
        product_id = products["Product_ID"][inventory]
        product = products["Product"][inventory]
        price = products["Price"][inventory]
        stock = products["Stock"][inventory]
        print(f"Product ID:{product_id}-----{product}----- ${price}----- Stock:{stock}")

#global list to hold added purchases
cart = []

#this function allows the cashier to add products to the cart
def purchases(new_cart):
    #this loops the prompt to enter Product ID until the user breaks the loop with 'menu'
    while True:
        prod_id = (input("Enter Product ID or 'menu' to return to menu:\n"))
        #ensures the word 'menu' is accepted regardless of capitalization
        if prod_id.lower() == "menu":
            break
        try:
            product_id = int(prod_id)
            #checks if Product ID exists in product
            if product_id not in products["Product_ID"]:
                print("Invalid Product ID, Try again...")
                continue
            #once a valid Product ID is enetered it will prompt for the quantity
            elif product_id in products["Product_ID"]:
                item_index = products["Product_ID"].index(product_id)
                product = products["Product"][item_index]
                quantity = int(input("Enter Quantity:\n"))
                try:
                    #checks if the quantity requested is in stock and makes sure the amount enetered is not less than 0
                    if quantity > products["Stock"][item_index]:
                        print(f"Insufficient Stock! Only {products['Stock'][item_index]} Available...")
                        continue
                    elif quantity <= 0:
                        print("You cannot enter a quantity less than 0. Try Again...")
                        continue
                    #creates a dictionary to contain purchase details
                    added_purchases = {"Product_ID": product_id, "Product": product, "Quantity": quantity, "Price": products["Price"][item_index]}
                    #added_purchases dictionary gets appened to new_cart list
                    new_cart.append(added_purchases)
                    print(f"{quantity} X {product} has been added to your cart!")
                except ValueError:
                        print("Stock not Available! Please Try Again...")
        except ValueError:
            print("Invalid Product ID! Please Try Again...")
    return new_cart

#this function displays what is currently in the cart
def view_cart(cart_items):
    #checks if cart_items is empty
    if not cart_items:
        print("Cart is Empty...")
        return
    item_total = 0
    #iterates through the item dictionary in the cart_items list and prints the information
    for item in cart_items:
        print(f"Product ID: {item['Product_ID']}-----{item['Product']}-----Quantity: {item['Quantity']}-----Price: ${item['Price']}")
        #calculates the total of the items and prints it
        item_total += item["Price"] * item["Quantity"]
    print(f"=-=-= Item Total: ${item_total} =-=-=")
    return item_total

#this function displays the cart and promts the user for what they want to remove   
def remove_product(new_cart):
    #checks if new_cart is empty
    if not new_cart:
        print("Cart is Empty...")
        return
    #loops the prompt for the Product ID of the itme the user wants to remove
    while True:
        view_cart(new_cart)
        remove_id = input("Enter the Product ID of the item your want to remove or 'menu' to return to menu:\n")
        if remove_id.lower() == "menu":
            break
        id_removal = int(remove_id)
        try:
            for index, item in enumerate(new_cart):
                #once the Product ID entered matches what the user entered the item will be removed
                if item["Product_ID"] == id_removal:
                    del new_cart[index]
                    print("Item has been removed...")
                    break
                else:
                    print("No matching Product ID currently in cart...")
        except ValueError:
            print("Invalid Product ID...Try Again.")
    return new_cart

#calculates the cart and prints the receipt    
def check_out(cart_items):
    #checks if cart is empty
    if not cart_items:
        print("Cart is Empty...")
        return
    subtotal = 0
    #calculates the item_total and adds it to the subtotal and prints it
    for item in cart_items:
        price = item["Price"]
        quantity = item["Quantity"]
        item_total = price * quantity
        subtotal += item_total
        print(f"{item['Product']} x {quantity} = ${item_total}")
        print(f"Subtotal: ${subtotal}")
    discount = 0
    #calculates 5% discount on subtotal over $5000 and prints the discounted subtotal
    if subtotal >= 5000:
        five_discount = subtotal * 5/100
        print(f"Discount of 5%: ${five_discount}")
        subtotal -= five_discount
    else:
        print("No discount earned.")
    #calculates tax on subtotal after discount and adds it to get the final total due
    tax = subtotal * 10/100
    print(f"Tax of 10%: ${tax}")
    total = subtotal + tax
    print(f"Total Amount Due: ${total}")
    #loop to accept and handle payment
    while True:
        try:
            payment = float(input("Enter Payment:\n$"))
            if payment >= total:
                change = payment - total
                print("Payment Successful")
                print(f"Change: ${change}")
                #clears cart for new purchses to be added
                cart.clear()
                break
            else:
                print("Insufficient Funds...Try Again.")
        except ValueError:
            print("Invalid payment amount...")

#loops the main_menu function and ask for the users choice, will exit once option 6 is picked
while True:
    main_menu()
    option = input()
    if option == "1":
        print("\n=-=-=-=-=-=-=-=-=-=-= Products Available =-=-=-=-=-=-=-=-=-=-=")
        view_stock()
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif option == "2":
        print("\n=-=-= Add a Product =-=-=")
        cart = purchases(cart)
    elif option == "3":
        print("\n=-=-=-=-=-=-=-=-=-=-= Customer's Cart =-=-=-=-=-=-=-=-=-=-=")
        view_cart(cart)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif option == "4":
        print("\n=-=-=-=-=-=-=-=-=-=-= Remove a Product =-=-=-=-=-=-=-=-=-=-=")
        remove_product(cart)
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif option == "5":
        print("\n=-=-=-=-=-= Receipt =-=-=-=-=-=")
        print("=-=-= Best Buy Retail Store =-=-=")
        check_out(cart)
        print("=-=-= Thank You for Shopping!!! =-=-=")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    elif option == "6":
        print("=-=-= Cashier Logged Out... =-=-=")
        break
    else:
        print("Invalid Input...")