# Calculate how much to save each month
# in order to afford a house in three years
# DECLARE AND INITIALIZE
total_cost = 1000000
semi_annual_raise = 0.0704
portion_down_payment = 0.25
current_savings = 0
r = 0.04
months = 36

# CALCULATIONS
goal = (total_cost * portion_down_payment)

# FIND BEST SAVINGS RATE THROUGH BISECTION SEARCH


def getincome(monthly_salary, portion_saved):

    for x in range(1,37):
        if (x % 6 == 0 and x > 1):
            monthly_salary *= (1 + semi_annual_raise)
            current_savings += current_savings*r/12
            # portion_saved = ((goal/36) - (current_savings*r/12))/monthly_salary
            current_savings += (monthly_salary * portion_saved)
        else:
            current_savings += current_savings*r/12
            current_savings += (monthly_salary * portion_saved)

            return current_savings

def app():
    # INPUTS
    bisection_steps = 0
    low = 0.0
    high = 1.0
    guess = (high + low)/2.0
    epsilon = 100

    
    annual_salary = float(input("Enter your annual salary: "))

    monthly_salary = (annual_salary/12)

    getincome(monthly_salary, guess)

    if (getincome(monthly_salary, 1.00)- goal) >= 0:

    # Initialize bisection step counter
        bisection_steps = 0

    # Check to see how close current savings is to the down payment by subtracting the two.
    # If the difference is greater than our target difference of 100 (epsilon), then we need
    # to find a new savings rate using bisection.
        while abs((current_savings - goal)) >= epsilon:

            # If current savings is less than down payment, then the savings rate needs to be larger.
            # To get a larger savings rate, we have to reset the low value to the current value of the
            # savings rate because we already know that this current savings rate is too low
            # (because it's producing too little savings).
            if (current_savings < goal):
                low = guess

            # Otherwise, if the current savings is greater than the down_payment, then we need to
            # reduce the savings rate. To get a smaller savings rate, we reset the high value to the
            # current savings rate because we know the current value of the savings rate is too high
            # (because it's producing too much savings).
            else:
                high = guess

            # Calculate new guess for bisection search
            guess = (high + low)/2

            # Calculate new savings rate to use in calculating current savings
            portion_saved = ((high + low)/2.0)

            # Increment the counter which is tracking number of bisection steps
            bisection_steps += 1

            # Reset current_savings to 0
            current_savings = 0

            # Call calcSavings function with original annual_salary and new savings_rate
            getincome(monthly_salary, portion_saved)

    #print("Current Savings:", current_savings)
        #print("Down payment required:", down_payment)
        print("Best savings rate:", savings_rate)
        print("Steps in bisection search:", bisection_steps)
    else:
        print("It is not possible to pay the down payment in three years.")

    # # print(getincome(monthly_salary, .11))
    # while abs(getincome(monthly_salary, portion_saved) - goal) >= 0.01:
    #     savings = getincome(monthly_salary, portion_saved)
    #     print("low: ", low, " high: ", high, "portion saved: ", portion_saved, "savings: ", savings)
    #     if savings < goal:
    #         low = portion_saved
    #         # current_savings = 0
    #     else:
    #         high = portion_saved
    #         # current_savings = 0
    #     portion_saved = (high + low)/2.0
    #     guesses += 1
    #
    #     current_savings = 0
    #
    #     getincome(monthly_salary, portion_saved)
    #
    #     if guesses > 30:
    #         print("It's not possible to pay within three years")
    #         break
    #
    #
    # print("Best savings rate: ", portion_saved)
    # print("Number of steps: ", guesses)




if __name__ == "__main__":
    app()
