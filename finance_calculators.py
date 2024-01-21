import math

#ask the user which calculation they want to do, investment or bond?
calculation = '''
	Investment 	- to calculate the amount of interest you'll earn on your investment.
	Bond		- to calculate the amount you'll have to pay on a home loan.

	Enter either "investment" or "bond" from the menu above to proceed:
'''
print(calculation)
#define a variable to store the user's selected calculation, and make sure is not case sensitive
user_calculation = input().lower()


if user_calculation == "investment" or user_calculation == "bond":
    print(f"Thank you, we will now calculate your {user_calculation}.")

    #if the user inputs either investment or bond then execute this code block
    if user_calculation == "investment":

        #Variables required for the calculations are:
        #A = total_balance (the output), P = user_deposit, r = interest_rate, t = number_years
        user_deposit = int(input("How much money are you depositing? £"))
        interest_rate = int(input("What is the interest rate you have? (only the number is required eg/ 8 not 8%) ")) / 100
        number_years = int(input("How many years do you plan on investing? "))

        #Calculation will depend on whether 'simple' or 'compound' is selected
        interest = input("Would you like 'simple' or 'compound' interest? ").lower()

        if interest == "simple": #follow equation, A = P * (1 + r*t)
            total_balance = user_deposit * (1 + interest_rate * number_years)
            total_balance = round(total_balance, 2)
            print(f"Your total balance is £{total_balance}.")

             #If user left investment for 20 years at 8%
            interest_rate = 0.08
            number_years = 20
            set_balance = user_deposit * (1 + interest_rate * number_years)
            set_balance = round(set_balance, 2)
            print(f"Your total balance would be £{set_balance} if you invested for 20 years at 8%.")

        elif interest == "compound": #follow equation, A = P * math.pow((1+r),t)
            total_balance = user_deposit * math.pow((1 + interest_rate), number_years)
            total_balance = round(total_balance, 2)
            print(f"Your total balance is £{total_balance}.")

            #If user left investment for 20 years at 8%
            interest_rate = 0.08
            number_years = 20
            set_balance = user_deposit * math.pow((1 + interest_rate), number_years)
            set_balance = round(set_balance, 2)
            print(f"Your total balance would be £{set_balance} if you invested for 20 years at 8%.")

        else:
            print("Sorry that wasn't recognised.")
    

    elif user_calculation == "bond":

        #Variables required for the calculations are:
        #repayment = (output), P = house_value, i = monthly_interest_rate, n = months_repaying
        house_value = int(input("What is the present value of the house? £"))
        monthly_interest_rate = (int(input("What is the interest rate you have? (only the number is required eg/ 8 not 8%) ")) / 100) / 12
        months_repaying = int(input("Over how many months are you repaying your bond? "))

        #follow equation, repayment = (i * P )/(1 - (1 + i)**(-n))
        repayment = (monthly_interest_rate * house_value)/(1 - (1 + monthly_interest_rate)**(-months_repaying))
        repayment = round(repayment, 2)
        print(f"Your monthly repayments will be £{repayment}.")
else:
    print("Sorry that wasn't recognised.")