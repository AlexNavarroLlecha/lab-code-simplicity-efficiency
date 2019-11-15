"""
You are presented with an integer number larger than 5. Your goal is to identify the longest side
possible in a right triangle whose sides are not longer than the number you are given.

For example, if you are given the number 15, there are 3 possibilities to compose right triangles:

1. [3, 4, 5]
2. [6, 8, 10]
3. [5, 12, 13]

The following function shows one way to solve the problem but the code is not ideal or efficient.
Refactor the code based on what you have learned about code simplicity and efficiency.
"""

def my_function(t):
    solutions = [[x,y,z] for x in range(t) for y in range(t) for z in range(t) if(x*x==y*y+z*z) ]
    m = 0
    m = [max(item) for item in solutions if m < max(item)]
    return max(m)

t = input("What is the maximal length of the triangle side? Enter a number: ")

print(f"The longest side possible is " + str(my_function(int(t))))

   