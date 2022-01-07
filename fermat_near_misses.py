# A near miss generator for Fermat's Last Theorem
# a^n + b^n = c^n (n > 2)
import math

# Min values for "a", "b" and "c" to begin with
startNumber = 1000

# Value to increment the values of 'a', 'b' and 'c' between the iterations
stepSize = 1000

# Range in which to search for the values for each iteration
searchSize = 3000

# Define the maximum allowable miss
maxMiss = 1e-08

# No of iterations to run the program
iterations = 20

# Min/max number 'n'
minN = 5
maxN = 20

# 'c' should not be near 'a' and 'b' by this value
diffCToAB = 20


# Get the nearest solution for a given range for the base and given exponent
def getNearestSolution(minB, maxB, n):
    nearestSolution = {
        'a': 0,
        'b': 0,
        'c': 0,
        'n': 0,
        'miss': 1
    }

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

            if miss < nMiss:
                c = int(math.floor(cExact))

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

                pass

            pass

        pass

    return nearestSolution


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

        if solution['miss'] < maxMiss:
            solutions.append(solution)
            pass

        pass

    pass

print(solutions)