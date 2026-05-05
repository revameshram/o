# Personalized Medical Treatment Decision System

# Taking user input (utility values)
print("Enter your preferences on a scale of 0–100:")

U_safety = float(input("Utility for Safety: "))
U_homeo = float(input("Utility for Homeopathic Treatment: "))
U_allo = float(input("Utility for Allopathic Treatment: "))
U_admit = float(input("Utility for Admitted Treatment: "))
U_home = float(input("Utility for Home Treatment: "))

# Treatment probabilities (example values)
treatments = {
    "A": {
        "safe": 0.8, "risky": 0.2,
        "homeo": 0.3, "allo": 0.7,
        "home": 0.4, "admit": 0.6
    },
    "B": {
        "safe": 0.6, "risky": 0.4,
        "homeo": 0.7, "allo": 0.3,
        "home": 0.6, "admit": 0.4
    },
    "C": {
        "safe": 0.9, "risky": 0.1,
        "homeo": 0.5, "allo": 0.5,
        "home": 0.3, "admit": 0.7
    },
    "D": {
        "safe": 0.7, "risky": 0.3,
        "homeo": 0.4, "allo": 0.6,
        "home": 0.8, "admit": 0.2
    }
}

# Function to calculate Expected Utility
def calculate_EU(t):
    EU = (
        t["safe"] * U_safety +
        t["homeo"] * U_homeo +
        t["allo"] * U_allo +
        t["admit"] * U_admit +
        t["home"] * U_home
    )
    return EU

# Compute EU for all treatments
results = {}
for name, values in treatments.items():
    results[name] = calculate_EU(values)

# Display results
print("\nExpected Utility for each treatment:")
for k, v in results.items():
    print(f"Treatment {k}: {v}")

# Best treatment
best = max(results, key=results.get)
print(f"\nRecommended Treatment: {best}")