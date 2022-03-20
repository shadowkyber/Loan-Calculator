import math
import argparse


arg = argparse.ArgumentParser()

arg.add_argument("--type", choices=["annuity", "diff"])
arg.add_argument("--principal", type=int)
arg.add_argument("--periods", type=int)
arg.add_argument("--interest", type=float)
arg.add_argument("--payment", type=int)

p = arg.parse_args()

total = 0

if p.interest is None:
    print("Incorrect parameters.")

elif p.type == "diff":  # calculating diff
    i = p.interest / (12 * 100)
    for m in range(1, p.periods+1):
        d = (p.principal / p.periods) + i * (p.principal - (p.principal * (m - 1)) / p.periods)
        d = math.ceil(d)  # rounds answer up
        print(f"Month {m}: payment is {d}")
        total += d
    print()
    print('Overpayment =', total - p.principal)

elif p.type == "annuity":  # calculating annuity
    if p.principal is None:  # calculate principal
        i = p.interest / (12 * 100)
        principal = p.payment / ((i * (1 + i) ** p.periods) / ((1 + i) ** p.periods - 1))
        principal = int(principal)
        over = p.periods * p.payment - principal
        print(f"Your loan principal = {principal}!")
        print('Overpayment =', over)

    elif p.periods is None:  # calculate periods
        i = p.interest / (12 * 100)
        n = math.log((p.payment / (p.payment - i * p.principal)), 1 + i)
        years = n // 12
        months = math.ceil(n - years * 12)
        years = int(years)
        if months == 12:
            years += 1
            months = 0
            print(f"It will take {years} years to repay this loan!")
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
        over = ((years * 12) + months) * p.payment - p.principal
        print('Overpayment =', over)

    elif p.payment is None:  # calculate payment
        i = p.interest / (12 * 100)
        payment = p.principal * (i * (1 + i) ** p.periods) / ((1 + i) ** p.periods - 1)
        payment = math.ceil(payment)
        over = abs(p.principal - (payment * p.periods))
        print(f"Your annuity payment = {payment}!")
        print('Overpayment =', over)

# python creditcalc.py
# cd C:\Users\pro\Documents\programs\jetbrains_academy\Loan Calculator\Loan Calculator\task\creditcalc
