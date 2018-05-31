"""
    PAYE Calcuator
    Programmer: SAMUEL PELL
    Date:       06-01-17 (dd-mm-yy)
    Basic income tax calculator
"""

import PAYE_calculator as paye_funcs


QUIT_KEY = "Q"
HEADER = """                  Income Tax Calculator
By Samuel Pell
--------------------------------------------------------
Please enter commands in the form '<money> -<timespan>'
<timespan> codes are: 
                     'a' - annual
                     'w' - weekly
                     'f' - fortnightly
                     'm' - monthly
                     'n' - number - followed by a number
                                    of days paid for
<timespan> defaults to weekly
To exit input '{}'
--------------------------------------------------------""".format(QUIT_KEY)

OUTPUT = "Pay after tax ${:.2f}"
ERROR_NO_N_NUMBER = "-n requires a number of days to work on"


def decide_calculation(user_input):
    """Decision for middle option"""
    pay = float(user_input[0])
    choice = user_input[1][1:] #remove first "-" character
    pay_after_tax = round(pay - paye_funcs.calculate_PAYE(pay, choice), 2)
    
    print(OUTPUT.format(pay_after_tax))


def calculate_paye_on_days(usr_input):
    """Calculate the paye based on a period of days paid for"""
    days = int(usr_input[2])
    pay = float(usr_input[0])
    period = 364 / days

    pay_after_tax = round(pay - paye_funcs._calculate_PAYE(pay, period), 2)
    print(OUTPUT.format(pay_after_tax))
    

def parse_input(usr_input):
    """Main logic of program"""
    usr_input = usr_input.strip()
    
    if usr_input.upper() == QUIT_KEY: #exit logic
        return False
    else:
        usr_input = usr_input.split()
        if len(usr_input) == 1: #if only one argument supplied default to weekly
            
            pay = float(usr_input[0])
            pay_after_tax = round(pay - paye_funcs.calculate_PAYE(pay, "w"), 2)
            
            print(OUTPUT.format(pay_after_tax))
            
        elif len(usr_input) == 2: #two arguments check if expecting 3 arguments and calculate
            if usr_input[1] == '-n':
                print(ERROR_NO_N_NUMBER)
            else:
                decide_calculation(usr_input)
            
        elif len(usr_input) == 3:
            if usr_input[1] == '-n': 
                if usr_input[2].isnumeric():
                    calculate_paye_on_days(usr_input)
                else:
                    print(ERROR_NO_N_NUMBER)
        else:
            print(UNKNOWN_COMMAND)
        
        return True

def main():
    """Mainloop of the program"""
    running = True
    print(HEADER)

    while running:
        user_input = input("> ")
        running = parse_input(user_input) #exit logic




if __name__ == "__main__":
    main()