'''
Lab 2 problem 4:
Name: Emma J. Verdugo
lab: @2pm
'''
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
    price_change = current_price - last_month_price
    monthly_m = float(current_price * 0.051) / 12
    
    print( 'Current price for this house is $' + str(current_price) + '.' + ' The change in price is $' + str(price_change) + ' since last month.' + '\n' + 'The estimated mortgage is $' + f'{monthly_m:.2f}')
if __name__ == "__main__":
   real_estate()