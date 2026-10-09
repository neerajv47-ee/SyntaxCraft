"""
SyntaxCraft - Rule-Based Python Code Generator
Module: generator.code_generator

A purely rule-based, deterministic engine for converting plain-English
programming instructions into Python code. No AI, ML, NLP libraries, or external
APIs are used.

Supported Tasks:
 1. Addition of two numbers
 2. Subtraction of two numbers
 3. Multiplication of two numbers
 4. Division of two numbers
 5. Even or odd number
 6. Positive, negative or zero
 7. Largest of three numbers
 8. Smallest of three numbers
 9. Print numbers from 1 to N (or 1 to 10)
10. Sum of numbers from 1 to N
11. Factorial of a number
12. Reverse a string
13. Check palindrome
14. Count vowels in a string
15. Check whether a number is prime
"""

import re
from typing import Dict, Any, Optional

UNSUPPORTED_MESSAGE = (
    "Sorry, SyntaxCraft currently does not support this type of problem. "
    "Try one of the supported examples."
)

SUPPORTED_TASKS = [
    {"id": "add_two_numbers", "name": "Addition of two numbers", "example": "Take two numbers and print their sum"},
    {"id": "subtract_two_numbers", "name": "Subtraction of two numbers", "example": "Subtract two numbers"},
    {"id": "multiply_two_numbers", "name": "Multiplication of two numbers", "example": "Multiply two numbers"},
    {"id": "divide_two_numbers", "name": "Division of two numbers", "example": "Divide two numbers"},
    {"id": "even_or_odd", "name": "Even or odd number", "example": "Check whether a number is even or odd"},
    {"id": "positive_negative_zero", "name": "Positive, negative or zero", "example": "Check if a number is positive, negative or zero"},
    {"id": "largest_of_three", "name": "Largest of three numbers", "example": "Find the largest of three numbers"},
    {"id": "smallest_of_three", "name": "Smallest of three numbers", "example": "Find the smallest of three numbers"},
    {"id": "print_1_to_n", "name": "Print numbers from 1 to N", "example": "Print numbers from 1 to 10"},
    {"id": "sum_1_to_n", "name": "Sum of numbers from 1 to N", "example": "Find the sum of numbers from 1 to N"},
    {"id": "factorial", "name": "Factorial of a number", "example": "Find the factorial of a number"},
    {"id": "reverse_string", "name": "Reverse a string", "example": "Reverse a string"},
    {"id": "check_palindrome", "name": "Check palindrome", "example": "Check whether a string is a palindrome"},
    {"id": "count_vowels", "name": "Count vowels in a string", "example": "Count vowels in a string"},
    {"id": "check_prime", "name": "Check whether a number is prime", "example": "Check whether a number is prime"},
]

# ---------------------------------------------------------------------------
# Code Templates by Task and Difficulty
# ---------------------------------------------------------------------------

