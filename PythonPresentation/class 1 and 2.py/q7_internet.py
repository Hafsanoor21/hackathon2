# Get input data.
package_code = input("enter the package code(B,S or P):")
# add match\case data.
match package_code :
    case "B":
        print("Basic 20 GB") 
    case "S":
        print("Standard 60 GB")
    case "p":
        print("premium 150 GB")
    case _:
        print("invalid package code")






