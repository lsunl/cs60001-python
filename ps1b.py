# Calculate how long it takes to save enough money make a down payment on a house
# after getting a semi annual raise

def app():
    # INPUTS
    annual_salary = float(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))
    semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

    portion_down_payment = 0.25

    current_savings = 0

    r = 0.04
    # bonus = current_savings*r/12


    monthly_salary = (annual_salary/12)

    goal = (total_cost * portion_down_payment)

    months = 1
    while (current_savings < goal):

        if (months % 6 == 0):
            monthly_salary *= (1 + semi_annual_raise)
            current_savings += current_savings*r/12
            current_savings += (monthly_salary * portion_saved)
        else:
            current_savings += current_savings*r/12
            current_savings += (monthly_salary * portion_saved)

        months += 1


    print(months)




if __name__ == "__main__":
    app()
