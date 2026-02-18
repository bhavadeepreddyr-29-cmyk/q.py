down_payment_percent = 0.25
anual_return = 0.04

anual_salary = int(input("Enter your salary per annum:"))
portion_saved = float(input("Enter the percent of salary to save,as a decimal:"))
dream_house_cost = int(input("Enter the cost of your dream house:"))

salary_per_month = anual_salary / 12.0
monthly_savings = portion_saved * salary_per_month
down_payment = down_payment_percent*dream_house_cost

present_savings = 0.0
mon = 0

while present_savings < down_payment :
    present_savings += present_savings*(anual_return/12.0)
    present_savings += monthly_savings
    mon += 1

print("Number of months:",mon)