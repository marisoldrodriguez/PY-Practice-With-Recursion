# Write code for algorithm 4 below
def power(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * power(a, b-1)

print(f"Two to the fourth power is:", power(2,4))
print(power(3,2))
print(power(2,0))
print(power(4, 1))