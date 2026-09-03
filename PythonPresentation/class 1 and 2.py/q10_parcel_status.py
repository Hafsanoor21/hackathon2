# Step 1: Create a dictionary containing tracking_id, destination, and status
parcel = {
    "tracking_id": "TRK12345",
    "destination": "New York",
    "status": "Packed"
}
# enter a new status: Packed, Shipped or Delivered.
new_status = input("enter new status (packed,shipped or delivered):")

# Update the dictionary's status value with the user's input.
parcel ["status"] = new_status

# Use match/case.
match parcel["status"]:
    case "Packed":
        print("Your item is in the warehouse and ready to go.")
    case "Shipped":
        print("Your item is currently on its way!")
    case "Delivered":
        print("Your item has safely arrived at its destination.")
    case _:
        print("Unknown status entered.")

# Step 5: Print the updated dictionary
print("\nUpdated Record:")
print(parcel)