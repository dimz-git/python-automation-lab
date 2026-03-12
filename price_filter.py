#function for categorization the price
def categorization_price(price_list, threshold=500):
    for price in price_list : 
        if price > threshold:
            print(f"premium: {price}")
        else:
            print(f"affordable: {price}")
#function for apply_discount
def apply_discount(price_list):
    for price in price_list:
        
        if price > 1000:
            new_price = price *0.9
            print(f"special pricer (10% Off): {new_price}")
        else:
            print(f"normal price: {price}")
#the data that can you change           
my_data = [1222,3444,5444,123,2123]
print("--- Categorization ---")
categorization_price(my_data)
print("\n--- Discount Applied ---")
apply_discount(my_data)








