# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 330
}

# To store investment details
total_investment = 0
investments = []

while True:
    stock = input("Enter stock symbol (AAPL, TSLA, etc) or 'done' to finish: ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found in our list.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
    except ValueError:
        print("Invalid quantity. Try again.")
        continue

    amount = stock_prices[stock] * quantity
    total_investment += amount
    investments.append(f"{stock}: {quantity} shares × ${stock_prices[stock]} = ${amount}")

# Display result
print("\n----- Investment Summary -----")
for entry in investments:
    print(entry)

print(f"Total Investment: ${total_investment}")

# Optional: save to text file
save = input("Do you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    with open("stock_investment.txt", "w") as file:
        file.write("Investment Summary:\n")
        for entry in investments:
            file.write(entry + "\n")
        file.write(f"\nTotal Investment: ${total_investment}")
    print("Data saved to 'stock_investment.txt'.")
