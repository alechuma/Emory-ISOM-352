def bmr_calculator(gender, age, weight, height):
    while True: # While loops to ensure user inputs correct gender
        g = input(gender)
        if g != "M" and g != "F":
            print("Try again, invalid gender!")
            continue
        else:
            break
    while True: # While loop to ensure the standard age range is inputted correctly in the function. 
        try:
            a = int(input(age))
        except ValueError:
                print("Invalid input")
                continue
        if a > 80 or a < 15:
            print("Age outside acceptable range, try again!.")
            continue
        break

    height = int(input(height)) # Input for height
    weight = int(input(weight)) # Input for weight
    if g == "M": # Checking for gender to go into correct function block
        bmr = 10*weight + 6.25*height - 5*a + 5 
        w_over_percent = (bmr*1.10 + 5*a - 5 -6.25*height)/10
        w_less_percent = (bmr*.90 + 5*a - 5 -6.25*height)/10
    else:
        bmr = 10*weight + 6.25*height - 5*a - 161
        w_over_percent = (bmr*.90 + 161 + 5*a - 6.25*height)/10
        w_less_percent = (bmr*1.10 + 161 + 5*a - 6.25*height)/10
    
    print("\n ----myBMR Calculator----")
    print("BMR = ", bmr, "Calories/Day")
    print("If calories consumed were 10 percent more, weight would be: ", w_over_percent, "lbs.")
    print("If calories consumed were 10 percent less, weight would be: ", w_less_percent, "lbs.")

bmr_calculator("Gender [M/F]: ", "What is your age: ", "What is your weight in pounds: ", "What is your height in inches: ")
