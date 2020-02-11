#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(log(n))
A increases faster than n increments which should make a equal n^3 faster than linear but slower than constant

b) O(n log(n))
The loop runs exactly the same amount of times as the size of n for O(n) which then loops through the while loop with j approaching n at a faster than linear rate so that would be O(log(n)).

    Combined together is O(n log(n))

c) O(n)
It is a recursive loop that runs exactly as many times as n which is O(n)

## Exercise II

This can be done with a recursive algorithm

function checkHeight(n floors)
create list of 1 to n floors

    function findHighest(list of floors)

        (test case)
        If length of floor list = 1 return return floor as answer

        Find the midpoint of total floors and test for breakage
        if eggs do not break
                split floor list in half
                run findHighest function with upper half of floors

        if eggs break
                split floor list in half
                run findHighest function with lower half of floors

Complexity should be O(log (n)) as it is removing half of n floors to test on every loop.
