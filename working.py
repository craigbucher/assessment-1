import math
def optimal_change(change):
    values = {
    '$100 bill': 100,
    '$50 bill': 50,
    '$20 bill': 20,
    '$10 bill': 10,
    '$5 bill': 5,
    '$1 bill': 1,
    'quarter': .25,
    'dime': .10,
    'nickel': .05,
    'penny': .01,
    }
    # create output variable
    #result = {}
    currency = {}
    # loop over map
    for i in values:
        while change >= values[i]:
            print(change, values[i])
            if i in currency:
                currency[i] += 1
            else:
                currency[i] = 1
            change -= values[i]
            change = math.trunc(change)
    return(currency)

print(optimal_change(1.11))