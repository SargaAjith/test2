# 1. Product catalog
products = {
    'P001': {'name': 'Apple', 'price': 0.5, 'stock': 100},
    'P002': {'name': 'Banana', 'price': 0.2, 'stock': 150},
    'P003': {'name': 'Orange', 'price': 0.7, 'stock': 80}
}

# 2. Function to add items to the bill and handle stock validation
def add_to_bill():
    bill = []
    total_amount = 0
    
    while True:
        product_id = input("Enter Product ID (or 'done' to finish): ").strip()
        
        if product_id.lower() == 'done':
            break
        
        if product_id not in products:
            print("Invalid product ID. Please try again.")
            continue
        
        try:
            quantity = int(input("Enter Quantity: ").strip())
        except ValueError:
            print("Invalid quantity. Please enter a valid number.")
            continue
        
        product = products[product_id]
        
        if quantity > product['stock']:
            print(f"Insufficient stock for {product['name']}. Available stock: {product['stock']}")
            continue
        
        cost = product['price'] * quantity
        
        bill.append({
            'name': product['name'],
            'quantity': quantity,
            'cost': cost,
            'price': product['price']
        })
        
        product['stock'] -= quantity
        
        total_amount += cost
    
    display_bill(bill, total_amount)

# 3. Function to display the bill summary
def display_bill(bill, total_amount):
    print("\nBill Summary:")
    for i, item in enumerate(bill, start=1):
        print(f"{i}. {item['name']} - {item['quantity']} x ${item['price']} = ${item['cost']}")
    print(f"\nTotal Amount: ${total_amount:.2f}")

if __name__ == "__main__":
    add_to_bill()
