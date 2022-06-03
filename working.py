def optimal_change(num):
    number_map = {
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
    # create output variable
    result = ''
    # loop over map
    for i in number_map:
        while num >= number_map[i]:
            result += i
            num -= number_map[i]
    return(result)

print(optimal_change(25))