# Get details of loan

principal = float(input('Enter principal amount: '))  # 50000
rate_of_interest = float(input('Enter Rate of Interest: '))  # 3
monthly_payment = float(input('Enter EMI payable: '))  # 1000
months = int(
    input('How many months do you want to see the results for ?'))  # 24

monthly_rate = rate_of_interest/100/12

for i in range(months):
    interest_paid = principal * monthly_rate
    principal = principal + interest_paid
    if (principal - monthly_payment < 0):
        print('The last payment is', principal)
        print('You paid off the loan in', i+1, 'months')
    principal = principal - monthly_payment
    print('Paid ', principal, 'of which', interest_paid, 'was interest')
    print('Remaining balance', principal)
