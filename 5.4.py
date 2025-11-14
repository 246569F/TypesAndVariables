price = input('Cost of a product: ')
price = float(price)
vat = price*0.23
vat = round(vat, 2)
print(f'Vat={vat}')