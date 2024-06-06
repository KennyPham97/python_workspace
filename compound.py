def main():
    starting_bal, monthly_cont, interest_rate, months_inv = get_info()
    total_acc_bal = calculate(starting_bal, monthly_cont, interest_rate, months_inv)
    print("\nTotal account balance:",f"${total_acc_bal:,}") #This \n forms a new line before total_account_balance is printed, then total_acc_balance is formatted as an f string, with a comma for the thousand numbers.

def get_info():
    starting_bal = int(input("What's your starting balance (dollars)? "))
    monthly_cont = int(input("What's your monthly contribution amount(dollars)? "))
    interest_rate = float(input("What's the annual interest rate(percent)? "))
    months_inv = int(input("How many months have you invested? "))
    return starting_bal, monthly_cont, interest_rate, months_inv

def calculate(sb, mc, ir, mv):
    total_acc_bal = sb #total_acc_bal to the starting balance
    monthly_interest = ir/12/100 #use the interest rate to calc the monthly ir
    for _ in range(mv):
        total_acc_bal += mc
        interest_payment = monthly_interest * total_acc_bal
        total_acc_bal += interest_payment
    return int(total_acc_bal)

main()


#this is an compounding interest calculator that takes in a user's starting balance, monthly contributions, interest rate and time invested to calculate their total balance after a period of time.