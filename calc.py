# x = int(input("What's starting capital? "))
# y = float(input("What's the annual interest rate? "))
# a = int(input("What's your monthly contribution? "))
# m = int(input("How many months are you investing? "))

# balance_pre_interest = int((x+a))
# monthly_interest_rate = (y/100/12)
# interest_payment = (monthly_interest_rate*balance_pre_interest)
# balance_post_interest = (balance_pre_interest * monthly_interest_rate + balance_pre_interest)


# total_balance = (balance_post_interest* (m*monthly_interest_rate) + balance_post_interest)

# print("This is your total balance:", total_balance)

#So the flaw of the program above is that it only calculates based on initial inputs. There needs to be a loop to update the balance and recalculate the interest every month.

x = int(input("What's your starting capital(dollar amount)? "))
y = float(input("What's the annual interest rate? "))
a = int(input("What's your monthly contribution amount? "))
m = int(input("How many months are you investing? "))

monthly_interest_rate = (y/100/12)
total_balance = x

for month in range(m):
    total_balance += a
    interest_payment = total_balance * monthly_interest_rate
    total_balance += interest_payment
    
print ("You will have",int(total_balance),"dollars after", m,"months of investing.")