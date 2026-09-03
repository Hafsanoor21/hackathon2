# Get input data.
temprature = float(input("enter the temprature:"))
is_raining = input("is it raining?(yes\no):")
# add contions.
if temprature <15 and is_raining == "yes":
    print("wear a warm raincoat.")
elif temprature >=15 and is_raining == "no":
    print("wear a light raincoat.")
else:
    print("it is not raining enjoy your day!")








