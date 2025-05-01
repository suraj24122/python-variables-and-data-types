# Swap two numbers using a third variable and then without using a third variable.

first_var = 20
sec_var = 21
temp_var = 0;

print("Before swapping the 1st variable = ",first_var)
print("Before swapping the 2nd variable = ",sec_var)

temp_var = first_var
first_var = sec_var
sec_var = temp_var

print("After swapping first var = ",first_var)
print("After swapping second var = ",sec_var)