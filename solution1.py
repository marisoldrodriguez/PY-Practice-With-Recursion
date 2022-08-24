# Write code for algorithm 1 below
def count_down(n):
    # Base
    if n == 0:
        return
    # Recursion
    else:
        # calling print before the recursive funciton will print in descending order 8-1 because it's a line above count_down(n-1)
        print(n)
        count_down(n-1)
        # calling print after would provide an output in ascending order 1-8 because the function would run recursively until it stops due to the base condition. Then print will provide the output.
        # print(n)
        
n=8
count_down(n)

# INHERENT EXAMPLE
# def count_down(n):
#   #inherent base case
#   #(will stop if n <= 0)
#   if n>0:
#       #recursive case
#       print(n)
#       count_down(n-1)
   
# #test case
# n=8
# count_down(n)
