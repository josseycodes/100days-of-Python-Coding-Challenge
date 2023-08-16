# Dictionary to store available products with their prices
products = {
    "shirt": 20,
    "pants": 30,
    "shoes": 50,
    "hat": 10,
}

# Shopping cart to store selected items and quantities
cart = {}


def display_products():
    print("Available products:")
    for product, price in products.items():
        print(f"{product.capitalize()}: ${price}")


def add_to_cart(item, quantity):
    if item in products and quantity > 0:
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Added {quantity} {item}(s) to the cart.")
    else:
        print("Invalid item or quantity. Please try again.")


def view_cart():
    if not cart:
        print("Your cart is empty.")
    else:
        print("Items in your cart:")
        for item, quantity in cart.items():
            print(f"{item.capitalize()}: {quantity}")


def calculate_total():
    total = 0
    for item, quantity in cart.items():
        total += products[item] * quantity
    return total


def checkout():
    if not cart:
        print("Your cart is empty. Nothing to checkout.")
    else:
        print("Your order:")
        view_cart()
        total = calculate_total()
        print(f"Total: ${total}")
        choice = input("Confirm your order (yes/no): ").lower()
        if choice == "yes":
            print("Thank you for your order!")
            cart.clear()
        else:
            print("Order cancelled.")


def main():
    print("Welcome to the E-commerce Store!")
    while True:
        print("\nMenu:")
        print("1. Display Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            display_products()
        elif choice == "2":
            item = input("Enter the product you want to add to the cart: ").lower()
            quantity = int(input("Enter the quantity: "))
            add_to_cart(item, quantity)
        elif choice == "3":
            view_cart()
        elif choice == "4":
            checkout()
        elif choice == "5":
            print("Thank you for visiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

