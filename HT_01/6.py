# Write a script to check whether a specified value is contained in a group of values.
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> (1, 5, 8, 3) : False

elem = input("input search element: ")
group = input("input group: ").split(', ')

print(elem in group)
