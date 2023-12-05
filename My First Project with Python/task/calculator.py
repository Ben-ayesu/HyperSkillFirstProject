items_prices = {
    'Bubblegum': 202,
    'Toffee': 118,
    'Ice cream': 2250,
    'Milk chocolate': 1680,
    'Doughnut': 1075,
    'Pancake': 80
}


print('Earned amount:')
for key, value in items_prices.items():
    print(f'{key}: ${value}')
print(f'Income ${sum(items_prices.values())}')