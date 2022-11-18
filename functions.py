# Conversion Calculator 
# By: Julio Andrade

# user input regarding the length to convert
# get unit from the user
# convert the length to the correct unit
# output the answer to the user
while True:
    while True:
        user_number = input("What number to convert? ")
        if user_number.isdigit():
            user_number = float(user_number)
            break
        else:
            print('please use a number')
    
    
    
    user_unit = input("What unit is your number? ")

    # user gives in unit
    if(user_unit == 'in'):
        # perform in to mm
        conv_number = user_number * 25.4
        conv_unit = 'mm'
        break

    elif(user_unit == 'mm'):
        #perform mm to in
        conv_number = user_number / 25.4
        conv_unit = 'in'
        break
    else:
        print('That is not a valid unit')

print(conv_number, conv_unit)