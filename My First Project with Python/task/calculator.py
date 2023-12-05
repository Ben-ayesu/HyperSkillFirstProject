items_prices = {
    'Bubblegum': 202,
    'Toffee': 118,
    'Ice cream': 2250,
    'Milk chocolate': 1680,
    'Doughnut': 1075,
    'Pancake': 80
}

def earned_amount():
    print('Earned amount:')
    for key, value in items_prices.items():
        print(f'{key}: ${value}')
    print()

def net_income():
    Income = sum(items_prices.values())
    print(f'Income: ${Income}')
    staff_expenses = input('Staff expenses:')
    other_expenses = input('Other expenses:')
    print(int(staff_expenses) + int(other_expenses))
    print(f'Net income: ${Income - (int(staff_expenses) + int(other_expenses))}')

earned_amount()
net_income()