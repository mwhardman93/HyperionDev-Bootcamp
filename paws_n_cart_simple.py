menu_line = '-' * 79
MENU = f'''
Welcome to Paws n Cart!
{menu_line}
This is your online shopping cart for all your pets needs!
{menu_line}
What would you like to do today:
1:  Add item to shopping cart.
2:  View shopping cart.
3:  Remove item from shopping cart.
4:  Calculate total cost of shopping cart.
5:  Checkout.

0:  Exit.
{menu_line}'''

cart = []
prices = []
total = 0

done = False
while not done:
    print(MENU)
    menu_choice = input("Type a number for your menu choice:\n")

    if menu_choice.isnumeric() and menu_choice <= "5":

        if menu_choice == "1":
            print(menu_line)
            item = input("What would you like to add?:\t").capitalize()
            price = float(input("Enter the item price in £:\t"))
            cart.append(item)
            prices.append(price)
            print(f"{item} has been added to your cart at price £{price}.")
            print(menu_line)


        if menu_choice == "2":
            print(menu_line)
            print("This is your shopping cart:")

            end = False
            counter = 0

            if (len(cart) > 0):
                while not end:
                    if (counter == len(cart) - 1):
                        end = True

                    print(f"{cart[counter]}:\t£{prices[counter]}")
                    counter += 1
            print(menu_line)


        if menu_choice == "3":
            print(menu_line)
            remove = input("What item would you like to remove?:\t")
            remove = remove.capitalize()
            if remove in cart:
                index = cart.index(remove)
                cart.pop(index)
                prices.pop(index)
                print(f"{remove} has been removed from your cart.")
            else:
                print("Item not in cart.")
            print(menu_line)


        if menu_choice == "4":
            print(menu_line)
            print("The total cost of your shopping cart is:")

            for price in prices:
                total += price
            print(f"£{total}")
            print(menu_line)


        if menu_choice == "5":
            print(menu_line)
            print("Thank you for shopping with Paws n Cart!")
            print(f"Your cart total is £{total}, continuing to payment.")
            break


        if menu_choice == "0":
            done = True

    else:
        print(menu_line)
        print("Invalid option, please type again.")