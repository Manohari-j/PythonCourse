def happy():
    print("Jumping...")


def sad():
    print("Crying...")


def calm_down():
    print("Calm down....")


def feeling(func):  # HOF:takes fn as parameter or returns a fn
    func()
    return calm_down


ret_fn=feeling(happy)
# print(ret_fn)
ret_fn()
f2=feeling(sad)
f2()
# happy()
# sad()

# print(happy)

# another name to a function - alias
# joy = happy # no () else it is calling...
# joy()
#
# sorrow = sad()
# sorrow()