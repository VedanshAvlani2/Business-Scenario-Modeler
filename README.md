# SaaS Business Scenario Modeler

## Overview
This Python terminal-based tool simulates and visualizes financial projections for a SaaS startup using a bottom-up modeling approach. It allows users to input assumptions and then generates profit forecasts, customer growth, and revenue-cost charts under three market scenarios—Base, Optimistic, and Pessimistic.

## 📌 Features
- Assumption-based input for growth, churn, cost, and pricing
- Scenario simulation for Base, Optimistic, and Pessimistic growth rates
- Inline terminal output for monthly profit
- Charts for profit trends, cumulative gains, customer growth, and cost vs revenue


## 📦 Dependencies
- numpy
- pandas
- matplotlib

Install via:
```bash
pip install numpy pandas matplotlib
```

## 📥 How to Use
1. Run the script using Python 3.x:
```bash
python saas_modeler.py
```
2. Enter the inputs for:
   - Timeframe (months)
   - Initial customers
   - Subscription price
   - Churn rate
   - Fixed & variable costs
   - Growth rate assumptions

3. View:
   - Monthly and cumulative profit forecasts
   - Customer growth simulation
   - Revenue vs cost trends

## 📊 Visual Output
The script displays the following charts:
- Monthly profit comparison across scenarios
- Cumulative profit over time
- Customer growth in the base scenario
- Revenue vs. Costs (Base scenario)

## 🔍 Example Assumptions
```
Months: 12
Initial Customers: 100
Monthly Fee: $50
Churn Rate: 0.05
Fixed Costs: $5,000
Variable Cost/Customer: $10
Base Growth Rate: 0.10
Optimistic Growth: 0.15
Pessimistic Growth: 0.05
```

## 📈 Sample Output
```
Month 1: $-4,000.00
Month 2: $-3,450.00
...
✅ Estimated Total Profit (Base): $12,500.00
🏆 Month with Highest Profit: Month 12 - $3,000.00
```

## 🔮 Future Enhancements
- **Interactive Dashboard:** Build a Streamlit or Dash-based interface to allow real-time slider adjustments and immediate visual feedback.
- **CAC & LTV Analysis:** Integrate customer acquisition cost (CAC), lifetime value (LTV), and payback period metrics for deeper business insights.
- **Multi-Tier Pricing:** Allow simulation of multiple subscription plans (e.g., Basic, Pro, Enterprise) with different pricing and churn rates.
- **Funding & Runway Simulation:** Include funding inflows and runway tracking based on burn rate and capital raised.
- **Hiring & HR Costs:** Model team growth scenarios with role-based salaries and hiring timelines.
- **CSV Export Option:** Enable exporting scenario data and charts to CSV or PDF for stakeholders.
- **Market Segmentation:** Simulate by market vertical or region to assess growth sensitivity and penetration.
- **Monthly Retention Curve:** Add custom retention decay curves instead of flat churn for more accurate behavior.
