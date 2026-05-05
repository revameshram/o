# Simple Investment Decision using Utility Theory (2 Stocks)

# User input
print("Enter your preferences (0–100):")

U_safety = float(input("Utility for Safety: "))
U_return = float(input("Utility for High Returns: "))

# Stock data (example probabilities)
stocks = {
    "P": {
        "safe": 0.7,
        "high_return": 0.6
    },
    "Q": {
        "safe": 0.4,
        "high_return": 0.9
    }
}

# Expected Utility function
def calculate_EU(stock):
    EU = (
        stock["safe"] * U_safety +
        stock["high_return"] * U_return
    )
    return EU

# Compute EU
results = {}
for name, values in stocks.items():
    results[name] = calculate_EU(values)

# Display results
print("\nExpected Utility:")
for k, v in results.items():
    print(f"Stock {k}: {v}")

# Best stock
best = max(results, key=results.get)
print(f"\nRecommended Stock: {best}")