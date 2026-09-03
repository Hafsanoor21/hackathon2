def calculate(a, b):
    add= a + b
    sub= a - b
    mul= a * b
    return add, sub, mul
add_res,sub_res,mul_res = calculate(3,4)

print(f" addition: {add_res}")
print(f" subtraction: {sub_res}")
print(f" multiplication: {mul_res}")