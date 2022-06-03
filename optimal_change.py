# Write your solution here!
# calculate change required
# determine valid bill/coin values
# iterate from largest to smallest
# check for edge cases
# check for special cases?
# ensure proper grammer in output

def optimal_change(cost, amount_paid):
    #map currency options to values
    values = {
    '$100 bill': 100,
    '$50 bill': 50,
    '$20 bill': 20,
    '$10 bill': 10,
    '$5 bill': 5,
    '$1 bill': 1,
    'quarter': .25,
    'dime': .10,
    'nickel': .5,
    'penn': .01,
    }
    # edge cases:
    if cost <= 0:
        return (f'An item with a price of ${cost} is free!')  
    # determine change required:
    change = amount_paid - cost
    #print(change)
    # iterate to determine optimal change:
    currency = {}
    for i in values:
        while change >= values[i]:
            if i in currency:
                currency[i] += 1
            else:
                currency[i] = 1
            change -= values[i]
    currencies = {}
    # iterate over currency dictionary to check for plural
    for k, v in currency.items():
        if v == 1:
            currencies[k] = currency[k]
        else:
            if k == 'penn':
                currencies['pennies'] = v
                currencies[k + 's'] = currency[k]
                currencies.pop('penns')
            else:
                currencies[k + 's'] = currency[k]

    #generate output string
    cost = '{:.2f}'.format(cost)
    amount_paid = '{:.2f}'.format(amount_paid)
    output = f'The optimal change for an item that costs ${cost} with an amount paid of ${amount_paid} is '
    ## iterate over currencies and append to output
    for k, v in currencies.items():
        output = output + f'{v} {k}, '
    
    
    return(output)

print(optimal_change(31.51, 50))

# issues - pluralizing keys
# sub-type for penny/pennies
# variable length output string