TEMPLATES: Dict[str, Dict[str, str]] = {
    # 1. Addition of two numbers
    "add_two_numbers": {
        "Beginner": '''# Addition of two numbers (Beginner)
# Step 1: Take two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 2: Calculate their sum
total = num1 + num2

# Step 3: Print the result
print("The sum is:", total)
''',
        "Intermediate": '''# Addition of two numbers (Intermediate: Reusable function)
def add_numbers(a: float, b: float) -> float:
    """Return the sum of two numeric values."""
    return a + b

# Read inputs and display formatted output
first = float(input("Enter first number: "))
second = float(input("Enter second number: "))
print(f"The sum of {first} and {second} is {add_numbers(first, second)}")
''',
        "Advanced": '''# Addition of two numbers (Advanced: Unpacking & Lambda)
add = lambda a, b: a + b

# Read both numbers in a single line
x, y = map(float, input("Enter two numbers separated by space: ").split())
print(f"Sum: {add(x, y):.2f}")
'''
    },

    # 2. Subtraction of two numbers
    "subtract_two_numbers": {
        "Beginner": '''# Subtraction of two numbers (Beginner)
# Step 1: Take two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 2: Calculate the difference
difference = num1 - num2

# Step 3: Print the result
print("The difference is:", difference)
''',
        "Intermediate": '''# Subtraction of two numbers (Intermediate: Function-based)
def subtract(a: float, b: float) -> float:
    """Return the difference between a and b."""
    return a - b

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
print(f"{x} - {y} = {subtract(x, y)}")
''',
        "Advanced": '''# Subtraction of two numbers (Advanced: Compact single-line input)
sub = lambda a, b: a - b

a, b = map(float, input("Enter two numbers separated by space: ").split())
print(f"Difference: {sub(a, b):.2f}")
'''
    },

    # 3. Multiplication of two numbers
    "multiply_two_numbers": {
        "Beginner": '''# Multiplication of two numbers (Beginner)
# Step 1: Take two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 2: Calculate the product
product = num1 * num2

# Step 3: Print the result
print("The product is:", product)
''',
        "Intermediate": '''# Multiplication of two numbers (Intermediate: Typed function)
def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Product of {num1} and {num2} is {multiply(num1, num2)}")
''',
        "Advanced": '''# Multiplication of two numbers (Advanced: Lambda & formatted output)
mul = lambda x, y: x * y

a, b = map(float, input("Enter two numbers separated by space: ").split())
print(f"Product: {mul(a, b):.2f}")
'''
    },

    # 4. Division of two numbers
    "divide_two_numbers": {
        "Beginner": '''# Division of two numbers (Beginner)
# Step 1: Take dividend and divisor
num1 = float(input("Enter dividend (first number): "))
num2 = float(input("Enter divisor (second number): "))

# Step 2: Check for division by zero before dividing
if num2 == 0:
    print("Error: Division by zero is not allowed.")
else:
    result = num1 / num2
    print("The quotient is:", result)
''',
        "Intermediate": '''# Division of two numbers (Intermediate: Exception handling)
def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

try:
    x = float(input("Enter dividend: "))
    y = float(input("Enter divisor: "))
    print(f"{x} / {y} = {divide(x, y):.4f}")
except ZeroDivisionError as err:
    print("Math Error:", err)
''',
        "Advanced": '''# Division of two numbers (Advanced: Safe ternary evaluation)
a, b = map(float, input("Enter dividend and divisor separated by space: ").split())
result = f"{a / b:.4f}" if b != 0 else "Undefined (division by zero)"
print(f"Result: {result}")
'''
    },

    # 5. Even or odd number
    "even_or_odd": {
        "Beginner": '''# Check Even or Odd (Beginner)
# Step 1: Input an integer
number = int(input("Enter an integer: "))

# Step 2: Use modulo (%) to check divisibility by 2
if number % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
''',
        "Intermediate": '''# Check Even or Odd (Intermediate: Function with ternary operator)
def is_even(n: int) -> bool:
    return n % 2 == 0

val = int(input("Enter an integer: "))
outcome = "Even" if is_even(val) else "Odd"
print(f"{val} is {outcome}")
''',
        "Advanced": '''# Check Even or Odd (Advanced: Bitwise AND check)
# In binary, odd numbers always have their least significant bit set to 1
n = int(input("Enter an integer: "))
print(f"{n} is {'Odd' if (n & 1) else 'Even'}")
'''
    },

    # 6. Positive, negative or zero
    "positive_negative_zero": {
        "Beginner": '''# Check Positive, Negative, or Zero (Beginner)
# Step 1: Input a number
num = float(input("Enter a number: "))

# Step 2: Multi-way conditional check
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")
''',
        "Intermediate": '''# Check Positive, Negative, or Zero (Intermediate: Classifier function)
def classify_number(val: float) -> str:
    if val > 0:
        return "Positive"
    elif val < 0:
        return "Negative"
    return "Zero"

number = float(input("Enter a number: "))
print(f"{number} is {classify_number(number)}")
''',
        "Advanced": '''# Check Positive, Negative, or Zero (Advanced: Nested conditional expression)
val = float(input("Enter a number: "))
sign = "Positive" if val > 0 else ("Negative" if val < 0 else "Zero")
print(f"The number {val} is {sign}")
'''
    },

    # 7. Largest of three numbers
    "largest_of_three": {
        "Beginner": '''# Largest of three numbers (Beginner)
# Step 1: Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Step 2: Compare using logical and
if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

# Step 3: Print the largest
print("The largest number is:", largest)
''',
        "Intermediate": '''# Largest of three numbers (Intermediate: Python max function)
def find_largest(x: float, y: float, z: float) -> float:
    return max(x, y, z)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print(f"The largest of [{a}, {b}, {c}] is {find_largest(a, b, c)}")
''',
        "Advanced": '''# Largest of three numbers (Advanced: Unpacking & max)
nums = list(map(float, input("Enter 3 numbers separated by space: ").split()))
print(f"Largest value: {max(nums)}")
'''
    },

    # 8. Smallest of three numbers
    "smallest_of_three": {
        "Beginner": '''# Smallest of three numbers (Beginner)
# Step 1: Input three numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

# Step 2: Compare using logical and
if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

# Step 3: Print the smallest
print("The smallest number is:", smallest)
''',
        "Intermediate": '''# Smallest of three numbers (Intermediate: Python min function)
def find_smallest(x: float, y: float, z: float) -> float:
    return min(x, y, z)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print(f"The smallest of [{a}, {b}, {c}] is {find_smallest(a, b, c)}")
''',
        "Advanced": '''# Smallest of three numbers (Advanced: Unpacking & min)
nums = list(map(float, input("Enter 3 numbers separated by space: ").split()))
print(f"Smallest value: {min(nums)}")
'''
    },

    # 9. Print numbers from 1 to N
    "print_1_to_n": {
        "Beginner": '''# Print numbers from 1 to N (Beginner)
# Step 1: Prompt the user for the upper limit N
n = int(input("Enter the limit (N): "))

# Step 2: Iterate from 1 up to N (inclusive)
for i in range(1, n + 1):
    print(i)
''',
        "Intermediate": '''# Print numbers from 1 to N (Intermediate: Horizontal print with end=" ")
n = int(input("Enter the limit (N): "))

for num in range(1, n + 1):
    print(num, end=" ")
print()  # newline
''',
        "Advanced": '''# Print numbers from 1 to N (Advanced: Iterable unpacking)
n = int(input("Enter the limit (N): "))
print(*range(1, n + 1))
'''
    },

    # 10. Sum of numbers from 1 to N
    "sum_1_to_n": {
        "Beginner": '''# Sum of numbers from 1 to N (Beginner)
# Step 1: Prompt for N
n = int(input("Enter a positive integer N: "))

# Step 2: Accumulate sum using a loop
total = 0
for i in range(1, n + 1):
    total = total + i

# Step 3: Output the result
print("The sum of numbers from 1 to", n, "is:", total)
''',
        "Intermediate": '''# Sum of numbers from 1 to N (Intermediate: sum() with range)
n = int(input("Enter positive integer N: "))
total = sum(range(1, n + 1))
print(f"Sum from 1 to {n} is: {total}")
''',
        "Advanced": '''# Sum of numbers from 1 to N (Advanced: O(1) Gauss formula n*(n+1)//2)
n = int(input("Enter positive integer N: "))
total = (n * (n + 1)) // 2
print(f"Sum from 1 to {n} = {total} (calculated in O(1) time)")
'''
    },

    # 11. Factorial
    "factorial": {
        "Beginner": '''# Factorial of a number (Beginner)
# Step 1: Input non-negative integer
num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0 or num == 1:
    print("The factorial is: 1")
else:
    fact = 1
    # Multiply numbers from 1 to num
    for i in range(1, num + 1):
        fact = fact * i
    print("The factorial of", num, "is:", fact)
''',
        "Intermediate": '''# Factorial of a number (Intermediate: Recursive approach)
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    return 1 if n in (0, 1) else n * factorial(n - 1)

val = int(input("Enter an integer: "))
try:
    print(f"{val}! = {factorial(val)}")
except ValueError as e:
    print("Error:", e)
''',
        "Advanced": '''# Factorial of a number (Advanced: Built-in math.factorial)
import math

n = int(input("Enter a non-negative integer: "))
if n >= 0:
    print(f"Factorial of {n}: {math.factorial(n)}")
else:
    print("Error: Factorial requires a non-negative number.")
'''
    },

    # 12. Reverse a string
    "reverse_string": {
        "Beginner": '''# Reverse a string (Beginner)
# Step 1: Input the original text
text = input("Enter a string: ")

# Step 2: Build the reversed string character by character
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text

# Step 3: Print reversed result
print("Reversed string:", reversed_text)
''',
        "Intermediate": '''# Reverse a string (Intermediate: Python slice step [::-1])
def reverse_string(s: str) -> str:
    """Return the reversed string using slicing."""
    return s[::-1]

user_text = input("Enter a string: ")
print(f"Reversed: {reverse_string(user_text)}")
''',
        "Advanced": '''# Reverse a string (Advanced: reversed() iterator and join)
text = input("Enter a string: ")
print("".join(reversed(text)))
'''
    },

    # 13. Check palindrome
    "check_palindrome": {
        "Beginner": '''# Check Palindrome (Beginner)
# Step 1: Input a string
text = input("Enter a word or text: ")

# Step 2: Normalize casing
cleaned_text = text.lower()

# Step 3: Reverse the string using a loop
reversed_text = ""
for char in cleaned_text:
    reversed_text = char + reversed_text

# Step 4: Compare original with reversed
if cleaned_text == reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
''',
        "Intermediate": '''# Check Palindrome (Intermediate: Cleaned slice comparison)
def is_palindrome(s: str) -> bool:
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
''',
        "Advanced": '''# Check Palindrome (Advanced: Two-pointer technique without full copy)
def is_palindrome(s: str) -> bool:
    cleaned = [ch.lower() for ch in s if ch.isalnum()]
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

user_input = input("Enter text: ")
print("Palindrome" if is_palindrome(user_input) else "Not a palindrome")
'''
    },

    # 14. Count vowels in a string
    "count_vowels": {
        "Beginner": '''# Count vowels in a string (Beginner)
# Step 1: Input the sentence
text = input("Enter a string: ")

# Step 2: Define vowels and initialize counter
vowels = "aeiouAEIOU"
count = 0

# Step 3: Iterate and check each character
for char in text:
    if char in vowels:
        count = count + 1

# Step 4: Print count
print("Total number of vowels:", count)
''',
        "Intermediate": '''# Count vowels in a string (Intermediate: Generator expression with sum)
def count_vowels(s: str) -> int:
    vowel_set = set("aeiou")
    return sum(1 for char in s.lower() if char in vowel_set)

user_text = input("Enter a string: ")
print(f"Number of vowels in '{user_text}': {count_vowels(user_text)}")
''',
        "Advanced": '''# Count vowels in a string (Advanced: Regular expressions)
import re

text = input("Enter a string: ")
vowels_found = re.findall(r"[aeiou]", text, re.IGNORECASE)
print(f"Total vowels: {len(vowels_found)}")
'''
    },

    # 15. Check whether a number is prime
    "check_prime": {
        "Beginner": '''# Check Prime Number (Beginner)
# Step 1: Input an integer
num = int(input("Enter a positive integer: "))

# Step 2: Numbers <= 1 are not prime
if num <= 1:
    print(num, "is not a prime number.")
else:
    is_prime = True
    # Test divisibility from 2 up to num - 1
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is not a prime number.")
''',
        "Intermediate": '''# Check Prime Number (Intermediate: Optimized up to sqrt(n))
import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    # Only check up to square root of n
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

val = int(input("Enter an integer: "))
print(f"{val} is {'a prime' if is_prime(val) else 'not a prime'} number.")
''',
        "Advanced": '''# Check Prime Number (Advanced: 6k +/- 1 primality test)
def is_prime(n: int) -> bool:
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

num = int(input("Enter an integer: "))
print(f"{num} is {'Prime' if is_prime(num) else 'Not Prime'}")
'''
    }
}


