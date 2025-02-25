name = input("What's your name?")
print("Hello "+name)

height = float(input("Whats your height? "))
height_inches="{:.2f}".format(height/2.54)  # string.format, {} place holder
print(type(height))
print(type(height_inches))
print("You are "+str(height)+ " cm")
print("You are "+height_inches+ " inches tall")


name = input("Name: ")
email = input("Email Id: ")
phone = input("Phone Number: ")

print("*" * 30)
print("UserName: "+name)
print("Email: "+email)
print("Ph: "+phone)
print("*" * 30)
