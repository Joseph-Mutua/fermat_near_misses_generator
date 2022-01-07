#  Fermat near-misses

Design a simple program to produce near-misses of integer triplets that would satisfy

a^n + b^n = c^n for some n > 2.

## Solution
[Fermat's Last Theorem](https://en.wikipedia.org/wiki/Fermat%27s_Last_Theorem#:~:text=In%20number%20theory%2C%20Fermat's%20Last,of%20n%20greater%20than%202.) states that  there are no positive integer solutions for the equation,

    a^n + b^n = c^n
when ***n > 2***, and ***a***, ***b*** and ***c*** are all non-zero. 

I designed a Python program to attempt to generate near-misses of the above equation, i.e integer triplets that come extremely close to satisfying the equation but in actuality don't.

## Step One
Import the Python [math](https://docs.python.org/3/library/math.html) module which will provide us with the mathematical functions neededed for the program.

```python
# A near miss generator for Fermat's Last Theorem
# a^n + b^n = c^n (n > 2)
import math
```
## Step Two
We'll then define eight variables to hold critical values we'll need for our operation: 
- ***startNumber*** - This will hold the minimum values for the integers ***a***, ***b***, and ***c*** that we'll begin iterating from.
- ***stepSize***- This will define the value to increment the values of the integers ***a***, ***b***, and ***c***  between the iterations.
- ***searchSize*** - This will define the range in which to search for the values during each iteration.
- ***maxMiss***- This will define the maximum allowable miss for a set of integers to qualify as a near-miss.
- ***iterations*** - This defines the number of iterations we want to undertake each time we run the program.
- ***minN***- The minimum value of ***n*** for which to begin searching for the near-misses. (*For this program I set this to 5*)
- ***maxN*** - The maximum value of ***n*** at which we'll stop searching. (*I set this to 20*)
*(We'll therefore search for integers ***a***,***b***,***c*** for 5 < ***n*** <= 20)*
- ***diffCToAB*** - The value of the integer ***c*** should not be close to the values of ***a*** and ***b*** by this margin.


## Step 3
We'll now define a function ***getNearestSolution()*** which will return the closest solution for (***a***, ***b***,***c*** ) for a given range for the base and the given exponent(***n***).

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
## Step 4
We'll create a nested *for loop* that will iterate from the given minimum values of the integers ***a*** and ***b*** to their maximum given values and try to approximate the value of integer ***c*** by raising the sum of the powers of ***a*** and ***b*** to the power of inverse ***n*** for each iteration.

If the ***miss*** is greater than 0.5, we'll increment the value of ***c*** by 1 and set the miss to the difference of 1 and the obtained miss, before passing on the value to the next operation.
  
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


If the ***miss*** obtained is less than the value of ***nMiss***, we'll set ***c*** to the value obtained from ***cExact***. 

Next we check whether the value of ***c*** is within the allowable range of difference to ***a*** and ***b***. If so, substitute the values of the integers  ***a***, ***b***,***c*** and ***n*** in the ***nearestSolution*** dictionary to those obtained above and set the next value of ***nMiss*** to the ***miss*** obtained. After the *for loop* has run to completion we return the nearestSolution dictionary

```python
 if miss < nMiss:
                c = int(math.floor(cExact))
                
                
                # Check whether the value of c is within the allowable
                # range of difference to 'a' and 'b' 
                # if so, subsitute the values of the integers
                # 'a', 'b', 'c' and 'n' in the nearestSolution dictionary to 
                # those obtained above
                if c > b + diffCToAB and c > a + diffCToAB:
                    nearestSolution = {
                        'a': a,
                        'b': b,
                        'c': int(math.floor(cExact)),
                        'n': n,
                        'miss': miss
                    }

                    nMiss = miss
                    pass

```
## Step 5
We'll now create a ***solutions*** array to hold the integer triplets that qualify as near-misses and begin our iterations using a *for loop*. The final results will be printed to the console.


```python
# Create array to hold the values of the solutions 
# meeting the value of maximum miss
solutions = []

# Begin the iterations
for iteration in range(0, iterations):
    
    # Get the min and max values for the integers for each iteration
    minB = startNumber + iteration * stepSize
    maxB = minB + searchSize

    print("Iteration " + str(iteration + 1) + " started")

    for n in range(minN, maxN + 1):
        solution = getNearestSolution(minB, maxB, n)
        print("Nearest solution for the bases between " + str(minB) + " and " +
              str(maxB) + " and the exponent " + str(n) + " => " +
              str(solution))

        # Append the obtained solution to the slutions array
        if solution['miss'] < maxMiss:
            solutions.append(solution)
            pass

        pass

    pass

print(solutions)
```
## Example
To test this program you can clone it from this [link](https://github.com/Joseph-Mutua/problem_no_5.git) into your directory.
```bash
git clone <url>
```
Now navigate to the project folder and run the program `python3 fermat_near_misses.py`

**Note:** For this example I will only run 2 iterations for the sake of demonstration.



```bash
mutua@mutua-virtualbox:~/Desktop/PROBLEM_SET/problem_no_5$ python3 fermat_near_misses.py
Iteration 1 started
Nearest solution for the bases between 1000 and 4000 and the exponent 5 => {'a': 1783, 'b': 2766, 'c': 2825, 'n': 5, 'miss': 2.50516677624546e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 6 => {'a': 2209, 'b': 2255, 'c': 2506, 'n': 6, 'miss': 2.7612122721620835e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 7 => {'a': 3029, 'b': 3964, 'c': 4045, 'n': 7, 'miss': 3.9972292142920196e-08}
Nearest solution for the bases between 1000 and 4000 and the exponent 8 => {'a': 1736, 'b': 2288, 'c': 2318, 'n': 8, 'miss': 4.235271262587048e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 9 => {'a': 3766, 'b': 3937, 'c': 4168, 'n': 9, 'miss': 2.3840129870222881e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 10 => {'a': 2140, 'b': 2704, 'c': 2729, 'n': 10, 'miss': 6.474510882981122e-08}
Nearest solution for the bases between 1000 and 4000 and the exponent 11 => {'a': 1264, 'b': 1280, 'c': 1355, 'n': 11, 'miss': 4.899986834061565e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 12 => {'a': 1782, 'b': 1841, 'c': 1922, 'n': 12, 'miss': 4.4133457777206786e-08}
Nearest solution for the bases between 1000 and 4000 and the exponent 13 => {'a': 3113, 'b': 3497, 'c': 3551, 'n': 13, 'miss': 3.50016762240557e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 14 => {'a': 3040, 'b': 3384, 'c': 3433, 'n': 14, 'miss': 6.873879101476632e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 15 => {'a': 1535, 'b': 1621, 'c': 1661, 'n': 15, 'miss': 5.378401510824915e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 16 => {'a': 2914, 'b': 3256, 'c': 3288, 'n': 16, 'miss': 7.109465514076874e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 17 => {'a': 3712, 'b': 3713, 'c': 3867, 'n': 17, 'miss': 6.797572495997883e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 18 => {'a': 2782, 'b': 3118, 'c': 3139, 'n': 18, 'miss': 5.139436325407587e-07}
Nearest solution for the bases between 1000 and 4000 and the exponent 19 => {'a': 1190, 'b': 1216, 'c': 1249, 'n': 19, 'miss': 1.6954227248788811e-06}
Nearest solution for the bases between 1000 and 4000 and the exponent 20 => {'a': 2586, 'b': 2615, 'c': 2693, 'n': 20, 'miss': 1.6082385627669282e-06}
Iteration 2 started
Nearest solution for the bases between 2000 and 5000 and the exponent 5 => {'a': 2250, 'b': 4670, 'c': 4694, 'n': 5, 'miss': 7.298240234376863e-08}
Nearest solution for the bases between 2000 and 5000 and the exponent 6 => {'a': 2209, 'b': 2255, 'c': 2506, 'n': 6, 'miss': 2.7612122721620835e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 7 => {'a': 3029, 'b': 3964, 'c': 4045, 'n': 7, 'miss': 3.9972292142920196e-08}
Nearest solution for the bases between 2000 and 5000 and the exponent 8 => {'a': 3287, 'b': 4265, 'c': 4328, 'n': 8, 'miss': 4.040693966089748e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 9 => {'a': 3766, 'b': 3937, 'c': 4168, 'n': 9, 'miss': 2.3840129870222881e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 10 => {'a': 2140, 'b': 2704, 'c': 2729, 'n': 10, 'miss': 6.474510882981122e-08}
Nearest solution for the bases between 2000 and 5000 and the exponent 11 => {'a': 3858, 'b': 4123, 'c': 4273, 'n': 11, 'miss': 1.006728780339472e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 12 => {'a': 3987, 'b': 4365, 'c': 4472, 'n': 12, 'miss': 7.057678885757923e-09}
Nearest solution for the bases between 2000 and 5000 and the exponent 13 => {'a': 3113, 'b': 3497, 'c': 3551, 'n': 13, 'miss': 3.50016762240557e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 14 => {'a': 4433, 'b': 4519, 'c': 4706, 'n': 14, 'miss': 3.986770025221631e-08}
Nearest solution for the bases between 2000 and 5000 and the exponent 15 => {'a': 4271, 'b': 4491, 'c': 4608, 'n': 15, 'miss': 5.013062036596239e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 16 => {'a': 2914, 'b': 3256, 'c': 3288, 'n': 16, 'miss': 7.109465514076874e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 17 => {'a': 3712, 'b': 3713, 'c': 3867, 'n': 17, 'miss': 6.797572495997883e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 18 => {'a': 3931, 'b': 4501, 'c': 4522, 'n': 18, 'miss': 1.1370684660505503e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 19 => {'a': 4629, 'b': 4659, 'c': 4817, 'n': 19, 'miss': 7.106345947249793e-07}
Nearest solution for the bases between 2000 and 5000 and the exponent 20 => {'a': 2586, 'b': 2615, 'c': 2693, 'n': 20, 'miss': 1.6082385627669282e-06}
[{'a': 3987, 'b': 4365, 'c': 4472, 'n': 12, 'miss': 7.057678885757923e-09}]

```

For our first two iterations we have obtained one integer triplet
```bash
[{'a': 3987, 'b': 4365, 'c': 4472, 'n': 12, 'miss': 7.057678885757923e-09}]
```
