print('Welcome to the Python Coffee Shop!')

# Prices
price_coffee = 3.50
price_latte = 4.00
price_mocha = 4.50

# Get customer name
customer_name = input('What is your name? ')
print('Hello, ' + customer_name + '! Let\'s order some coffee.')

# Ask if student
student_status = input("Are you a student? (yes/no): ").lower()
is_student = (student_status == "yes")

# Loop for multiple orders
total_bill = 0.0
while True:
    print("\nMenu:")
    print("Coffee: $" + str(price_coffee))
    print("Latte: $" + str(price_latte))
    print("Mocha: $" + str(price_mocha))

    choice = input("What would you like to order? (coffee/latte/mocha): ").lower()

    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "mocha":
        cost = price_mocha
    else:
        print("Sorry, we do not have that.")
        cost = 0

    if cost > 0:
        quantity = int(input("How many cups would you like? "))
        order_cost = cost * quantity

        if quantity > 1:
            print("You get a discount of $1.00!")
            order_cost -= 1.00

        total_bill += order_cost
        print("Subtotal for this order: $" + "{:.2f}".format(order_cost))

    # Ask if they want another order
    another = input("Would you like to order something else? (yes/no): ").lower()
    if another == "no":
        break

# Apply student discount
if is_student:
    print("\nYou are eligible for a 10% student discount!")
    total_bill *= 0.90

# Final bill
print("\nYour total is: $" + "{:.2f}".format(total_bill))
print("Thank you, " + customer_name + "! Please come again.")
