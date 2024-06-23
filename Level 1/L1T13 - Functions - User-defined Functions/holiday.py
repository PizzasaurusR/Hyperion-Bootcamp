#FUNCTIONS
#hotel_cost function to calculate total hotel cost based on num_nights and city_flight
def hotel_cost(x, y):

    hotel_rate = 0

    if  y == "Johannesburg":
        hotel_rate = 2000
    
    elif y == "Cape Town":
      hotel_rate = 2500

    elif y == "Durban":
      hotel_rate = 1500

    else:
      hotel_rate = 1000

    total_hotel_cost = x * hotel_rate
    return(total_hotel_cost)

#plane_cost func to calculate flight cost based on city_flight
def plane_cost(x):

    flight_cost = 0

    if  x == "Johannesburg":
        flight_cost = 1500
    
    elif x == "Cape Town":
      flight_cost = 1500

    elif x == "Durban":
      flight_cost = 1000

    else:
      flight_cost = 500

    return(flight_cost)

#car_rental func to calculate car rental based on rental_days. Daily rate is set at 250
def car_rental(x):

   rental_cost = x * 250

   return(rental_cost)

#holiday_cost function to calculate total holiday cost based on hotel_cost, plane_cost and car_rental
def holiday_cost(x, y, z):
   
   total_cost = x + y + z

   return(total_cost)
#-------------------------------------------------
city_flight = input("Please select your flight destination:\nJohannesburg\nCape Town\nDurban\nPort Elizabeth\n\n")
num_night = int(input("\nHow many days will your stay be?:\n"))
rental_days = int(input("\nHow many days will you be needing a car for?:\n"))

#Calculate total costs using functions and user input
flight_total_cost = plane_cost(city_flight)
car_rental_total_cost = car_rental(rental_days)
hotel_total_cost = hotel_cost(num_night, city_flight)
holiday_total_cost = flight_total_cost + car_rental_total_cost + hotel_total_cost

print("Thank you for your selection. The details for your holiday will be:\n")
print(f"Destination: {city_flight}")
print(f"Number of days staying: {num_night}")
print(f"Number of days car rental: {rental_days}")
print(f"Flight to {city_flight}: R{flight_total_cost}")
print(f"Hotel cost: R{hotel_total_cost}")
print(f"Rental Cost: R{car_rental_total_cost}\n")
print("------------------------------------------------------------")
print(f"Total holiday cost: R{holiday_total_cost}")