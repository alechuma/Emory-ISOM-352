Part 1: Mortgage Payment Calculator
	Link: "https://www.myfico.com/credit-education/calculators/loan-savings-calculator/Links"
	My Fico calculator is described as: "The Loan Savings Calculator shows how FICO® scores impact the interest you pay on a loan. Select your loan type and state, enter the appropriate loan details and choose your current FICO® score range. You can see that working to get your score in the higher ranges can mean a big savings!"
	Using MyFico calculator as an example, referenced from the link above, the goal of this assignment is to replicate the functions of the calculator with three primary user inputs:
	- Loan duration, 
	- Loan amount, 
	- FICO score.
Moreover, (print) an analysis on how much will a customer pay/month and pay/loan-term more/less if their credit score was 50 points higher or 50 points lower and (print) an analysis on how much will a customer pay more/less and pay/loan-term if they put a 0%, 10%, 20%, 30% down payment (change their loan amount).

The interest rates used in this case were hypothetical, and the  kind is a n-month fixed loan. The assignment description requires there should be two functions: one to calculate monthly payments, and one to calculate total payments. In order to calculate monthly payments, I used the function: 
A  = P {[r(1+r)^n ]/ [(1+r)^(n)-1]}

A = the amount of your monthly payment (what you’re solving for)
P = the principal (what you borrowed)
r = your monthly interest rate (your annual interest rate divided by 12 months)
n = the loan term in months

Part 2: Create Basal Metabolic Rate (BMR) Calorie Calculator (10 points):
	Link: "https://www.calculator.net/bmr-calculator.htmlLinks"
	 Using the following calculator and Mifflin-St Jeor equation for reference:
Mifflin-St Jeor Equation for men: BMR = 10W + 6.25H - 5A + 5
Mifflin-St Jeor Equation for women: BMR = 10W + 6.25H - 5A - 161
Get input form user for gender, age, weight, and height. (let user enter height in inches and weight in lbs)
(print) a result on how many calories that individual should consume/day and an analysis on what would be the weight if that user consumes 10% more or 10% less calories.

