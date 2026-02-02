def calculate(transactions):
    total_transactions = {  
        "revenue":{
            "Wages":0,
            "Other Income":0
        },

        "expenses":{
            "Rent":0,
            "Food":0,
            "Entertainment":0,
            "Utilities":0
        },

        "totals":{
            "Total Income":0,
            "Total Expenses":0,
            "Earnings Before Tax":0,
            "Net Income":0
        }
        
    }
    #Iterate through each transaction and categorize amounts
    for x in transactions:
        amount = x["amount"]
        category = x["category"]
        
        #Adds amount to appropriate category and totals
        if category in total_transactions["revenue"]:
            total_transactions["revenue"][category] += amount
            total_transactions["totals"]["Total Income"] += amount

        if category in total_transactions["expenses"]:
            total_transactions["expenses"][category] += amount
            total_transactions["totals"]["Total Expenses"] += amount

    
    #Calculate net total
    total_transactions["totals"]["Earnings Before Tax"] = total_transactions["revenue"]["Total Income"] - total_transactions["expenses"]["Total Expenses"]
    total_transactions["totals"]["Net Income"] = (total_transactions["totals"]["Earnings Before Tax"] - (total_transactions["totals"]["Earnings Before Tax"] * 0.0425)) #Assuming current Michigan tax rate of 4.25%
    
    return total_transactions

"""
        if category in total_transactions["categories"]:
            total_transactions["categories"][category] += amount 
        if amount > 0:
            total_transactions["totals"]["Income"] += amount
        if amount < 0:
            total_transactions["totals"]["Expenses"] += amount



            "categories":{
            "Food":0, 
            "Rent":0, 
            "Entertainment":0,
            "Utilities":0
        }


        #total_transactions["totals"]["Net"] = total_transactions["totals"]["Income"] + total_transactions["totals"]["Expenses"]
"""