# ---------------------------------------------------------------------------
# Natural English Intent Classifier (Rule-Based)
# ---------------------------------------------------------------------------

def normalize_text(text: str) -> str:
    """Clean and normalize English prompt by lowercasing and trimming punctuation."""
    if not text:
        return ""
    # Convert to lowercase
    normalized = text.lower().strip()
    # Replace punctuation characters with spaces, keeping alphanumerics
    normalized = re.sub(r"[^\w\s]", " ", normalized)
    # Collapse multiple whitespace
    normalized = re.sub(r"\s+", " ", normalized).strip()
    return normalized


def classify_task(prompt: str) -> Optional[str]:
    """
    Classify the user's natural English request into one of the 15 supported tasks.
    Returns the task identifier string or None if unsupported.
    """
    clean = normalize_text(prompt)
    if not clean:
        return None

    # Check 13: Palindrome
    if "palindrome" in clean:
        return "check_palindrome"

    # Check 14: Count vowels
    if "vowel" in clean or "vowels" in clean:
        return "count_vowels"

    # Check 15: Prime number
    if "prime" in clean:
        return "check_prime"

    # Check 11: Factorial
    if "factorial" in clean:
        return "factorial"

    # Check 12: Reverse string
    # (Matches "reverse", "invert" with "string", "word", "text", "sentence" or explicit reverse string prompts)
    if ("reverse" in clean or "invert" in clean) and (
        "string" in clean or "word" in clean or "text" in clean or "sentence" in clean
    ) or clean in ("reverse string", "reverse a string", "reverse word", "reverse a word"):
        return "reverse_string"

    # Check 5: Even or odd
    if (
        ("even" in clean and "odd" in clean)
        or ("is even" in clean or "is odd" in clean or "even or odd" in clean or "divisible by 2" in clean)
        or ("even number" in clean or "odd number" in clean)
    ):
        return "even_or_odd"

    # Check 6: Positive, negative or zero
    if (
        ("positive" in clean and "negative" in clean)
        or ("positive" in clean and "zero" in clean)
        or ("negative" in clean and "zero" in clean)
        or (("positive" in clean or "negative" in clean) and ("check" in clean or "find" in clean or "determine" in clean))
    ):
        return "positive_negative_zero"

    # Check 7: Largest of three numbers
    has_three = bool(re.search(r"\b(three|3)\b", clean))
    is_max = bool(re.search(r"\b(largest|greatest|maximum|max|biggest|highest)\b", clean))
    if has_three and is_max:
        return "largest_of_three"

    # Check 8: Smallest of three numbers
    is_min = bool(re.search(r"\b(smallest|minimum|min|lowest|least)\b", clean))
    if has_three and is_min:
        return "smallest_of_three"

    # Check 10: Sum of numbers from 1 to N
    is_sum_word = bool(re.search(r"\b(sum|total|addition|add)\b", clean))
    has_range_pattern = bool(
        re.search(r"\b(1\s+to\s+n|from\s+1\s+to\s+n|first\s+n|1\s+through\s+n|natural\s+numbers|1\s+to\s+10|from\s+1\s+to)\b", clean)
    )
    if is_sum_word and has_range_pattern:
        return "sum_1_to_n"

    # Check 9: Print numbers from 1 to N (or 1 to 10)
    is_print_word = bool(re.search(r"\b(print|display|show|output|generate|count|list)\b", clean))
    has_print_range = bool(
        re.search(r"\b(1\s+to\s+n|1\s+to\s+10|1\s+to\s+\d+|from\s+1\s+to|1\s+through)\b", clean)
    )
    if (is_print_word and has_print_range) or ("numbers from 1 to" in clean):
        return "print_1_to_n"

    # Check 1: Addition of two numbers
    has_two = bool(re.search(r"\b(two|2|both)\b", clean))
    if (
        (is_sum_word or "plus" in clean)
        and (has_two or "two numbers" in clean or "2 numbers" in clean or ("numbers" in clean and "sum" in clean))
        and not has_range_pattern
        and not has_three
    ):
        return "add_two_numbers"

    # Check 2: Subtraction of two numbers
    is_sub_word = bool(re.search(r"\b(subtract|subtraction|difference|minus)\b", clean))
    if is_sub_word and (has_two or "numbers" in clean or "values" in clean) and not has_three:
        return "subtract_two_numbers"

    # Check 3: Multiplication of two numbers
    is_mul_word = bool(re.search(r"\b(multiply|multiplication|product|times)\b", clean))
    if is_mul_word and (has_two or "numbers" in clean or "values" in clean) and not has_three:
        return "multiply_two_numbers"

    # Check 4: Division of two numbers
    is_div_word = bool(re.search(r"\b(divide|division|quotient)\b", clean))
    if is_div_word and (has_two or "numbers" in clean or "values" in clean) and not has_three:
        return "divide_two_numbers"

    # Fallback exact matches for common user phrases
    exact_phrases = {
        "add two numbers": "add_two_numbers",
        "addition of two numbers": "add_two_numbers",
        "find the sum of two numbers": "add_two_numbers",
        "calculate addition of two numbers": "add_two_numbers",
        "take two numbers and print their sum": "add_two_numbers",
        "subtract two numbers": "subtract_two_numbers",
        "subtraction of two numbers": "subtract_two_numbers",
        "multiply two numbers": "multiply_two_numbers",
        "multiplication of two numbers": "multiply_two_numbers",
        "divide two numbers": "divide_two_numbers",
        "division of two numbers": "divide_two_numbers",
        "check whether a number is even or odd": "even_or_odd",
        "check if a number is even or odd": "even_or_odd",
        "even or odd": "even_or_odd",
        "check positive or negative": "positive_negative_zero",
        "positive negative or zero": "positive_negative_zero",
        "find the largest of three numbers": "largest_of_three",
        "largest of three numbers": "largest_of_three",
        "find the smallest of three numbers": "smallest_of_three",
        "smallest of three numbers": "smallest_of_three",
        "print numbers from 1 to 10": "print_1_to_n",
        "print numbers from 1 to n": "print_1_to_n",
        "find the factorial of a number": "factorial",
        "factorial of a number": "factorial",
        "reverse a string": "reverse_string",
        "check whether a string is a palindrome": "check_palindrome",
        "check palindrome": "check_palindrome",
        "count vowels in a string": "count_vowels",
        "check whether a number is prime": "check_prime",
        "check if a number is prime": "check_prime"
    }

    if clean in exact_phrases:
        return exact_phrases[clean]

    return None


