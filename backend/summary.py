def generate_summary(transactions):
    income = sum(tx["amount"] for tx in transactions if tx.get("category") == "Income")
    expenses = sum(-tx["amount"] for tx in transactions if tx["amount"] < 0)
    surplus = income - expenses
    return {
        "total_income": income,
        "total_expenses": expenses,
        "surplus": surplus,
        "health_score": round((surplus / income) * 100, 2) if income > 0 else 0
    }
