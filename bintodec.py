#program for binary to decimal


num = int(input("Enter any  number:"))
binval = num
decval = 0
base = 1


while num > 0:
    rem = num % 10
    decimal_val = decimal_val + rem * base
    num = num // 10
    base = base * 2

print("Binary Number is {} and Decimal Number is {}".format(binary_val, decimal_val))

