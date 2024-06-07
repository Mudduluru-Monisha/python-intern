expenses = []
expense1 = {'amount': '250', 'category': 'shirt'}
expenses.append(expense1)
expense2 = {'amount': '100', 'category': 'groceries'}
expenses.append(expense2)

def removeExpense():
    while True:
        listExpenses()
        print("What expense would you like to remove?")
        try:
          expenseToRemove = int(input("> "))
          del expenses[expenseToRemove]
          break
        except:
            print("Invalid input. Please try again.")

def addExpense(amount, category):
    expense = {'amount': amount, 'category': category}
    expenses.append(expense)

def printMenu():
    print("Please choose from one of the following options:")
    print("1. Add a New Expense")
    print("2. Remove an Expense")
    print("3. List all Expenses")

def listExpenses():
    print("\n Here is a list of your Expenses..")
    print("------------------------------------")
    counter = 0
    for expense in expenses:
        print("#", counter, " - ", expense['amount'], " - ", expense['category'])
        counter += 1
    print("\n\n")

if __name__ == "__main__":
    while True:
        printMenu()
        optionSelected = input("> ")

        if(optionSelected == "1"):
            print("How much was this expense?")
            while True:
                try:
                    amountToAdd = input("> ")
                    break
                except:
                  print("Invalid input. Please Try again.")

            print("What category was this expense?")
            while True:
                try:
                    category = input("> ")
                    break
                except:
                  print("Invalid input. Please Try again.")

            addExpense(amountToAdd, category)
        elif(optionSelected == "2"):
            removeExpense()
        elif(optionSelected == "3"):
            listExpenses()
        else:
            print("Invalid input. Please Try again.")
