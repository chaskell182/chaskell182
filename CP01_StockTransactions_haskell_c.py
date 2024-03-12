'''

Christopher Haskell
Jan 25, 2024
ISCS 210 Python Programming
Filename:CP01_StockTransactions_Haskell_C.py
Description of the program: This program will calculate stock purchasing/selling
price and commssion, as well as profit or loss on the sale 

Algorithm:
Input: What am I inputting and how
The number of shares that Joe purchased (2,000)
Stock price ($40)
Commision paid to his breaker(3%)

Sold 2,000 shares
Sold at $42.75 per share
Another 3 % commission 


Processing: Calculations
Amount of money Joe paid: share_amount = float(input('How Many shares did you purchase? ')
purchase_price = float(input('What was the cost per share in dollars? ')
Commission amount commission = total_cost * .03
Amount Joe sold the stock for
Amount commission paid on the sale
How much Joe had left over after the sale and commision




Output:
Clear and easy to read values
How much joe purchased the stocks for
What he sold them for
The commission amounts
total profit 

'''

print('\nThis program will calculate the total purchase cost and')
print('commission totals on stock purchases and sales')



print('\nFollow the prompts on the screen')


#User inputs amount of shares purchased

shares_bought = float(input('\nHow many shares were purchased? '))

#User enters the purchase price per share
purchase_price = float(input('\nWhat was the cost per share in dollars? '))

#Calculates the total cost of the purchase
total_cost = float(shares_bought * purchase_price)



print(f'\nThe stock was purchased for ${total_cost:.2f}')


#Converts inputted percent into usable percentage

commission_percent = float(input('\nWhat is the commission percentage owed on the purchase? '))

#divide input by 100 to get percentage, then multiply by purchase cost 
percent = commission_percent / 100


p_commission = percent * total_cost


print(f'\nThe amount of commission paid on the purchase is ${p_commission:.2f}')

print('\nNow please enter the sale data:')

#user can now enter the sale data

shares_sold = float(input('\nHow many shares did you sell? '))

sell_price = float(input('\nWhat was the selling price per share in dollars? '))

total_sale = shares_sold * sell_price

print(f'\nThe stocks sold for ${total_sale:.2f}')

commission_sale_percent = float(input('\nWhat was the commission percentage on the sale? '))

#user can enter any percentage

sale_percent = commission_sale_percent /100

sale_commission = sale_percent * total_sale

print(f'\nThe commission paid on the sale is ${sale_commission:.2f}')

#calculating total profit, need to subtract all values from the sale price

total_profit = total_sale - total_cost - sale_commission - p_commission

#if positive it will print profit
#if negative will print loss

if(total_profit > 0):
    print(f'\nThe total profit on the sale is ${total_profit:.2f}')

if(total_profit < 0):
    print(f'\nThe total loss on the sale is ${total_profit:.2f}')




                           
                           
                
