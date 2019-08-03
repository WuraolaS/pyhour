monthly_needed=250000/36

total_cost = 1000000
#down payment amount
portion_down_payment = 0.25 * total_cost
current_savings = 0
r = 0.04
semi_annual_raise=0.07

annual_salary=float(input("what is your annual salary?\n"))
portion_saved = 0.1
monthly_salary = annual_salary/12


increase_amount = 0.1
#determines how many months it'll take to retrieve the down payment with a 0.1 savings rate
while current_savings < portion_down_payment:
    current_savings += float((portion_saved*monthly_salary))+float((current_savings*r))/12.0
    count += 1
print(f"It will take {count} months to save for the down payment of this home")
#if after this loop current saving is not equal to
    if current_saving < portion_down_payment and count==36
    portion_saved =+ 0.01

if monthly_salary * 1 *36 < portion_down_payment:
    print("It is not possible to pay the down payment in three years.")
    #if count == 36 and current_savings =! portion_down_payment:
        #portion_saved =+ increase_amount
    #then check again
    #keeo increasing portion_down_payment by 0.1 until current_saving == downpayment
