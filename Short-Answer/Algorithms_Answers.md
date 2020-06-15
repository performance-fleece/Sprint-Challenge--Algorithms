#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) 0(n)
    This while loop will run exactly n times because the formula is written such that at the nth step the sum of the previous steps plus n squared will equal n cubed 


b) 0(n log n)
    The first loop is running n times, the second time is running shy of n times because j is rising faster than n. This puts it between 0(n) and 0(n^2)

c) 0 (n)
    It's recursive and because it will call itself -1 times each iteration it will run a total of n times.

## Exercise II

def eggdrop(n)
    floors = [i+1 for i in range(n)]
    middle = n/2
    while len(floors) > 1:
        throw from mid:
            if egg breaks:
                recurse using start to (midpoint-1)
            if egg doesn't break:
                recurse using midpoint to end of range
    return remaining value

    This should be 0(log n), at each iteration the number of remaining floors is cut in half which is less than 0(n) but obviously not a constant.
            
        


