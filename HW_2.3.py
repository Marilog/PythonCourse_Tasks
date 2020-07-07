#3.task


var_1 = int(input("Insert the value of the first variable:"))
var_2 = int(input("Insert the value of the second variable:"))

var_1, var_2 = var_2, var_1

print("Swapped first variable is ", var_1)
print("Swapped second variable is ", var_2)
