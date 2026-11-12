import re

CATEGORIES = {"P": "Individual", "C": "Company", "H": "HUF", "F": "Firm"}

_INCOME_RE = re.compile(r"[0-9]+(,[0-9]+)*")
_PAN_RE = re.compile(r"[A-Z]{5}[0-9]{4}[A-Z]")

def parse_income(income):
    if not isinstance(income, str):
        raise ValueError("Income must be a string")
    income = income.strip()
    if not _INCOME_RE.fullmatch(income):
        raise ValueError("Income must be digits, optionally comma-separated")
    return int(income.replace(',', ''))

def monthly_emi(details):
    if not isinstance(details, str):
        raise ValueError("Details must be a string")
    parts = [p.strip() for p in details.split(',')]
    if len(parts) != 3 or not all(re.fullmatch(r"[0-9]+", p) for p in parts):
        raise ValueError("Expected 'principal,rate,years' as non-negative integers")
    principal, rate, years = map(int, parts)
    if not (0 < principal <= 10**12):
        raise ValueError("Principal out of range")
    if not (0 <= rate <= 100):
        raise ValueError("Rate out of range")
    if not (0 < years <= 50):
        raise ValueError("Years out of range")
    n = years * 12
    if rate == 0:
        return round(principal / n, 2)
    r = rate / 1200
    factor = (1 + r) ** n
    return round(principal * r * factor / (factor - 1), 2)

def pan_category(pan):
    if not isinstance(pan, str):
        raise ValueError("PAN must be a string")
    pan = pan.strip().upper()
    if not _PAN_RE.fullmatch(pan):
        raise ValueError("PAN must match format AAAAA9999A")
    category = CATEGORIES.get(pan[3])
    if category is None:
        raise ValueError("Unrecognised PAN category letter")
    return category

def main():
    print("==== Running parse_income ====")
    user_input = input("Enter monthly income (e.g. 50,000): ")
    try:
        print("Income:", parse_income(user_input))
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running monthly_emi ====")
    user_input = input("Enter principal,rate,years (e.g. 500000,10,5): ")
    try:
        print("Monthly EMI:", monthly_emi(user_input))
    except ValueError as e:
        print("Invalid input:", e)

    print("\n==== Running pan_category ====")
    user_input = input("Enter a PAN number (e.g. ABCPE1234F): ")
    try:
        print("PAN Category:", pan_category(user_input))
    except ValueError as e:
        print("Invalid input:", e)

if __name__ == "__main__":
    main()