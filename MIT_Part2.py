total_cost = float(input("What is the total cost the house?\n"))
#down payment amount
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
annual_salary=float(input("what is your annual salary?\n"))
portion_saved = float(input("what percentage of your salary will you be saving each month?\n"))
monthly_salary = annual_salary/12
#Your salary raises every 6 months by this percentage, how long will it take for you to save for your dream home
semi_annual_raise = 0.03

count = 0

######  Semi annual raise section
# Monthly raise after 6 months:
#print(monthly_salary * semi_annual_raise/6 + monthly_salary)

while current_savings < portion_down_payment:
    current_savings += float((portion_saved*monthly_salary))+float((current_savings*r))/12.0
    count += 1
    if count % 6 == 0:
        monthly_salary += monthly_salary * float((semi_annual_raise/6.0))
    #roadblock, how to get tell the code to continue looping
print(f"It will take {count} months to save for the down payment of this home")


#simple case for how to calculate the raise
# for i in range(0, 24):
#     if i % 6 == 0:
#         monthly_salary += monthly_salary * float((semi_annual_raise/6.0))
#         print(monthly_salary)
#     i+=1
