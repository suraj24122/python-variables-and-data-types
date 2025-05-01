# Convert a float to an integer and a string to an integer (e.g., "123" → 123). Try converting "abc" to an integer — what happens?

f_value = 3.14;
con_value = int(f_value)
print("Converting float value into integer value and type is  = ",f_value,type(con_value))

s_value = "123"
con1_value = int(s_value)
print("Converting string value into integer value and type is  = ",s_value,type(con1_value))

s1_value = "abc"
con2_value = int(s1_value)
print("Converting String value into integer see what happens = ",s1_value,type(con2_value))