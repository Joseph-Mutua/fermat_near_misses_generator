#  Fermat near-misses.

Design a simple program to produce near-misses of integer triplets that would satisfy

a^n + b^n = c^n for some n > 2.

## Solution
[Fermat's Last Theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem#:~:text=In%20number%20theory%2C%20Fermat's%20Last,of%20n%20greater%20than%202.) states that  there are no positive integer solutions for the equation,

    a^n + b^n = c^n
when n > 2, and a, b and c are all non-zero. 

I designed a Python program to attempt to generate near-misses of the above equation, i.e integers that come extremely close to satisfying the equation but in actuality don't.

## 1. Step One
Import the Python [math](https://docs.python.org/3/library/math.html) module which will provide us with the mathematical functions neededed for the program.

```python
# A near miss generator for Fermat's Last Theorem
# a^n + b^n = c^n (n > 2)
import math
```
## 2. Step Two
We'll then define eight variables to hold critical values we'll need for our operation: 
- ***startNumber*** - This will hold the minimum values for the integers 'a', 'b', and 'c' that we'll begin iterating from.
- ***stepSize***- This will define the value to increment the values of the integers 'a', 'b', and 'c' between the iterations.
- ***searchSize*** - This will defne the range in which to search for the values during each iteration
- ***maxMiss***- This will define the maximum allowable miss for a set of integers to qualify as a near-miss.
- ***iterations*** - This defines the number of iterations we want to undertake each time we run the program.
- ***minN***- The minimum value of 'n' for which to begin searching for the near-misses. (*For this program I set this to 5*)
- ***maxN*** - The maximum value of 'n' at which we'll stop searching. (*I set this to 20*)
*We'll therefore search for integers a,b,c for 5 < n < 20*
- ***diffCToAB***- The value of the integer 'c' should not be close to the values of 'a' and 'b' by this margin.


## 3. Step 3
We'll now define a function ***getNearestSolution()*** which will return the closest solution (a, b ,c) for a given range for the base and the given exponent (n).

Inside the function we create a dictionary to hold the integers and initialize them with zero values and a maximum miss of 1.

```python
# Get the nearest solution for a given range for the base and given exponent
def getNearestSolution(minB, maxB, n):
    nearestSolution = {
        'a': 0,
        'b': 0,
        'c': 0,
        'n': 0,
        'miss': 1
    }
```
## 4. Step 4
We'll create a nested *for* loop that will iterate from the given minimum values of the integers 'a' and 'b' to their maximum given values and try to approximate the value of integer 'c' by raising the sum of the powers of 'a' and 'b' to the poer of inverse 'n' for each iteration.

If the miss is greater than 0.5, we'll increment the value of 'c' by 1 and set the miss to the difference of 1 and the obtained miss, before passing on the value to the next operation.
  
```python
    nMiss = 1
    for a in range(minB, maxB + 1):
        for b in range(a, maxB + 1):
            
            # approximate the value of 'c' by raising the sum of 
            # powers of 'a' and 'b' to the power of inverse 'n'
            cExact = math.pow(math.pow(a, n) + math.pow(b, n), 1.0 / n)
            miss = cExact % 1


            # if the miss is greater than 0.5, increment the value of 
            # c by 1 and set the miss to the difference of 1 and the 
            # obtained miss and pass onto the next operation
            
            # if the miss obtained is less than the value of nMiss, 
            # set c to the value obtained from cExact
            if miss > 0.5:
                cExact += 1
                miss = 1 - miss
                pass
```


If the miss obtained is less than the value of nMiss, we'll set ***c*** to the value obtained from ***cExact***. 

Next we check whether the value of ***c*** is within the allowable range of difference to ***a*** and ***b***. If so, substitute the values of the integers  ***a***, ***b***,***c*** and ***n*** in the ***nearestSolution*** dictionary to those obtained above and set the next value of ***nMiss*** to the ***miss*** obtained. After the *for loop* has run to completion we return the nearestSolution dictionary
