def calculate_credit_score(personal_code, loan_amount, loan_period):
    """
    Calculates the credit score of a person based on their personal code, loan amount and loan period
    """
    credit_modifier_map = {
        49002010976: 100,
        49002010987: 300,
        49002010998: 1000
    }
    credit_modifier = credit_modifier_map.get(personal_code, None)
    if credit_modifier is None:
        return 0  # person has debt, return credit score of 0
    credit_score = (credit_modifier / loan_amount) * loan_period
    return credit_score


def decision_engine(personal_code, loan_amount, loan_period):
    """
    Determines the maximum loan amount that can be approved based on the person's credit score
    """
    # Enforce minimum and maximum loan amount and period constraints
    loan_amount = max(loan_amount, 2000)
    loan_amount = min(loan_amount, 10000)
    loan_period = max(loan_period, 12)
    loan_period = min(loan_period, 60)

    # Calculate credit score based on personal code, loan amount and loan period
    credit_score = calculate_credit_score(personal_code, loan_amount, loan_period)

    # Check if the loan can be approved based on the credit score
    if credit_score >= 1:
        return 'positive', loan_amount

    # Find the maximum loan amount that can be approved
    while loan_amount > 2000:
        loan_amount -= 1000
        credit_score = calculate_credit_score(personal_code, loan_amount, loan_period)
        if credit_score >= 1:
            return 'positive', loan_amount

    # Find a new suitable period if loan amount cannot be found
    while loan_period < 60:
        loan_period += 12
        credit_score = calculate_credit_score(personal_code, loan_amount, loan_period)
        if credit_score >= 1:
            return 'positive', loan_amount, loan_period

    # Unable to find suitable loan amount and period
    return 'negative', 2000


if __name__ == '__main__':
    print(decision_engine(49002010976, 4000, 12))
