# Apollos Eastman
# Oct 11 2024
# Carpet Calculator

print()
print('Thank you for using my Carpet Calculator!')

# State tax rate
SALES_TAX = 1.06

# Input
length = float(input('Enter the length of your room in feet:'))
width = float(input('Enter the width of your room in feet:'))
price_sq_yrd =  float(input('Enter the price of carpet per sqaure yard ($2.00-$4.50):\n'))

# If statement to see if inputted price is valid
if price_sq_yrd > 4.50 or price_sq_yrd < 2.00:
    print(f'Error, carpet price invalid. Please input a price between $2.00 and $4.50.')
else:
    # Calculating areas
    sq_feet = length * width
    sq_yards = sq_feet / 9

    # Calculating prices
    price = sq_yards * price_sq_yrd
    price_total = price * SALES_TAX

    # Output
    print(f'You will need to buy {sq_yards:.2f} square yards of carpet.\n')
    print(f'To buy {sq_yards:.2f} square yards of carpet it will cost ${price:.2f} before sales tax.\n')
    print(f'Your grand total including sales tax will be ${price_total:.2f}!')
