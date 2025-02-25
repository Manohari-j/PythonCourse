# {:flags} format a value based on what flags are inserted
# .(num)f = round to that many decimal places
# :(num) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = + to indicate positive value
# := = place sign to leftmost pos
# : = insert a space before pos num
# :, = comma separator

p1 = 3.14159
p2=-987.65
p3 = 12.34

print(f"Price 1 is ${p1:.3f}")
print(f"Price 2 is ${p2:.3f}")
print(f"Price 3 is ${p3:.3f}")

print(f"Price 1 is ${p1:010}")
print(f"Price 2 is ${p2:<10}")
print(f"Price 3 is ${p3:>10}")

p4 = 999000098.555678
print(f"Price 1 is ${p1:^10}")
print(f"Price 4 is ${p4:+,.2f}")
print(f"Price 3 is ${p3:+}")


