#Determine how many months it will take your savings to come up with the the down payment amount
#
#total cost of home
total_cost = float(input("What is the total cost the house?\n"))
#down payment amount
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
annual_salary=float(input("what is your annual salary?\n"))
portion_saved = float(input("what percentage of your salary will you be saving each month?\n"))
monthly_salary = annual_salary/12

count = 0
while current_savings < portion_down_payment:
    current_savings += float((portion_saved*monthly_salary))+float((current_savings*r))/12.0
    count += 1
print(f"It will take {count} months to save for the down payment of this home")
# x=0
# current_savings = 0
# total_monthly_savings = (portion_saved*monthly_salary) +current_savings*r/12​ 
# while
#     x = ((x * 3)/ 12) + 1000

#Next steps is to add the function to a function
