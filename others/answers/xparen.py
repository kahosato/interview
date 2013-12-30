# given a number, it will print all valid parenthesis.
# eg: given 2, it should print
#     (()) and ()()
def helper(balance, to_open, lis):
    if to_open < 0 or balance < 0:
        return
    if to_open == 0 and balance == 0:
        print lis
        return
    if balance >= 0:
        new = lis + [")"]
        helper(balance-1, to_open, new)
    new = lis + ["("]
    helper(balance+1, to_open-1, new)

def print_valid_paren(n):
    helper(0, n, [])

if __name__ == "__main__":
    print_valid_paren(4)
