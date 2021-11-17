# Write a script to concatenate N strings.

result_str = ""
for i in range(0, int(input("n: "))):
    result_str += input(f"string #{i+1}: ")

print(result_str)
