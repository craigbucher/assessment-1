# Write your solution here!
# calculate change required
# determine valid bill/coin values
# iterate from largest to smallest
# check for edge cases
# ensure proper grammer in output

def optimal_change(cost, amount_paid):
    #create result variable
    change = ''
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
    'penny': .1,
    }
    
    # determine change required
    change = amount_paid - cost

    return(change)

print(optimal_change(75.00, 100))