base_price =  15
age = 21
seat_type = 'Gold'
show_time = 'Evening'
if  age > 17 :
    print ('User is eligible to book a ticket')
if age >= 21:
    print('User is eligible for Evening shows')
else:
    print ('User is not eligble for Evening shows')

is_member =  False  
is_weekend = False

discount = 0
if is_member and age >= 21:
    discount = 3
    print("Userqualifies for membership discount")
else:
    print('User does not qualifyb for  Membership discount')
print(f'Discount : {discount}')
extra_charges =  0
if show_time == 'Evening' or is_weekend:
    extra_charges = 2
    print('Extra charges will be applied.')
else:
    print ("No extra charges will be applied")    
print(f"Extra charges: {extra_charges}")

if age >= 21 or age >= 18 and show_time != "Evening":
    print('Ticket booking condition satisfied')
else:
    print('Ticket booking failed due to restrictions')
if age >= 21 :
    print("Ticket booking condition satisfied")
else:
    print('Ticket booking failed due to restrictions')