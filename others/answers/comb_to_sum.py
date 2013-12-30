# print the list of numbers that sums up to a given number
# the list shouldn't include 0
# given 3, should give [1, 2] [1, 1, 1]
def helper(max_num_to_use, goal, lis):
    if goal == 0:
        print lis
        return
    elif goal < 0:
        return
    for i in xrange(1, max_num_to_use+1):
        new = lis + [i]
        helper(i, goal-i, new)

def nums_that_sum_up_to(x):
    helper(x-1, x, [])

if __name__ == "__main__":
    nums_that_sum_up_to(4)
