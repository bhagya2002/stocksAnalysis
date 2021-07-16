# imports yahoo finance, terminal selector (inquirer)
import yfinance as yf
import inquirer

while True:
    # selecter from the terminal
    questions = [
        inquirer.List("Stock Analysis App", message="Please enter a stock and exit once finsihed.", 
                    choices=["Select Stock", "Exit"], carousel=True),
    ]

    # get the answer form the prompt in a dictionary
    stocked = inquirer.prompt(questions)

    # get the value from the dictionary
    if stocked["Stock Analysis App"] == "Select Stock":
        # get list of user stock(s) they want to see
        user_stocks = input("What stock(s) do you want to look into: ")
        # stockparam for Ticker
        stock = yf.Ticker(user_stocks)
    
        while True:
            # selecter from the terminal
            questions = [
                inquirer.List("Stock Analysis Option", message="What about the stock do you want to analyse?", 
                            choices=["Actions (dividends, splits)", "Financials", "Earnings", "Major Holders", "Balance Sheet", "Analysts Recommendations", "Next Event", "New Stock"], carousel=True),
            ]

            # get the answer form the prompt in a dictionary
            answers = inquirer.prompt(questions)

            # get the value from the dictionary
            if answers["Stock Analysis Option"] == "Actions (dividends, splits)":
                print(stock.actions)
                
                # selecter from the terminal
                questions = [
                inquirer.List("Completed sinlge analysis", message="What about the stock do you want to analyse?", 
                            choices=["Done"], carousel=True),
                            ]

                # get the answer form the prompt in a dictionary
                option = inquirer.prompt(questions)
                if option["Completed sinlge analysis"] == "Done":
                    continue
            elif answers["Stock Analysis Option"] == "Financials":
                print(stock.financials)
                
                # selecter from the terminal
                questions = [
                inquirer.List("Completed sinlge analysis", message="What about the stock do you want to analyse?", 
                            choices=["Done"], carousel=True),
                            ]

                # get the answer form the prompt in a dictionary
                option = inquirer.prompt(questions)
                if option["Completed sinlge analysis"] == "Done":
                    continue
            elif answers["Stock Analysis Option"] == "Earnings":
                print(stock.earnings)
                
                # selecter from the terminal
                questions = [
                inquirer.List("Completed sinlge analysis", message="What about the stock do you want to analyse?", 
                            choices=["Done"], carousel=True),
                            ]

                # get the answer form the prompt in a dictionary
                option = inquirer.prompt(questions)
                if option["Completed sinlge analysis"] == "Done":
                    continue
            elif answers["Stock Analysis Option"] == "Major Holders":
                print(stock.major_holders)
                
                # selecter from the terminal
                questions = [
                inquirer.List("Completed sinlge analysis", message="What about the stock do you want to analyse?", 
                            choices=["Done"], carousel=True),
                            ]

                # get the answer form the prompt in a dictionary
                option = inquirer.prompt(questions)
                if option["Completed sinlge analysis"] == "Done":
                    continue
            elif answers["Stock Analysis Option"] == "Balance Sheet":
                print(stock.balance_sheet)
                
                # selecter from the terminal
                questions = [
                inquirer.List("Completed sinlge analysis", message="What about the stock do you want to analyse?", 
                            choices=["Done"], carousel=True),
                            ]

                # get the answer form the prompt in a dictionary
                option = inquirer.prompt(questions)
                if option["Completed sinlge analysis"] == "Done":
                    continue
            elif answers["Stock Analysis Option"] == "Analysts Recommendations":
                print(stock.recommendations)
                
                # selecter from the terminal
                questions = [
                inquirer.List("Completed sinlge analysis", message="What about the stock do you want to analyse?", 
                            choices=["Done"], carousel=True),
                            ]

                # get the answer form the prompt in a dictionary
                option = inquirer.prompt(questions)
                if option["Completed sinlge analysis"] == "Done":
                    continue
            elif answers["Stock Analysis Option"] == "Next Event":
                print(stock.next_event)
                
                # selecter from the terminal
                questions = [
                inquirer.List("Completed sinlge analysis", message="What about the stock do you want to analyse?", 
                            choices=["Done"], carousel=True),
                            ]

                # get the answer form the prompt in a dictionary
                option = inquirer.prompt(questions)
                if option["Completed sinlge analysis"] == "Done":
                    continue
            elif answers["Stock Analysis Option"] == "New Stock":
                break
    
    elif stocked["Stock Analysis App"] == "Exit":
        break