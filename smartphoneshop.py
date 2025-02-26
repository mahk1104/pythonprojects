# Smartphone prices
phone_prices = {"basic": 250, "standard": 450, "superior": 950}
# Setup options
setup_options = {"A": 30, "B": 50}
# VAT rate
vat_rate = 0.20

# Function to get valid quantity input
def get_quantity():
    while True:
        quantity = input("Enter quantity of smartphones (must be multiple of 5, between 5 and 100): ")
        if quantity.isdigit() and 5 <= int(quantity) <= 100 and int(quantity) % 5 == 0:
            return int(quantity)
        else:
            print("Invalid input. Quantity must be between 5 and 100 and a multiple of 5.")

# Function to get valid phone type input
def get_phone_type():
    while True:
        phone_type = input("Enter smartphone type (basic/standard/superior): ").lower()
        if phone_type in phone_prices:
            return phone_type
        else:
            print("Invalid phone type. Please choose from basic, standard, or superior.")

# Function to get valid setup option input
def get_setup_option():
    while True:
        setup_option = input("Enter setup option (A/B): ").upper()
        if setup_option in setup_options:
            return setup_option
        else:
            print("Invalid setup option. Please choose A or B.")

# Function to calculate total cost
def calculate_total_cost(quantity, phone_type, setup_option):
    phone_cost = phone_prices[phone_type] * quantity
    setup_cost = setup_options[setup_option] * quantity
    total_cost = phone_cost + setup_cost
    vat = total_cost * vat_rate
    total_cost_with_vat = total_cost + vat
    return total_cost, vat, total_cost_with_vat, setup_cost

# Function to print quotation
def print_quotation(customer_name, company_name, contact_number, quantity, phone_type, setup_option, total_cost, vat, total_cost_with_vat, setup_cost):
    print("\n--- Quotation ---")
    print("Customer Details:")
    print("Name:", customer_name)
    print("Company:", company_name)
    print("Contact Number:", contact_number)
    print("\nSmartphones:")
    print("Quantity:", quantity)
    print("Type:", phone_type.capitalize())
    print("Total phone cost: £", total_cost)
    print("\nSetup Option:")
    print("Option:", setup_option)
    print("Total setup cost: £", setup_cost)
    print("\nCost Summary:")
    print("Total cost (excl. VAT): £", total_cost)
    print("VAT (20%): £", vat)
    print("Total cost (incl. VAT): £", total_cost_with_vat)

# Main function
def main():
    # Get customer details
    customer_name = input("Enter customer name: ")
    company_name = input("Enter company name: ")
    contact_number = input("Enter contact number: ")

    # Get quantity, phone type, and setup option
    quantity = get_quantity()
    phone_type = get_phone_type()
    setup_option = get_setup_option()

    # Calculate total cost
    total_cost, vat, total_cost_with_vat, setup_cost = calculate_total_cost(quantity, phone_type, setup_option)

    # Print quotation
    print_quotation(customer_name, company_name, contact_number, quantity, phone_type, setup_option, total_cost, vat, total_cost_with_vat, setup_cost)

# Run the program
if __name__ == "__main__":
    main()