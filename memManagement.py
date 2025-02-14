# RAM - Stack and Heap
# var name in stack and obj value in heap. If same obj then diff var points to same obj value

#


# increases the ref count.
# Ref count based garbage collector:
# if ref count is 0 then garbage collector will remove the obj memory from heap
# ref count has to be checked very often which slows the system
# Python is dynamically typed language. a first points to int then to string
# it just changes the ref from one obj to another
# C/C++ - statically typed language: if a=5. stores 5 in stack memory
# but in python, it creates an obj in heap and the var in stack points to it

class Box:
    def __init__(self, l):
        self.len = l


b1=Box(5)
b2=Box(10)

print(b1.len)
# box, len and value will be in heap. b1,b2 will be in stack referencing respective values 5 and 10 in heap
# b1 and b2 creates separate memory for box and its var len

def test(x):
    x=20

x=10
test(x)
print(x)  # Immutable: int, float, string, tuple x=10 then changing it to 11 will create new obj and var ref to it... it wont change the same obj value
# mutable: list, set

# function will be in separate block stack