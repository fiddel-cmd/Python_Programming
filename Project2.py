# variables
distance_mi = 1
# variable with bool condition not raining 
is_raining = False
#variable with a bool condition do not have a bike
has_bike = False
# variable with a bool condition doesn't have a car
has_car = False
# variable with a bool condition doesn't have a ride app.
has_ride_share_app = False

#Check if distance is not  1 and then print False.
if not distance_mi:

    print(False)

# check if distance is less than or equal to 1 and it is not raining and then print True.
elif distance_mi <= 1 and not is_raining:

    print(True)
    
 # check if the distance is less than or equal to 1  and  is raining the print False.
elif distance_mi <= 1 and is_raining:

    print(False)
# check if distance is between 1 (excluded) and 6(include) and is raining while their is no bike then print False.
elif 1 < distance_mi <= 6 and is_raining and not has_bike:

    print(False)
    
#check if distance is between 1 (excluded) and 6(included) and their is no rain print False.
elif  1 < distance_mi <= 6 and not is_raining:

    print(False) 
    
#check if distance is between 1(included) and 6(excluded),their is a bike and their is no rain then print True
elif 1 < distance_mi <=6 and has_bike and not is_raining:
    print(True)
    
elif 1 < distance_mi <= 6 and has_bike and is_raining:
    print(False)

    

elif distance_mi > 6 and has_car :
    print(True)
elif distance_mi > 6 and has_ride_share_app:
    print(True)
            
elif distance_mi > 6 and not has_car and not has_ride_share_app:

    print(False)

else:

    print("None of the conditions matched!") 

        

