with open("/LogicFirst/myfile.txt") as f:
    print(f.read())
# file automatically closes while using with to open a file
print(f.closed)

txt = "I am learning python"
with open("/LogicFirst/myfile.txt", 'w') as f:
    f.write(txt)

with open("/LogicFirst/myfile.txt", 'a') as f:
    f.write("Appending a text")