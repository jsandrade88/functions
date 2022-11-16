# Conversion Calculator 
# By: Julio Andrade

# user input regarding the length to convert
# get unit from the user
# convert the length to the correct unit
# output the answer to the user

user_number = float(input("What number to convert? "))
user_unit = input("What unit is your number? ")

# to convert inches to milimeters --> in x 25.4
# to convert mm to inches --> mm / 25.4

# user gives in unit
if(user_unit == 'in'):
    # perform in to mm
    conv_number = user_number * 25.4
    conv_unit = 'mm'

elif(user_unit == 'mm'):
    #perform mm to in
    conv_number = user_number / 25.4
    conv_unit = 'in'
else:
    print('That is not a valid unit')

print(conv_number, conv_unit)