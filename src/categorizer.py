def add_category(transaction):
    categories = {"Food":["grocery", "groceries", "target", "walmart", "restaurant"], 
                  "Rent":["rent"], 
                  "Entertainment":["netflix", "hulu", "disney", "amazon prime"],
                  "Utilities":["electricity", "gas", "water", "bill"],
                  "Wages":["paycheck", "salary"],
                  "Other Income":["refund", "rebate", "cashback", "gift"]
                }
    
    for x in transaction:
        description = x["description"].lower()
        for key, value_list in categories.items():
            #Check if current word in value_list matches the description and assign category
            if any(word_in_values in description for word_in_values in value_list):
                x["category"] = key
                break
        if "category" not in x:
            x["category"] = "Other"


"""
    for x in transaction:
        description = x["description"].lower()
        for key, value in categories.items():
            if description in value:
                x["category"] = key
                break
        if "category" not in x:
            x["category"] = "Other" 
"""

    