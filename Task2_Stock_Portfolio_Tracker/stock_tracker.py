stocks = {
    "TCS": 3500,
    "INFY": 1600,
    "WIPRO": 450,
    "RELIANCE": 2800
}

total_value = 0

print("Available Stocks:")
for stock, price in stocks.items():
    print(stock, ":", price)

n = int(input("How many stocks do you own? "))

for i in range(n):
    stock_name = input("Enter stock name: ").upper()
    quantity = int(input("Enter quantity: "))

    if stock_name in stocks:
        total_value += stocks[stock_name] * quantity
    else:
        print("Stock not found!")

print("\nTotal Portfolio Value: ₹", total_value)