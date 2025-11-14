price = input('Enter price of your product: ')
price = float(price)
discount = input('Enter discount of your product: ')
discount = int(discount)
discount = discount/100
promo = price-price*discount
reuction = price-promo
print(f'Price with discount:{promo}')
print(f'Reduction: {round(reuction,2)}')