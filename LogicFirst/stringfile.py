# message = "happy birthday"
# name = 'Mano'
# quote='"Testing"'
# print(quote)
# msg = message+name
# num = "12345"
# String has many methods
# functions/methods-performs specified tasks
# Function can be called directly
# but methods need variable/object to invoke it using dot operator
# print is function, upper is method
# print(name.upper())
# print(name.lower())
# print(message.title())  # first letters to caps
# print(message + ' ' + name)  # concatenate
# print("Multi \n line")  # \escape sequences - \n, \t
# print(len(message))
# print(message.find('i'))  # returns -1 if not present
#
# print(message.count("p"))
# print(message.replace('a','o'))
# print(message.isalpha()) # has space
# print(num.isdigit())
#
# print(message*10)

# split and join in strings

s="abc,def,ghi,jkl"
l=s.split(',')
print(l)

sjoin = '-'.join(l)
print(sjoin)
