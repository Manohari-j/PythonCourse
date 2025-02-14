otp=78123
print("your otp is "+ str(otp))  # temporary type cast
print(type(otp))
otp=str(otp)
print(type(otp))
# In python, it is class int/ class str instead of data type int/str
# python is oop

count="20.5"
print(int(float(count))+1)  # no rounding during type cast


name="Mano"
days = 15
year = 2025

print("Dear "+name+",\nYou have "+str(days)+" days of leave balance for this \nyear("+str(year)+").")
