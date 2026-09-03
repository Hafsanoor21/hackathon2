# travel_bag_weight_checker.
# input travel class and bag weight.
travel_class = input("enter your travel class(economy\bussiness)")
bag_weight = float(input("enter your bag weight"))

# Use match/case to choose the limit.
match travel_class :
    case "economy":
        weight_limit=23
    case "bussiness":
        weight_limit=32

# Use if/else to check if the weight is allowed.
if bag_weight <=weight_limit:
    print("accepted")
else :
    print("over_weight")

