def add_category(transaction):
    categories = {"Food":["grocery", "target", "walmart", "restaurant"], 
                  "Rent":["rent"], 
                  "Entertainment":["netflix", "hulu", "disney", "amazon prime"],
                  "Utilities":["electricity", "gas", "water", "bill"],
                  "Income":["paycheck", "salary"], 
                  "Other":["miscellaneous", "other", "misc"]}

    for x in transaction:
        description = x["description"].lower()
        for key, value in categories.items():
            if description in value:
                x["category"] = key
                break
            else:
                x["category"] = "Other"