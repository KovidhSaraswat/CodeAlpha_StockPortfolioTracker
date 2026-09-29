CodeAlpha_StockPortfolioTracker
# 📈 Stock Portfolio Tracker

A financial calculation tool built in Python to manage stock holdings, calculate portfolio values, and export summary reports. Developed as part of the **CodeAlpha Python Programming Internship**.

---

## 📌 Project Overview
The Stock Portfolio Tracker lets users input stock ticker symbols and quantities, automatically calculates real-time holding values against market prices, and generates an itemized portfolio summary. Users can also export their transaction history directly to a CSV file.

### Key Features
* 💹 **Portfolio Valuation**: Computes individual and total investment totals based on share quantities.
* 📄 **CSV Exporting**: Automatically formats and saves portfolio summaries into `portfolio_summary.csv`.
* ⚠️ **Error Handling**: Handles invalid tickers and non-numeric quantity inputs gracefully.

---

## 🛠️ Tech Stack & Concepts Used
* **Language**: Python 3.x
* **Core Concepts**: Dictionaries, File I/O (`csv` module), input parsing, basic arithmetic algorithms.

---

## 🚀 How to Run

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_StockPortfolioTracker.git](https://github.com/YOUR_GITHUB_USERNAME/CodeAlpha_StockPortfolioTracker.git)
   cd CodeAlpha_StockPortfolioTracker

2. Output Preview 
=== Stock Portfolio Tracker ===
Available stocks and prices ($): {'AAPL': 180, 'TSLA': 250, 'GOOGL': 140, 'MSFT': 400, 'AMZN': 175}

Enter stock symbol to add (or type 'done' to finish): aapl
Enter quantity for AAPL: 5

Enter stock symbol to add (or type 'done' to finish): tsla
Enter quantity for TSLA: 2

Enter stock symbol to add (or type 'done' to finish): done

--- Portfolio Summary ---
AAPL: 5 shares @ $180 each = $900.00
TSLA: 2 shares @ $250 each = $500.00

Total Portfolio Value: $1400.00

Would you like to save this summary to a CSV file? (y/n): y
Summary successfully saved to 'portfolio_summary.csv'.
