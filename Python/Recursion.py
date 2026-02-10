def num():
    print("Nahid")
    num()

num()


#another example of recursion
def print_num(n):
    if n == 0:        # base case
        return
    print(n)
    print_num(n-1)    # recursive call

print_num(3)
