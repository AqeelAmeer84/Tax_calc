def cal_income_tax(annual_income):
    tax = 0
    income = annual_income
    
    if income <= 1800000: #1.8 mil
        return 0
    if income > 1800000: #1.8 mil
        can_tax = min(annual_income, 2800000) - 1800000
        tax += can_tax * 0.06
    if income > 2800000:
        can_tax = min(income, 3300000) - 2800000
        tax += can_tax * 0.18
    if income > 3300000:
        can_tax = min(income, 3800000) - 3300000
        tax += can_tax * 0.24
    if income > 3800000:
        can_tax = min(income, 4300000) - 3800000
        tax += can_tax * 0.30
    if income > 4300000:
        can_tax = income - 4300000
        tax += can_tax * 0.36
    return tax
        
def calculate_effective_tax_rate(annual_income):
    if annual_income <= 0:
        return 0
    
    
    tax = cal_income_tax(annual_income)
    return (tax/annual_income) * 100

def calculate_take_home(annual_income):
    tax = cal_income_tax(annual_income)
    return annual_income - tax

incomes = [2500000, 4000000, 5000000, 1500000, 3500000]
taxes = list(map(cal_income_tax, incomes))
high_earners = list(filter(lambda income: income >= 4300000, incomes))
income_tax_pairs = list(zip(incomes,taxes))

sort_income_taxes = sorted(income_tax_pairs, key=lambda pair: pair[1], reverse=True)

print("=" * 60)
print("SRI LANKAN TAX CALCULATOR (April 2025 Tax Reforms)")
print("=" * 60)

print("\n" + "=" * 60)
print("DETAILED TAX REPORTS")
print("=" * 60)

for income in incomes:
    tax = cal_income_tax(income)
    rate = calculate_effective_tax_rate(income)
    take_home = calculate_take_home(income)
    
    print(f"Annual Income: Rs. {income:,.2f}")
    print(f"Income Tax: Rs. {tax:,.2f} ({rate:.2f}%)")
    print(f"Take-Home (Annual): Rs. {take_home:,.2f}")
    print(f"Take-Home (Monthly): Rs. {take_home / 12:,.2f}")
    print("-" * 60)
    
print("=" * 60)
print("TOP TAXPAYERS (Ranked by Tax Paid)")
print("=" * 60)

for index, (income, tax) in enumerate(sort_income_taxes, start=1):
    print(f"{index}. Rs. {income:,.2f} - Tax Paid: Rs. {tax:,.2f}")


print("=" * 60)
print("HIGH EARNERS (>= Rs. 4,300,000 - Top Tax Bracket)")
print("=" * 60)

for income in high_earners:
    tax = cal_income_tax(income)
    print(f"Income: Rs. {income:,.2f} - Tax: Rs. {tax:,.2f}")    