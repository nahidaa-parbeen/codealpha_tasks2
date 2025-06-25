stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2700,
    "MSFT": 320,
    "AMZN": 135
}

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(f"  {stock} - ₹{price}")

portfolio = {}
n = int(input("\nHow many different stocks do you want to add? "))

for i in range(n):
    print("\nChoose from the available stock names above.")
    stock_name = input(f"Enter stock name ({i+1}): ").upper()
    if stock_name not in stock_prices:
        print("This stock is not in the list. Skipping.")
        continue
    quantity = int(input(f"How many shares of {stock_name}? "))
    portfolio[stock_name] = quantity

total = 0
print("\n--- Portfolio Summary ---")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    investment = price * qty
    total += investment
    print(f"{stock}: {qty} shares x ₹{price} = ₹{investment}")

print(f"\nTotal Investment Value: ₹{total}")

save = input("\nDo you want to save this summary to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("--- Portfolio Summary ---\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            investment = price * qty
            file.write(f"{stock}: {qty} shares x ₹{price} = ₹{investment}\n")
        file.write(f"\nTotal Investment Value: ₹{total}\n")
    print("Summary saved to: portfolio_summary.txt")
