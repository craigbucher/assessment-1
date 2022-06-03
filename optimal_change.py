# Write your solution here!
# calculate change required
# determine valid bill/coin values
# iterate from largest to smallest
# check for edge cases
# check for special cases?
# ensure proper grammer in output

def optimal_change(cost, amount_paid):
    cost = float("{:.2f}".format(cost))
    amount_paid = float("{:.2f}".format(amount_paid))
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
    'penny': .01,
    }
    # edge cases:
    if cost <= 0:
        return (f'An item with a price of ${cost} is free!')  
    # determine change required:
    change = amount_paid - cost
    # iterate to determine optimal change:
    currency = {}

    for i in values:
        while change >= values[i]:
            #print(i)
            if i in currency:
                currency[i] += 1
            else:
                currency[i] = 1
            change -= values[i]
    return(currency)

    

print(optimal_change(75, 100))