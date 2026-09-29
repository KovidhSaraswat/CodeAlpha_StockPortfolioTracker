import csv

def stock_tracker():
    # Hardcoded stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 400,
        "AMZN": 175
    }

    portfolio = {}
    total_investment = 0

    print("=== Stock Portfolio Tracker ===")
    print("Available stocks and prices ($):", stock_prices)

    while True:
        symbol = input("\nEnter stock symbol to add (or type 'done' to finish): ").upper().strip()
        
        if symbol == 'DONE':
            break

        if symbol not in stock_prices:
            print("Stock not found in database. Try AAPL, TSLA, GOOGL, MSFT, or AMZN.")
            continue

        try:
            quantity = int(input(f"Enter quantity for {symbol}: "))
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
            
            portfolio[symbol] = portfolio.get(symbol, 0) + quantity
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if not portfolio:
        print("\nNo stocks were added to your portfolio.")
        return

    print("\n--- Portfolio Summary ---")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total_investment += value
        print(f"{stock}: {qty} shares @ ${price} each = ${value:.2f}")

    print(f"\nTotal Portfolio Value: ${total_investment:.2f}")

    # Optional: Save result to a file
    save_choice = input("\nWould you like to save this summary to a CSV file? (y/n): ").lower().strip()
    if save_choice == 'y':
        with open("portfolio_summary.csv", mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Stock Symbol", "Quantity", "Price Per Share ($)", "Total Value ($)"])
            for stock, qty in portfolio.items():
                writer.writerow([stock, qty, stock_prices[stock], stock_prices[stock] * qty])
            writer.writerow([])
            writer.writerow(["Total Portfolio Value", "", "", total_investment])
        print("Summary successfully saved to 'portfolio_summary.csv'.")

if __name__ == "__main__":
    stock_tracker()