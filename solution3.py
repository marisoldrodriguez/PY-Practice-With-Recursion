# Write code for algorithm 3 below
def nth_fibonacci(n):
    if n<= 0:
        print("Wrong Input")    
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return nth_fibonacci(n-1)+nth_fibonacci(n-2)
print("2nd fib number:")
print(nth_fibonacci(2))
print("4th fib number:")
print(nth_fibonacci(4))
print("8th fib number:")
print(nth_fibonacci(8))
print("Invalid fib number:")
print(nth_fibonacci(0))
