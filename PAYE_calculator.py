"""
    PAYE Calcuator
    Programmer: SAMUEL PELL
    Date:       26-11-16 (dd-mm-yy)
    A calulator of PAYE tax
"""

ACC_MAX = 122063
ACC_LEVY_RATE = 1.39 #in %
TAX_BRACKETS = [14000, 48000, 70000]
TAX_RATES = [10.5, 17.5, 30, 33] #for each bracket in %

#Convert from % to multipliers
TAX_RATES= [(tax_rate / 100) for tax_rate in TAX_RATES]
ACC_LEVY_RATE = ACC_LEVY_RATE / 100

UNKNOWN_PERIOD = "Unknown time period code '{}'."


def _calculate_income_tax(annual_income):
    """Calculates annual income tax"""
    if annual_income <= TAX_BRACKETS[0]:
        ##tax on first bracket
        tax_paid = (annual_income * TAX_RATES[0])
        
    elif annual_income <= TAX_BRACKETS[1]:
        ##tax on second bracket
        tax_paid = (TAX_BRACKETS[0] * TAX_RATES[0]) #fist brackets tax
        tax_paid += (annual_income - TAX_BRACKETS[0]) * TAX_RATES[1]
        
    elif annual_income <= TAX_BRACKETS[2]:
        ##tax on third bracket
        tax_paid = TAX_BRACKETS[0] * TAX_RATES[0]  #first brackets tax
        tax_paid += (TAX_BRACKETS[1] - TAX_BRACKETS[0]) * TAX_RATES[1] #second brackets tax
        tax_paid += (annual_income - TAX_BRACKETS[1]) * TAX_RATES[2]
        
    else:
        ##tax on fourth bracket
        tax_paid = TAX_BRACKETS[0] * TAX_RATES[0]  #first brackets tax
        tax_paid += (TAX_BRACKETS[1] - TAX_BRACKETS[0]) * TAX_RATES[1] #second brackets tax
        tax_paid += (TAX_BRACKETS[2] - TAX_BRACKETS[1]) * TAX_RATES[2] #third brackets tax
        tax_paid += (annual_income - TAX_BRACKETS[2]) * TAX_RATES[3]
        
    return tax_paid


def _calculate_ACC_levy(annual_income):
    """Calculate ACC levy on annual income"""
    if annual_income < ACC_MAX:
        levy = annual_income * ACC_LEVY_RATE
    else:
        levy = ACC_MAX * ACC_LEVY_RATE
    
    return levy


def _calculate_PAYE(period_income, period):
    """Calculate PAYE tax to pay for income (period_income) over a period of time.
       This period of time is a subdivision of a year
    """
    predicted_annual_income = period * period_income
        
    income_tax = _calculate_income_tax(predicted_annual_income)
    acc_levy = _calculate_ACC_levy(predicted_annual_income)
    
    total_tax_paid = income_tax + acc_levy
    
    return round(total_tax_paid / period, 2)
        

def calculate_PAYE(income, time_period="w"):
    """A wrapper function for _calculate_PAYE.
       time_period is a code for a period of a year passed in as a string
           "a" - annual
           "m" - monthly
           "f" - fortnightly (2 weeks)
           "w" - weekly
       income is the ammount of income over this period. The default period
       is weekly."""
    if time_period == "w":
        return _calculate_PAYE(income, 52)
    elif time_period == "m":
        return _calculate_PAYE(income, 12)
    elif time_period == "f":
        return _calculate_PAYE(income, 26)
    elif time_period == "a":
        return _calculate_PAYE(income, 1)
    else:
        raise Exception(UNKNOWN_PERIOD.format(time_period))