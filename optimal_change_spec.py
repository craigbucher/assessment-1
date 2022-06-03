# Write your tests here!
from optimal_change import optimal_change

print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print("3:", optimal_change(8.89, 10) == "The optimal change for an item that costs $8.89 with an amount paid of $10 is 1 $1 bill, 1 dime, and 1 penny.")
print("4:", optimal_change(12.34, 20) == "The optimal change for an item that costs $12.34 with an amount paid of $20 is 1 $5 bill, 2 $1 bills, 2 quarters, 1 dime, 1 nickel, and 1 penny.")
print("5:", optimal_change(12.34, 50) == "The optimal change for an item that costs $12.34 with an amount paid of $50 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 2 quarters, 1 dime, 1 nickel, and 1 penny.")
print("6:", optimal_change(64.79, 75.50) == "The optimal change for an item that costs $64.79 with an amount paid of $75.5 is 1 $10 bill, 2 quarters, 2 dimes, and 1 penny.")
print("7:", optimal_change(0, 50) == "An item with a price of $0 is free!")
print("8:", optimal_change(.01, 1) == "The optimal change for an item that costs $0.01 with an amount paid of $1 is 3 quarters, 2 dimes, and 4 pennies.")