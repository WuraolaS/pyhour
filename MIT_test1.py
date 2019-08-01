total_cost = float(1000000)
#down payment amount
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
annual_salary=float(120000)
portion_saved = 0.1
monthly_salary = float(annual_salary/12)

#number_of_months = portion_down_payment/portion_saved

#It keeps ending in an infinite loop
count = 0
while current_savings <= portion_down_payment:
    current_savings += float((portion_saved*monthly_salary)) + float((current_savings*r))/12.0
    count += 1
print(count)
