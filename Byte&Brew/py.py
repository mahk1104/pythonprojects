import datetime
import json
import os

# File to store past orders
ORDERS_FILE = "past_orders.json"
STAFF_PASSWORD = "admin123"  # Set your staff password here

# Load past orders
def load_past_orders():
    if os.path.exists(ORDERS_FILE):
        with open(ORDERS_FILE, "r") as file:
            return json.load(file)
    return []

# Save order history
def save_order(order):
    past_orders = load_past_orders()
    past_orders.append(order)
    with open(ORDERS_FILE, "w") as file:
        json.dump(past_orders, file, indent=4)

# Get the current date and time
order_date = datetime.datetime.now().strftime("%d-%m-%y")
order_time = datetime.datetime.now().strftime("%H-%M-%S")

# Get customer details
first_name = input("Please enter your first name: ").strip().title()
last_name = input("Please enter your last name: ").strip().title()

# Ensure table number is a valid number
while True:
    table_number = input("Please enter your table number: ").strip()
    if table_number.isdigit():
        break
    print("Invalid table number! Please enter a number.")

print("\nWelcome to Byte and Brew Cafe!!")

# Initialize order details
total_price = 0.0
items_ordered = {}

# Menu and book list with pricing
menu_items = {
    'food': {
        'cheese sandwich': 4.85, 'cheesecake': 5.25, 'chocolate croissant': 4.50, 'muffin': 3.65,
        'cupcake': 3.90, 'carrot cake': 5.10, 'danish': 4.50, 'chicken bagel': 5.60,
        'chocolate cookie': 3.50, 'brownie': 3.50, 'steak pie': 4.70, 'caesar salad': 5.90,
        'egg and cheese flan': 5.15, 'english breakfast': 15.40, 'jam on toast': 3.00,
        'toast': 3.50, 'honey on toast': 4.50, 'cinnamon cruffin': 5.00, 'double english breakfast': 25.70
    },
    'drinks': {
        'latte': 4.50, 'english tea': 3.00, 'orange juice': 3.50, 'apple juice': 3.50,
        'mocha': 5.40, 'double mocha': 7.10, 'frappuccino': 6.00, 'macchiato': 5.50,
        'black coffee': 2.00, 'flat white': 3.00, 'chai tea': 4.50, 'cappuccino': 6.00,
        'americano': 5.50, 'espresso': 4.00, 'green tea': 4.80
    }
}

book_list = {
    'The Alchemist': 10.00, 'A Song of Ice and Fire': 15.00, 'Moby Dick': 12.00, 'Treasure Island': 16.00,
    'The Great Gatsby': 19.00, '1984': 21.00, 'The Woman in the Window': 17.00, 'The Silent Patient': 26.00,
    'Pride and Prejudice': 10.00, 'The Hobbit': 14.00, "Salem's Lot": 13.00, 'The War Horse': 9.00,
    'The Dance of Dragons': 23.00
}

# Function to display menu
def display_menu():
    print("\n*** Menu ***")
    for category, items in menu_items.items():
        print(f"\n{category.capitalize()}:")
        for item, price in items.items():
            print(f"  - {item.title()} : £{price:.2f}")
    print("\n*** Book List ***")
    for book, price in book_list.items():
        print(f"  - {book} : £{price:.2f}")

# Ask the customer if they want to see the menu
view_menu = input("Would you like to see the menu? (yes/no): ").strip().lower()
if view_menu in ['yes', 'y']:
    display_menu()

# Function to get a valid quantity from the user
def get_quantity():
    while True:
        quantity = input("How many would you like? ").strip()
        if quantity.isdigit() and int(quantity) > 0:
            return int(quantity)
        print("Invalid quantity. Please enter a positive number.")

# Function to handle ordering food and drinks
def handle_order(category):
    global total_price
    while True:
        item = input(f"What {category} would you like to order? ").lower()
        if item in menu_items[category]:
            quantity = get_quantity()
            price = menu_items[category][item]
            items_ordered[item] = items_ordered.get(item, 0) + quantity
            total_price += price * quantity
            print(f"Added {quantity} x {item.title()} : £{price * quantity:.2f} to your order. Total: £{total_price:.2f}")
        else:
            print(f"Sorry, we don't have {item}. Please choose from the menu.")
            continue
        if input("Would you like to order more? (yes/no): ").lower() not in ['yes', 'y']:
            break

# Function to handle book orders
def handle_book_order():
    global total_price
    while True:
        book = input("What book would you like to order? ").title()
        if book in book_list:
            quantity = get_quantity()
            price = book_list[book]
            items_ordered[book] = items_ordered.get(book, 0) + quantity
            total_price += price * quantity
            print(f"Added {quantity} x '{book}' : £{price * quantity:.2f} to your order. Total: £{total_price:.2f}")
        else:
            print("Sorry, we don't have that book.")
            continue
        if input("Would you like to order another book? (yes/no): ").lower() not in ['yes', 'y']:
            break

# Ask the user what they would like to order
while True:
    choice = input("\nWould you like to order food, drinks, or books? (Type your desired category or type 'done' to finish): ").lower()
    if choice == 'food':
        handle_order('food')
    elif choice == 'drinks':
        handle_order('drinks')
    elif choice == 'books':
        handle_book_order()
    elif choice == 'done':
        break
    else:
        print("Invalid choice. Please enter 'food', 'drinks', 'books', or 'done'.")

# Final Order Summary (defined before saving the order)
order_summary = {
    "Customer Name": f"{first_name} {last_name}",
    "Table Number": table_number,
    "Server": "Cafe Waiter",
    "Date": order_date,
    "Time": order_time,
    "Items Ordered": items_ordered,
    "Total Price": f"£{total_price:.2f}"
}

print("\n*** Order Summary ***")
for key, value in order_summary.items():
    print(f"{key}: {value}")

# Confirm order completion
if input("\nWould you like to complete your order? (yes/no): ").lower() in ['yes', 'y']:
    print("Thank you for your order! Enjoy your meal.")
    # Ask for staff password to view past orders
    view_past = input("\nWould you like to see past orders? (staff only) (yes/no): ").strip().lower()
    if view_past in ['yes', 'y']:
        password = input("Enter staff password: ")
        if password == STAFF_PASSWORD:
            past_orders = load_past_orders()
            print("\n*** Past Orders ***")
            # Initialize grand total accumulator
            grand_total = 0.0
            for i, order in enumerate(past_orders, start=1):
                print(f"\nOrder {i}:")
                for key, value in order.items():
                    print(f"  {key}: {value}")
                # Extract the numeric value from the 'Total Price' string (removing the currency symbol)
                total_str = order.get("Total Price", "£0.00")
                try:
                    order_total = float(total_str.replace("£", "")) 
                except ValueError:
                    order_total = 0.0
                grand_total += order_total
            print(f"\nGrand Total of All Orders: £{grand_total:.2f}")
        else:
            print("Incorrect password! Access denied.")
else:
    print("Order not completed.")

# Save the order
save_order(order_summary)
