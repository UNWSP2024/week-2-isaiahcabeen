def calculate_total_purchase():
    print("Enter the price of the items")
calculate_total_purchase()

sales_tax_rate = 0.07

subtotal = 0

p1 = float(input("Price of item 1:"))
subtotal = subtotal + p1

p2 = float(input("Price of item 2:"))
subtotal = subtotal + p2

p3 = float(input("Price of item 3:"))
subtotal = subtotal + p3

p4 = float(input("Price of item 4:"))
subtotal = subtotal + p4

p5 = float(input("Price of item 5:"))
subtotal = subtotal + p5

sales_tax = subtotal * sales_tax_rate

total = subtotal + sales_tax

print("Subtotal: $", subtotal)
print("Sales tax: $", round(sales_tax, 2))
print("Total: $", round(total, 2))
