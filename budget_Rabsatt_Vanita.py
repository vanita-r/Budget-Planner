#Welcome Screen
print("~Welcome To Budget Planner~")
print("What is your name?: ") #Asks the user what their name is
name=input() #Prompts the user to input their name
print("Hello, " + name + "!") #Greets the user with their name


# Wage
hourlyWage = float(10) #As stated in the project assignment page, the hourly wage is $10
print("Hourly wage: $" + str(hourlyWage)) #Prints the hourly wage and turns the hourlyWage variable into a string
print() #Extra print line to make the results look neater

# Monthly costs
def monthlyCosts():
    print("What is the monthly rent for a local apartment?: ")
    monthlyRent = float(input()) #All of the inputs here and below turn the stored input in the variable into a float so monthly costs can have a decimal

    print("What is the monthly internet service cost?: ")
    monthlyInternet = float(input())

    print("What is the monthly grocery bill cost?: ")
    monthlyGrocery = float(input())

    print("What is the monthly 'fun' allowance? (Can be funds used to pay for leisurely activities): ")
    monthlyAllowance = float(input())
    print() #Extra print line to make the results look neater

    # Calculate hours needed for each expense
    def expenseCalculations(monthlyRent, monthlyInternet, monthlyGrocery, monthlyAllowance):
        hoursNeeded_Rent = monthlyRent / hourlyWage
        hoursNeeded_Internet = monthlyInternet / hourlyWage
        hoursNeeded_Grocery = monthlyGrocery / hourlyWage
        hoursNeeded_Allowance = monthlyAllowance / hourlyWage

        # Calculate total hours needed to cover all expenses + $100
        totalMonthlyExpenses = monthlyRent + monthlyInternet + monthlyGrocery + monthlyAllowance + 100
        hoursNeeded_Total = totalMonthlyExpenses / hourlyWage

        return hoursNeeded_Rent, hoursNeeded_Internet, hoursNeeded_Grocery, hoursNeeded_Allowance, hoursNeeded_Total, totalMonthlyExpenses

    # Call expenseCalculations and get results
    hoursNeeded_Rent, hoursNeeded_Internet, hoursNeeded_Grocery, hoursNeeded_Allowance, hoursNeeded_Total, totalMonthlyExpenses = expenseCalculations(monthlyRent, monthlyInternet, monthlyGrocery, monthlyAllowance)

    # Print results
    def monthlyExpenses(monthlyRent, monthlyInternet, monthlyGrocery, monthlyAllowance, totalMonthlyExpenses):
        print(f"Monthly rent: ${str(monthlyRent)}") #All of the hoursNeeded are called with strings to format them better
        print(f"Internet Service Bill: ${str(monthlyInternet)}")
        print(f"Grocery bill: ${str(monthlyGrocery)}")
        print(f"'Fun' Allowance: ${str(monthlyAllowance)}")
        print(f"Total monthly expenses: ${str(totalMonthlyExpenses)}")
        print() #Extra print line to make the results look neater

    monthlyExpenses(monthlyRent, monthlyInternet, monthlyGrocery, monthlyAllowance, totalMonthlyExpenses)

    # Print hours needed
    def expenseResults(hoursNeeded_Rent, hoursNeeded_Internet, hoursNeeded_Grocery, hoursNeeded_Allowance, hoursNeeded_Total):
        print("To cover the monthly rent for a local apartment, you will need to work " + str(hoursNeeded_Rent) + " hours.") #All of the hoursNeeded are called with strings to format them better
        print("To cover the internet service bill, you will need to work " + str(hoursNeeded_Internet) + " hours.")
        print("To cover the grocery bill, you will need to work " + str(hoursNeeded_Grocery) + " hours.")
        print("To cover the 'fun' allowance, you will need to work " + str(hoursNeeded_Allowance) + " hours.")
        print("To cover all expenses and save an additional $100, you will need to work " + str(hoursNeeded_Total) + " hours.")

    expenseResults(hoursNeeded_Rent, hoursNeeded_Internet, hoursNeeded_Grocery, hoursNeeded_Allowance, hoursNeeded_Total)

# Start Program
monthlyCosts() #Calls the monthlyCosts function to start the program, calculate the costs, and print the results


#Loop for continuing or stopping the program
loopCount = 0 
while loopCount == 0: #The loopCount variable and while loop helps the program to keep running until the user says no to planning another budget
    print() #Extra print line to make the results look neater
    print() #Extra print line to make the results look neater
    print("Would you like to plan another budget?")
    answer=input() #Stores the user's input into the "answer" variable
    userAnswer=answer.upper() #capitalizes the user's answer to match the yes variable below if their answer is "yes"
    yes = "YES"
    if userAnswer == yes:
        print() #Extra print line to make the results look neater
        monthlyCosts() #Calls the monthlyCosts variable to calculate the costs and print them
    else:
        #End of Program
        print() #Extra print line to make the results look neater
        print("Goodbye!") 
        loopCount=loopCount+1 #Ends the loop by adding 1 to the loopCount