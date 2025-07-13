import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# 1. User-Defined Assumptions
# -------------------------------
print("📊 SaaS Business Scenario Modeler: Assumption Adjuster")
print("--------------------------------------------------")

try:
    months = int(input("Number of months to simulate (e.g. 12): ") or 12)
    initial_customers = int(input("Initial number of customers (e.g. 100): ") or 100)
    monthly_fee = float(input("Monthly subscription fee in USD (e.g. 50): ") or 50)
    churn_rate = float(input("Monthly churn rate (0.0 - 1.0) (e.g. 0.05): ") or 0.05)
    fixed_costs = float(input("Monthly fixed costs in USD (e.g. 5000): ") or 5000)
    variable_cost_per_customer = float(input("Variable cost per customer in USD (e.g. 10): ") or 10)
    growth_rate_base = float(input("Base growth rate (0.0 - 1.0) (e.g. 0.10): ") or 0.10)
    growth_rate_optimistic = float(input("Optimistic growth rate (e.g. 0.15): ") or 0.15)
    growth_rate_pessimistic = float(input("Pessimistic growth rate (e.g. 0.05): ") or 0.05)
except ValueError:
    print("⚠️ Invalid input detected. Please enter numeric values.")
    exit()

# -------------------------------
# 2. Scenario Simulation Function
# -------------------------------
def simulate_scenario(growth_rate):
    customers = [initial_customers]
    revenue = []
    costs = []
    profit = []

    for month in range(months):
        current_customers = customers[-1]
        next_customers = current_customers * (1 + growth_rate - churn_rate)
        customers.append(next_customers)

        current_revenue = current_customers * monthly_fee
        current_costs = fixed_costs + (current_customers * variable_cost_per_customer)
        current_profit = current_revenue - current_costs

        revenue.append(current_revenue)
        costs.append(current_costs)
        profit.append(current_profit)

    return revenue, costs, profit

# -------------------------------
# 3. Simulate All Scenarios
# -------------------------------
rev_base, cost_base, prof_base = simulate_scenario(growth_rate_base)
rev_opt, cost_opt, prof_opt = simulate_scenario(growth_rate_optimistic)
rev_pes, cost_pes, prof_pess = simulate_scenario(growth_rate_pessimistic)

months_range = np.arange(1, months + 1)

# -------------------------------
# 4. Terminal Outputs
# -------------------------------
print("\n📈 Monthly Profit Projections (Base Scenario):")
print("--------------------------------------------------")
for m, p in zip(months_range, prof_base):
    print(f"Month {m}: ${p:,.2f}")

print("--------------------------------------------------")
print(f"✅ Estimated Total Profit (Base): ${sum(prof_base):,.2f}")
print(f"🏆 Month with Highest Profit (Base): Month {np.argmax(prof_base) + 1} - ${max(prof_base):,.2f}")
print("--------------------------------------------------")

# -------------------------------
# 5. Visualization
# -------------------------------
plt.figure(figsize=(12, 6))
plt.plot(months_range, prof_opt, label="Optimistic", linestyle="--")
plt.plot(months_range, prof_base, label="Base", linestyle="-")
plt.plot(months_range, prof_pess, label="Pessimistic", linestyle=":")
plt.title("Monthly Profit Projections - SaaS Scenario Modeling")
plt.xlabel("Month")
plt.ylabel("Profit (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(months_range, np.cumsum(prof_opt), label="Optimistic", linestyle="--")
plt.plot(months_range, np.cumsum(prof_base), label="Base", linestyle="-")
plt.plot(months_range, np.cumsum(prof_pess), label="Pessimistic", linestyle=":")
plt.title("Cumulative Profit Over Time")
plt.xlabel("Month")
plt.ylabel("Cumulative Profit (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

customers_base = [initial_customers]
for i in range(months):
    next_customers = customers_base[-1] * (1 + growth_rate_base - churn_rate)
    customers_base.append(next_customers)
plt.figure(figsize=(10, 6))
plt.plot(range(months + 1), customers_base, marker='o')
plt.title("Customer Growth (Base Scenario)")
plt.xlabel("Month")
plt.ylabel("Number of Customers")
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(months_range, rev_base, label="Revenue", color='green')
plt.plot(months_range, cost_base, label="Costs", color='red')
plt.title("Revenue vs Costs (Base Scenario)")
plt.xlabel("Month")
plt.ylabel("Amount (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 6))
plt.bar(months_range, prof_base, color='skyblue')
plt.title("Monthly Profit - Base Scenario")
plt.xlabel("Month")
plt.ylabel("Profit (USD)")
plt.grid(True, axis='y')
plt.tight_layout()
plt.show()