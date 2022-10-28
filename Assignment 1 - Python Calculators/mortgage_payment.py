
def total_payments(monthly_payment, n): # Multiplying monthly payments by the amount of months
    return monthly_payment*n

def monthly_payments(loan_duration, loan_amount, rate): # Using the online equation for monthly payments
    return loan_amount * ( (rate*( 1 + rate)**loan_duration ) / ( -1 + ( 1 + rate )**loan_duration) )

def myFICO(loan_duration, loan_amount, fico):
    while True: # Loop that prompts user for a loan duration in months. Does not accept floats or strings.
        try:
            n = int(input(loan_duration))
        except ValueError:
            print("Invalid input, enter a loan duration in months!")
            continue
        if n <= 0:
            print("Invalid loan duration, try again!")
            continue
        else: break
    
    while True: # Loop that prompts user for a loan amount. Accepts floats.
        try:
            loan_amount = float(input(loan_amount))
        except ValueError:
            print("Invalid input, enter a correct loan amount. Can be decimals or integers!")
            continue
        break

    while True: # Loop that prompts user for a FICO score within the acceptable range, loop will continue until a score inside range is provided.
        try:
            score = int(input(fico))
        except ValueError:
            print("Invalid input, try a range of numbers from [620-850]!")
            continue
        if score > 850 or score < 620:
            print("FICO score is outside acceptable range, try again!")
            continue
        else: break

    def bracket(score): # Returns the bracket score when given a FICO
        if score <= 850 and score >= 760:
            return "760-850"
        elif score < 760 and score >= 700:
            return "700-759"
        elif score < 700 and score >= 680:
            return "680-699"
        elif score < 680 and score >= 660:
            return "660-679"
        elif score < 660 and score >= 640:
            return "640-659"
        elif score < 640 and score >= 620:
            return "620-639"
        elif score > 850: # Accounts for the 50+ part of the analysis
            return "760-850"
        elif score < 620: # Accounts for the -50 part of the analysis
            return "620-639"

    fixed_rates = {"620-639": 0.075, "640-659": 0.065, "660-679": 0.0615, "680-699": 0.059, "700-759": 0.057, "760-850": 0.055} # Dictionary containing FICO score brackets as keys, and annual rates as values
    
    # Section: Rates
    rate = fixed_rates[bracket(score)]/12 # Rate given input FICO
    rate_over = fixed_rates[bracket(score + 50)]/12 # Portion asking for FICO to be 50 above
    rate_less = fixed_rates[bracket(score - 50)]/12 # Portion of analysis asking FICO to be 50 below
    
    # Section: Payments
    monthly_payment = monthly_payments(n, loan_amount, rate)
    monthly_payment_higher = monthly_payments(n, loan_amount, rate_over)
    monthly_payment_lower = monthly_payments(n, loan_amount, rate_less)
    
    total_payment = total_payments(monthly_payment, n)
    total_payment_higher = total_payments(monthly_payment_higher, n)
    total_payment_lower = total_payments(monthly_payment_lower, n)

    print("\n ----myFICO Calculator----")
    print(f"FICO: {score}, \n Loan Principal: {loan_amount}, \n Duration: {n} month(s) --> \n Monthly Payments: {monthly_payment}. \n Total payments: {total_payment}")
    print("\n")
    print(f"If your FICO score was {score + 50}, within bracket {bracket(score + 50)} --> \n your monthly payments would be: {monthly_payment_higher}, while total payments are {total_payment_higher}.")
    print(f"Meaning you would save ${monthly_payment-monthly_payment_higher} on monthly payments, and ${total_payment-total_payment_higher} on total payments")
    print("\n")
    print(f"If your FICO score was {score - 50}, within bracket {bracket(score - 50)} --> \n your monthly payments would be: {monthly_payment_lower}, while total payments are {total_payment_lower}.")
    print(f"Meaning you would lose ${monthly_payment_lower-monthly_payment} on monthly payments, and ${total_payment_lower-total_payment} on total payments")
    print("\n")
    for down_payment in [1, 0.9, 0.8, 0.7]: # Looping for the possible down payments
        monthly = monthly_payments(n, loan_amount*down_payment, rate)
        print(f"If you put a {round((1.0-down_payment)*100)}% down payment on the loan --> \n Monthly payments: {monthly} \n Total payments: {total_payments(monthly, n)}")
 
myFICO("What is your loan duration in months: ", "What is your principal loan amount: ", "What is your FICO score [620 to 850]: ")