# ---------------------------------------------------------------------------
# Main Generation Function
# ---------------------------------------------------------------------------

class GeneratedResult(dict):
    """
    Dictionary response wrapper supporting dict lookup and direct string conversion.
    """
    def __str__(self) -> str:
        return self.get("code", "")


def generate_code(user_prompt: str, difficulty: str = "Beginner") -> GeneratedResult:
    """
    Process the user's natural English prompt and generate corresponding Python code.
    
    Args:
        user_prompt: The plain English description from the user.
        difficulty: 'Beginner', 'Intermediate', or 'Advanced' (defaults to 'Beginner').
        
    Returns:
        GeneratedResult dictionary with:
            success (bool): True if intent recognized and code generated.
            task (str): Human-readable task name.
            task_id (str): Internal task ID.
            difficulty (str): Selected difficulty tier.
            code (str): The Python code string, or the unsupported message.
            message (str): Informational or error message.
    """
    if not isinstance(user_prompt, str) or not user_prompt.strip():
        return GeneratedResult({
            "success": False,
            "task": None,
            "task_id": None,
            "difficulty": difficulty or "Beginner",
            "code": UNSUPPORTED_MESSAGE,
            "message": "Please enter an English instruction to generate Python code."
        })

    # Normalize difficulty
    diff_normalized = (difficulty or "Beginner").strip().capitalize()
    if diff_normalized not in ("Beginner", "Intermediate", "Advanced"):
        diff_normalized = "Beginner"

    # Rule-based intent classification
    task_id = classify_task(user_prompt)

    if not task_id or task_id not in TEMPLATES:
        return GeneratedResult({
            "success": False,
            "task": None,
            "task_id": None,
            "difficulty": diff_normalized,
            "code": UNSUPPORTED_MESSAGE,
            "message": UNSUPPORTED_MESSAGE
        })

    task_templates = TEMPLATES[task_id]
    code = task_templates.get(diff_normalized, task_templates["Beginner"])

    # Lookup friendly task name
    friendly_name = next((t["name"] for t in SUPPORTED_TASKS if t["id"] == task_id), task_id.replace("_", " ").title())

    return GeneratedResult({
        "success": True,
        "task": friendly_name,
        "task_id": task_id,
        "difficulty": diff_normalized,
        "code": code,
        "message": f"Successfully generated Python code for: {friendly_name} ({diff_normalized} mode)."
    })
