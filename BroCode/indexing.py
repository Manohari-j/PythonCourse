# accessing elts using [start: end : step]

credit = "1234-5678-9012-3456"

print(credit[0])
print(credit[0:4])
print(credit[:9:2])
print(credit[5:])

print(credit[-1])
print(credit[:-1])
print(credit[-5:])

last = credit[-4:]
print(f"xxxx-xxxx-xxxx-{last}")
# to reverse use -1 in step place

print(credit[::-1])
