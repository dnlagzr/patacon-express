# Assign values to the pension variables
#worker's largest 3 expected incomes:
pension1 = 65000.00
pension2 = 68000.00
pension3 = 72000.00

workers_current_age = 40 
workers_current_years_of_service = 10 

#retirement_ages = [55, 60, 65]
retirement_age1 = 55
retirement_age2 = 60
retirement_age3 = 65

# Calculate the average of the three pension values
pension_avg_best_of_3 = (pension1 + pension2 + pension3) / 3  # Use / for division

# Print the average value
print(pension_avg_best_of_3)

rate = 0.014
pension_avg_best_of_3 = 68333.33333333333

#years of service at retirement = 10 + (retirement age [55, 60, 65] - 40)
years_of_service_at_retirement1 = workers_current_years_of_service + (retirement_age1 - workers_current_age)
print(years_of_service_at_retirement1)

years_of_service_at_retirement2 = workers_current_years_of_service + (retirement_age2 - workers_current_age)
print(years_of_service_at_retirement2)

years_of_service_at_retirement3 = workers_current_years_of_service + (retirement_age3 - workers_current_age)
print(years_of_service_at_retirement3)

#pension income = 68333.33 * 0.014 * (years of retirement [55, 60, 65])
pension_income1 = pension_avg_best_of_3 * rate * years_of_service_at_retirement1
print(pension_income1)
pension_income2 = pension_avg_best_of_3 * rate * years_of_service_at_retirement2
print(pension_income2)
pension_income3 = pension_avg_best_of_3 * rate * years_of_service_at_retirement3
print(pension_income3)