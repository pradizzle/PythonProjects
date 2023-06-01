import csv
import re

cleaned_data = []

with open('sales_data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        if all(row.values()):  
            row['Product'] = row['Product'].strip()
            year, month, _ = row['Date'].split('-')
            row['Year'] = int(year)
            row['Month'] = int(month)
            row['Category'] = re.sub(r'\W+', '', row['Notes']).strip()
            cleaned_data.append(row)

fieldnames = cleaned_data[0].keys()

with open('new_sales_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(cleaned_data)

product_revenue = {}
product_quantity = {}
product_price = {}

for row in cleaned_data:
    product = row['Product']
    quantity = int(row['Quantity']) if row['Quantity'] else 0  
    price = float(row['Price']) if row['Price'] else 0.0   
    revenue = quantity * price

    if product in product_revenue:
        product_revenue[product] += revenue
        product_quantity[product] += quantity
    else:
        product_revenue[product] = revenue
        product_quantity[product] = quantity

    if product not in product_price:
        product_price[product] = price

highest_revenue_product = max(product_revenue, key=product_revenue.get)
print("Product with the highest revenue:", highest_revenue_product)

summary_data = []
for product in product_revenue:
    total_revenue = round(product_revenue[product], 2)
    total_quantity = product_quantity[product]
    average_price = round(total_revenue / total_quantity, 2) if total_quantity > 0 else 0.0  
    summary_data.append({
        'Product': product,
        'Total Sales Revenue': total_revenue,
        'Total Quantity Sold': total_quantity,
        'Average Price Per Unit': average_price
    })

summary_fieldnames = summary_data[0].keys()

with open('sales_summary.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=summary_fieldnames)
    writer.writeheader()
    writer.writerows(summary_data)
