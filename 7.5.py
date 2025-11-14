###
# Vehicle registration numbers in Krakow start
# with the letters KR or KK. Write a program that checks
# whether the vehicle registration number entered
# from the keyboard means a vehicle from Krakow.
# Print True whether a car is from Krakow or False otherwise.
#
car_number = input('Enter car registration number: ') 
if car_number[0:2] == "KR" or "KK":
    ex = "Car is from Krakow"
else:
    ex = "Car isn't from Krakow"
print(ex)