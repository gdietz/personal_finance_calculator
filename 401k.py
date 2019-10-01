#!/usr/bin/env python3

import math

def get_percent_salary():
    contributions_limit = float(input("Contribution Limit: "))
    gross_salary_per_pay_period = float(input("gross salary per pay period: "))
    contributions_to_date = float(input("Contributions to Date: "))
    remaining_pay_periods = float(input("Remaining Pay Periods: "))

    allowed_contrib_amount_remaining = contributions_limit - contributions_to_date
    percent = (allowed_contrib_amount_remaining / remaining_pay_periods) / gross_salary_per_pay_period
    return percent

if __name__ == "__main__":
    percent = get_percent_salary()
    print(f"Percent: {percent:.2%}")