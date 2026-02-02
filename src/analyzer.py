def calculate(transactions):
    total_transactions = {  
        "totals":{
            "Income":0,
            "Expenses":0,
            "Net":0
        },
        "categories":{
            "Food":0, 
            "Rent":0, 
            "Entertainment":0,
            "Utilities":0}
    }

    for x in transactions:
        amount = x["amount"]
        category = x["category"]
        
        #Adds amount to appropriate category and totals
        if category in total_transactions:
            total_transactions["categories"][category] += amount 
        if amount > 0:
            total_transactions["totals"]["Income"] += amount
        if amount < 0:
            total_transactions["totals"]["Expenses"] += amount
    
    #Calculate net total
    total_transactions["totals"]["Net"] = total_transactions["totals"]["Income"] + total_transactions["totals"]["Expenses"]
    
    return total_transactions