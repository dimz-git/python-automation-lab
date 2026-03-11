# List of product prices from our supplier
# You can update this list with your inventory data
product_price = [10,100,400,900,1200,1500]

# Price threshold for categorization (in currency units)
threshold = 500

# Loop through each price and categorize automatically
for price in product_price :
    if price > threshold :
        print(f":Premium Product {price}")
    else:
        print(f"Affordable Product: {price}")
print("categorization complete!")
