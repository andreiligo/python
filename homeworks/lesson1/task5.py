profit = float(input('Please enter profit of your company: '))
costs = float(input('Please enter costs of your company: '))
clear_profit = profit - costs
if profit > costs:
    profitability = clear_profit / profit * 100
    print('Company is working in profit, your profitability is {0}%'.format(profitability))
elif profit < costs:
    print('Work harder! You are loosing the money!!!')
elif profit == costs:
    print('Stay on your place, seams you like it:D, sure work harder dead sugar')
employees_number = int(input('How many worker are in your company?: '))
profit_per_employee = round(clear_profit // employees_number)
print('Index of clear profit per every employee is {0}$'.format(profit_per_employee))
