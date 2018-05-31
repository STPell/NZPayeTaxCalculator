"""
   Tax Refund Calculator
   Programmer: Samuel Pell
   Date:       10-02-17 (DD-MM-YY)
   Calculates whether someone is due a refund on their PAYE income tax
"""

import PAYE_calculator as paye_funcs

def calculate_refund(income_to_date, tax_paid_to_date):
    """Calculates the difference between tax paid and tax that
       should be paid"""
    
    correct_tax = paye_funcs.calculate_PAYE(income_to_date, "a")
    
    return round(tax_paid_to_date - correct_tax, 2)


def main():
    """Main logic of the program"""
    income_to_date = input("Please enter Gross Taxable Income: $")
    tax_paid = input("Please enter Tax Paid:             $")
    
    try:
        income_to_date = float(income_to_date)
        tax_paid = float(tax_paid)
    except TypeError:
        print("Error restart program")
    else:
        refund = calculate_refund(income_to_date, tax_paid)
        
        if refund < 0:
            print("Oh noes!!! You have underpaid by ${:.2f}".format(abs(refund)))
        elif refund == 0:
            print("Sorry, no refund this year. Maybe next year?")
        else:
            print("Congrats you've overpaid on your PAYE!! You'll get a refund of ${:.2f}".format(refund))
            
            
if __name__ == "__main__":
    main()