import os
from datetime import datetime
from pandas import read_csv

def format_usd(my_price):
    """
    Formats numbers in USD with a $ and two decimals (and thousands separator)
    Params: 
        my_price (numeric, like int or float) that we want to format

    Example: 
        format_price(8.5433)
        format_price(8)
   """
    return f"${my_price:,.2f}"

def calculate_tax(subtotal):
    """
    Calculates the tax for the receipt
    Params:
        subtotal (numeric, like int or float) that we want to calculate tax on

    Example:
        calculate_tax(10.35)
        calculate_tax(10)

    """
    return "TAX: "+format_usd(0.875*subtotal)

    
# READ INVENTORY OF PRODUCTS

products_filepath = os.path.join(os.path.dirname(__file__), "..", "data", "products.csv")
products_df = read_csv(products_filepath)
products = products_df.to_dict("records")


# CAPTURE PRODUCT SELECTIONS

selected_products = []
while True:
    selected_id = input("Please select a product identifier: ")
    if selected_id.upper() == "DONE":
        break
    else:
        matching_products = [p for p in products if str(p["id"]) == str(selected_id)]
        if any(matching_products):
            selected_products.append(matching_products[0])
        else:
            print("OOPS, Couldn't find that product. Please try again.")

checkout_at = datetime.now()
receipt_id = checkout_at.strftime('%Y-%M-%d-%H-%m-%S')

subtotal = sum([float(p["price"]) for p in selected_products])

# PRINT RECEIPT

intro_output=("---------"+
"\nCHECKOUT AT: " + str(receipt_id)+
"\n---------")

print(intro_output)

for p in selected_products:
    print("\nSELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))

terminal_output = (""+"\n---------"+ 
f"\nSUBTOTAL: {format_usd(subtotal)}"+
"\n"+calculate_tax(subtotal)+
f"\nTOTAL: {format_usd((subtotal * 0.0875) + subtotal)}"+
"\n---------"+
"\nTHANK YOU! PLEASE COME AGAIN SOON!"+
"\n---------")

print(terminal_output)


# WRITE RECEIPT TO FILE

receipt_filepath = os.path.join(os.path.dirname(__file__), "..", "receipts", f"{receipt_id}.txt")

with open(receipt_filepath, "w") as receipt_file:
    receipt_file.write(intro_output)
    for p in selected_products:
        receipt_file.write("\nSELECTED PRODUCT: " + p["name"] + "   " + format_usd(p["price"]))
    receipt_file.write(terminal_output)