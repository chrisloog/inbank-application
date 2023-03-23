CREDIT_MODIFIERS = {
    49002010965: 0,
    49002010976: 100,
    49002010987: 300,
    49002010998: 1000,
}

MAX_LOAN_AMOUNT = 10000
MIN_LOAN_AMOUNT = 2000
MAX_LOAN_PERIOD = 60
MIN_LOAN_PERIOD = 12


def calculate_credit_score(personal_code, loan_amount, loan_period):
    credit_modifier = CREDIT_MODIFIERS.get(personal_code, 0)
    if credit_modifier == 0:
        return 0  # person has debt, return credit score of 0
    credit_score = (credit_modifier / loan_amount) * loan_period
    return credit_score


def is_loan_amount_valid(loan_amount):
    return MIN_LOAN_AMOUNT <= loan_amount <= MAX_LOAN_AMOUNT


def is_loan_period_valid(loan_period):
    return MIN_LOAN_PERIOD <= loan_period <= MAX_LOAN_PERIOD


def get_max_loan_amount(personal_code, loan_period):
    for max_loan_amount in range(MAX_LOAN_AMOUNT, MIN_LOAN_AMOUNT - 1, -1):
        credit_score = calculate_credit_score(personal_code, max_loan_amount, loan_period)
        if credit_score >= 1:
            return max_loan_amount
    return 0


def check_different_loan_period(personal_code, loan_amount):
    for loan_period in range(MIN_LOAN_PERIOD, MAX_LOAN_PERIOD + 1):
        credit_score = calculate_credit_score(personal_code, loan_amount, loan_period)
        if credit_score >= 1:
            return loan_period
    return 0


def decision_engine(personal_code, loan_amount, loan_period):
    if not is_loan_amount_valid(loan_amount):
        return "Loan amount needs to be between €2,000 and €10,000."

    if not is_loan_period_valid(loan_period):
        return "Loan period needs to between 12 and 60 months."

    credit_modifier = CREDIT_MODIFIERS.get(personal_code, 0)
    if credit_modifier == 0:
        return "Person has debt and therefore does not qualify for a loan."

    max_loan_amount = get_max_loan_amount(personal_code, loan_period)
    if max_loan_amount == 0:
        loan_period = check_different_loan_period(personal_code, loan_amount)
        if loan_period != 0:
            return f"Decision: Approved\nLoan amount: {loan_amount}€\nLoan period: {loan_period} months"
    else:
        return f"Decision: Approved\nLoan amount: {max_loan_amount}€\nLoan period: {loan_period} months"

    return "Did not find a suitable loan period for the requested loan amount. Please try with a lower amount."
