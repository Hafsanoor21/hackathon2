# funcation in puthon :
# normal funcation :
def sayshi():
    print("Hi")
    print("Hi Ai Skool")

# sayshi():

def do_something ():
    a = 10
    b = 20
    print("a is :",a)
    print("b is :",b)

# do something.()

def sayhello():
    "sayhi"()
    print("hello")
    do_something()
    print("hello funcation end")

# sayhello()

#  funcation with peremeter.

def sayhi(name):
    print("hello :",name)

# sayHi("hafsa").
def add_three_numbers(a,b,c): # a=4, b=3, c=9
    result = a+b+c
    print("sum is:",result)

user_first_number= int(input("enter first number:"))
user_second_name = int(input("enter second number:"))
user_third_number= int(input("enter third number:"))

add_three_numbers("user_first_number,user_second_number,user_third_number")


# funcation with return keywords:

def sayhi(name):
    output = "Hi" + name  
    return output

#  a = sayhi("hafsa")
# print(a)
def is_age_greater_ten(age):
    if age > 10 :
        return True
    else:
        return False


isagegreaterthanten = "is_age_greater_then"(8)
# print(is age greater then ten)

