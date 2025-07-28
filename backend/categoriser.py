def categorise_transactions(transactions):
    for tx in transactions:
        desc = tx.get("description", "").lower()
        if "uber" in desc:
            tx["category"] = "Transport"
        elif "payment" in desc:
            tx["category"] = "Income"
        elif any(x in desc for x in ["tesco", "asda", "grocery"]):
            tx["category"] = "Groceries"
        else:
            tx["category"] = "Other"
    return transactions
