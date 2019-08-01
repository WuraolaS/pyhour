#function that dtermines the percentage of your monthly salary that you need save to reach your downpayment in 36 months, keeping the semi annual raise in min
total_cost = float(input("What is the total cost of the house?\n"))
#down payment amount
portion_down_payment = 0.25 * total_cost
goal=36
current_savings = 0
#savings_rate = ???

#36 * monthly_saving = 250000
#monthly_saving=6944.44
#6944 is 69.4 of monthly salary, they'll need a saving rate of 0.69

#first divide the number of months  by the downpayment to get the monthly amount needed
#then find out how much of that is equal to to the monthly income
#monthly amount needed to reach goal. The amount you need to save monthly to reach the goal

monthly_needed_amount=float(portion_down_payment)/goal
#you need 6944 a month to reach the downpayment of 250000 in 36 months
#actual_monthly_needed_amount = 6944
#how much of that part of the monhtly amount

annual_salary=float(input("what is your annual salary?\n"))
monthly_salary = annual_salary/12
semi_annual_raise = 0.04

for i in range(0, 24):
    if i % 6 == 0:
        monthly_salary += monthly_salary * float((semi_annual_raise/6.0))
    i+=1


savings_amount = monthly_needed_amount/monthly_salary

print(f"you'll need to save {savings_amount} of your monthly salary to reach your downpayment in 36 months")


#find out how much saving amount is for each month, then average it all
# monthly_savings=[]
# for i in range (0.36):
