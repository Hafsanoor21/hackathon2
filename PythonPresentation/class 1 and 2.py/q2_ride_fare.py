# Get the input.
distance = input("enter your distance")
base_fare = input("enter your base fare")
price_per_kilometer = input("enter the price per kilometer")

# Convert all three inputs to float values.
distance = float(input("enter your distance:"))
base_fare = float(input("enter your base fare:"))
price_per_kilometer = float(input("enter your price per kilometer:"))

# Calculate the total fare using.
Total_fare = base_fare + (distance * price_per_kilometer)

# Print the distance and final fare.
print(f"For a trip of {distance} km, your final fare is {Total_fare}.")