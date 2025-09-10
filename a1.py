# Assignment 1: AI-Generated Python Problems
# Name: Lyle Jose

"""
AI-Generated Problem Set

INSTRUCTIONS:
1. Document your original AI prompt below
2. Copy the problems your AI assistant generated
3. Implement solutions for each problem
4. Include comments explaining your approach
5. Test your solutions with different inputs

Remember: The goal is to LEARN, not just get working code!
"""

# =============================================================================
# PART 1: DOCUMENT YOUR AI COLLABORATION
# =============================================================================

"""
MY ORIGINAL AI PROMPT:
[Paste the prompt you used to generate your problem set here]

I'm learning the basics of Python programming in a high school programming class.
I have experience with Java, as I took APCSA and passed it last year without thinking
it was too difficult. Can you create 5-7 problems that cover
 > - Variables and basic data types 
 > - Conditionals (if/elif/else) 
 > - Loops (for and while) 
 > - Functions 
 > - Basic list operations 
Make them progressively more challenging. Make sure each problem has clear instructions and example inputs/outputs."


Example: "I'm learning Python basics in a high school programming class. 
I have some experience with Java. Can you create 5-7 practice problems that cover..."
"""

# =============================================================================
# PART 2: AI-GENERATED PROBLEMS & SOLUTIONS
# =============================================================================

"""
Example:
Problem: Write a function called 'is_even' that takes an integer and returns 
True if the number is even, False if it's odd.

Example inputs/outputs:
- is_even(4) should return True
- is_even(7) should return False
"""

'''
PROBLEM 1: Welcome Message Generator (Variables & Strings)
Task: Write a program that asks the user for their name and age, then prints a welcome message.
Example Input:
name = "Alex"
age = 16
Example Output:
Welcome, Alex! You are 16 years old.
'''
def greet():
    name = "Lyle"
    age = "17"
    print(f"Welcome, {name}! You are {age} years old.")
      
'''
PROBLEM 2: Even or Odd Checker (Conditionals)
Write a function check_even_odd(num) that takes an integer and prints whether it is even or odd.
Ex Input:
check_even_odd(7)
Ex Output:
7 is odd.
'''

def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd") 

'''
PROBLEM 3: Sum of First N Numbers (Loops)
Task: Write a program that asks the user for a number n and calculates the sum of the first n natural numbers using a for loop.
Example Input:
Enter a number: 5
Example Output:
The sum of the first 5 numbers is 15.
'''
def first_n(n):
    n = int(input("Enter number: "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

'''
4. Password Strength Checker (Conditionals + Loops)
Task: Write a function check_password_strength(password) that checks if a password is strong. A strong password:
Is at least 8 characters long
Contains at least one digit
Contains at least one uppercase letter
Example Input:
check_password_strength("Python123")
Example Output:
Password is strong.
'''
def check_password_strength(password):
    numbs = "0123456789"
    has_numb = False
    has_uppercase = False
    has_8_chars = len(password) >= 8
    for char in password:
        if char in numbs:
            has_numb = True
    for char in password:
        if char.isupper():
            has_uppercase = True
    return has_numb and has_uppercase and has_8_chars
        
"""
Task: Write a function find_multiples(n, limit) that returns a list of all multiples of n up to limit.
Example Input:
find_multiples(3, 20)
Example Output:
[3, 6, 9, 12, 15, 18]
"""
def find_multiples(n, limit):
    multiples = []
    inc = n
    while n <= limit:
        multiples.append(n)
        n += inc
    return multiples
    
"""
6. Grade Categorizer (Lists + Conditionals + Functions)
Task: Write a function categorize_grades(grades) that takes a list of numerical grades and returns a list of letter grades:
A: 90+
B: 80–89
C: 70–79
D: 60–69
F: <60
Example Input:
categorize_grades([95, 82, 67, 74, 58])
Example Output:
['A', 'B', 'D', 'C', 'F']
"""

def categorize_grades(grades):
    lst = []
    for grade in grades:
        if grade >= 90:
            lst.append("A")
        elif grade >= 80 and grade < 90:
            lst.append("B")
        elif grade >= 70 and grade < 80:
            lst.append("C")
        elif grade >= 60 and grade < 70:
            lst.append("D")
        else:
            lst.append("F")
    return lst

"""
7. Prime Number Generator (Functions + Loops + Conditionals)
Task: Write a function generate_primes(limit) that returns a list of all prime numbers up to limit.
Example Input:
generate_primes(20)
Example Output:
[2, 3, 5, 7, 11, 13, 17, 19]
"""

def generate_primes(limit):
    lst = []
    if limit < 2:
        return lst
    i = 2
    while i < limit:
        prime = True
        for n in range(2, i):
            if i % n == 0:
                prime = False
                break
        if prime:
            lst.append(i)
        i += 1
    return lst

"""
Problem 8: Substring Extraction with Indexing
Prompt: You’re given a string:

python
text = "pineapple"
Write a function extract_sub(str, find) that checks if find exists in str. Returns true if yes, false if no

"""
def extract_sub(str, find):
    fnd = False
    for i in range(len(str) - len(find) + 1):
        curr = str[i:i + len(find)]
        if curr == find:
            fnd = True
    return fnd

"""
Problem 9: 📚 2. Chunk a List
Function Name: chunk_list(lst, size)

Prompt: Write a function that splits a list into chunks of a given size using slicing. Return a list of lists.

Example:

python
chunk_list([1, 2, 3, 4, 5, 6], 2)  
# → [[1, 2], [3, 4], [5, 6]]
"""

def chunk_list(lst, size):
    result = []
    for i in range(0, len(lst), size):
        new_lst = lst[i:i + size]
        result.append(new_lst)
    return result




# =============================================================================
# PART 3: TESTING YOUR SOLUTIONS
# =============================================================================


"""
Test all your solutions with different inputs

Add asserts if you feel comfortable

Example:
print("Testing Problem 1:")
print(f"is_even(4): {is_even(4)}")  # Should print True
print(f"is_even(7): {is_even(7)}")  # Should print False
"""

print("Testing Problem 1:")
# Add your tests here
greet()
print("\nTesting Problem 2:")
# Add your tests here
check_even_odd(3)
check_even_odd(2)
print("\nTesting Problem 3:")
# Add your tests here
print(first_n(5))
print(first_n(10))
print(first_n(6))
print("\nTesting Problem 4:")
# Add your tests here
print(check_password_strength("IntroToAi123"))
print(check_password_strength("hello"))
print("\nTesting Problem 5:")
# Add your tests here
print(find_multiples(3, 20))
print(find_multiples(2, 10))
print(find_multiples(6, 64))

print("\nTesting Problem 6:")

print(categorize_grades([99, 94, 93, 34, 65, 79]))
print(categorize_grades([99, 89, 79, 69, 59]))

print("\nTesting Problem 7:")

print(generate_primes(5))
print(generate_primes(19))
print(generate_primes(8))

print("\nTesting Problem 8:")
print(extract_sub("banana", "apple"))
print(extract_sub("pineapple", "apple"))
print(extract_sub("helloabcbye", "abc"))

print("\nTesting Problem 9:")
print(chunk_list([1,2,3,4,5,6], 2))
print(chunk_list([3, 6, 9, 12, 15, 18, 21, 24, 27, 30], 3))

