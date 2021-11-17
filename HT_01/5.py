# Write a script to convert decimal to hexadecimal
# Sample decimal number: 30, 4
# Expected output: 1e, 04

n = int(input("number: "))
if n < 0:
    print(f"-{hex(n)[3:]}")
else:
    print(hex(n)[2:])

