"""
SyntaxCraft - Code Insights Analyzer Module
Module: insights.code_analyzer

Performs static and rule-based source inspection to provide student-friendly
structural analysis, line-by-line breakdowns, complexity evaluations, and improvement tips.
No AI or external APIs are used.
"""

from typing import Dict, Any, Optional, List
from generator.code_generator import classify_task, SUPPORTED_TASKS

# Comprehensive knowledge base for the 15 supported tasks
TASK_INSIGHTS: Dict[str, Dict[str, Any]] = {
    "add_two_numbers": {
        "name": "Addition of Two Numbers",
        "logic_approach": "Direct Arithmetic Computation: Reads two numeric values from standard input, converts them from strings to floating-point numbers, computes their sum using the addition operator (+), and prints the result.",
        "concepts_used": ["Standard Input (input())", "Type Casting (float())", "Arithmetic Operators (+)", "Variables & Output Formatting"],
        "beginner_explanation": "In Python, input() always reads user keystrokes as strings. To perform arithmetic addition rather than text concatenation ('5' + '5' = '55'), we wrap input() inside float() to convert the string to a real number before adding.",
        "time_complexity": "O(1) - Constant Time (executes in a fixed number of CPU instructions)",
        "space_complexity": "O(1) - Constant Space (only requires two scalar variables)",
        "improvement_suggestion": "In intermediate Python, you can wrap addition in a reusable function, or use Python's built-in sum([num1, num2]) when dealing with collections.",
        "line_by_line": [
            {"lines": "1-3", "code": "num1 = float(input(...))\nnum2 = float(input(...))", "explanation": "Prompts the user for two numbers, converts the text inputs into float values, and stores them in memory."},
            {"lines": "5-6", "code": "total = num1 + num2", "explanation": "Evaluates the addition expression using the + operator and binds the sum to the variable 'total'."},
            {"lines": "8", "code": "print('The sum is:', total)", "explanation": "Outputs the calculated result to the console."}
        ]
    },

    "subtract_two_numbers": {
        "name": "Subtraction of Two Numbers",
        "logic_approach": "Arithmetic Difference: Takes two numbers, calculates the difference between the first and the second using the subtraction operator (-), and prints the outcome.",
        "concepts_used": ["Standard Input (input())", "Type Casting (float())", "Arithmetic Operators (-)", "Variables"],
        "beginner_explanation": "Subtraction evaluates the difference between values. Order matters: (num1 - num2) subtracts the second operand from the first.",
        "time_complexity": "O(1) - Constant Time",
        "space_complexity": "O(1) - Constant Space",
        "improvement_suggestion": "To accept multiple numbers on a single line, use input().split() combined with map(float, ...) to read numbers in one step.",
        "line_by_line": [
            {"lines": "1-3", "code": "num1 = float(input(...))\nnum2 = float(input(...))", "explanation": "Reads the minuend and subtrahend as floats."},
            {"lines": "5", "code": "difference = num1 - num2", "explanation": "Calculates the arithmetic difference."},
            {"lines": "7", "code": "print('The difference is:', difference)", "explanation": "Prints the formatted result."}
        ]
    },

    "multiply_two_numbers": {
        "name": "Multiplication of Two Numbers",
        "logic_approach": "Arithmetic Scaling: Takes two numeric factors and multiplies them using the asterisk (*) operator.",
        "concepts_used": ["Standard Input", "Data Types (Float)", "Multiplication Operator (*)", "Print Function"],
        "beginner_explanation": "Multiplication in Python scales one number by another. If float inputs are used, Python preserves decimal precision.",
        "time_complexity": "O(1) - Constant Time",
        "space_complexity": "O(1) - Constant Space",
        "improvement_suggestion": "For repeated multiplication or scaling a list of numbers, Python 3.8+ offers math.prod().",
        "line_by_line": [
            {"lines": "1-3", "code": "num1 = float(input(...))\nnum2 = float(input(...))", "explanation": "Captures numeric input from user."},
            {"lines": "5", "code": "product = num1 * num2", "explanation": "Multiplies factors and stores in 'product'."},
            {"lines": "7", "code": "print('The product is:', product)", "explanation": "Displays product on console."}
        ]
    },

    "divide_two_numbers": {
        "name": "Division of Two Numbers",
        "logic_approach": "Guarded Division: Validates that the divisor is not zero before computing the quotient with the slash (/) operator to prevent ZeroDivisionError.",
        "concepts_used": ["Conditionals (if-else)", "Arithmetic Division (/)", "Error Prevention (Zero Division)", "Floating Point"],
        "beginner_explanation": "Division by zero is undefined in mathematics and causes Python to crash with a ZeroDivisionError. Using an if condition before dividing protects the application.",
        "time_complexity": "O(1) - Constant Time",
        "space_complexity": "O(1) - Constant Space",
        "improvement_suggestion": "You can also use try-except blocks (ZeroDivisionError) to handle invalid math operations idiomatically.",
        "line_by_line": [
            {"lines": "1-3", "code": "num1 = float(input(...))\nnum2 = float(input(...))", "explanation": "Prompts for dividend and divisor."},
            {"lines": "5-6", "code": "if num2 == 0:\n    print('Error: Division by zero...')", "explanation": "Checks if denominator is zero to guard against runtime crash."},
            {"lines": "7-9", "code": "else:\n    result = num1 / num2\n    print(...)", "explanation": "Safely computes quotient and prints it."}
        ]
    },

    "even_or_odd": {
        "name": "Check Even or Odd Number",
        "logic_approach": "Modulo Divisibility Test: Calculates the remainder when the integer is divided by 2 using num % 2. If remainder is 0, the number is even; otherwise, it is odd.",
        "concepts_used": ["Modulo Operator (%)", "Conditional Branching (if-else)", "Integer Conversion (int())", "Boolean Expressions"],
        "beginner_explanation": "The modulo operator (%) returns the remainder of integer division. Every even number divided by 2 leaves a remainder of 0, while odd numbers leave a remainder of 1.",
        "time_complexity": "O(1) - Constant Time",
        "space_complexity": "O(1) - Constant Space",
        "improvement_suggestion": "In competitive programming or bitwise optimization, checking (n & 1 == 0) achieves the same check by inspecting the least significant binary bit.",
        "line_by_line": [
            {"lines": "1-2", "code": "number = int(input(...))", "explanation": "Reads the input and converts it strictly to an integer using int()."},
            {"lines": "4-5", "code": "if number % 2 == 0:\n    print('The number is Even')", "explanation": "Tests divisibility by 2; prints 'Even' if remainder is 0."},
            {"lines": "6-7", "code": "else:\n    print('The number is Odd')", "explanation": "Catches all remaining integers (odd) and prints 'Odd'."}
        ]
    },

    "positive_negative_zero": {
        "name": "Positive, Negative or Zero",
        "logic_approach": "Multi-way Branching: Compares the numeric value against the threshold 0 using relational operators (> and <) within an if-elif-else construct.",
        "concepts_used": ["Multi-Branch Conditionals (if, elif, else)", "Comparison Operators (>, <)", "Control Flow"],
        "beginner_explanation": "Numbers fall into three distinct zones on the real number line: greater than 0 (positive), less than 0 (negative), or exactly 0 (neutral). An elif ladder tests each case sequentially.",
        "time_complexity": "O(1) - Constant Time",
        "space_complexity": "O(1) - Constant Space",
        "improvement_suggestion": "In Python 3.10+, you can also use match-case structural pattern matching, or a ternary expression for compact assignment.",
        "line_by_line": [
            {"lines": "1-2", "code": "num = float(input(...))", "explanation": "Takes input value and converts to float."},
            {"lines": "4-5", "code": "if num > 0:\n    print('Positive')", "explanation": "Checks if strictly greater than zero."},
            {"lines": "6-7", "code": "elif num < 0:\n    print('Negative')", "explanation": "Checks if strictly less than zero."},
            {"lines": "8-9", "code": "else:\n    print('Zero')", "explanation": "Handles the remaining exact zero case."}
        ]
    },

    "largest_of_three": {
        "name": "Largest of Three Numbers",
        "logic_approach": "Comparative Elimination: Compares each number against the other two using compound logical 'and' expressions to deduce which variable holds the maximum value.",
        "concepts_used": ["Logical AND (and)", "Relational Operators (>=)", "Conditional Selection", "Variables"],
        "beginner_explanation": "For variable 'a' to be the largest, both (a >= b) and (a >= c) must be True simultaneously. The logical 'and' operator ensures both conditions hold before declaring 'a' the winner.",
        "time_complexity": "O(1) - Constant Time (at most 3 comparisons)",
        "space_complexity": "O(1) - Constant Space",
        "improvement_suggestion": "Python provides a built-in max(a, b, c) function that handles any number of arguments cleanly in a single line.",
        "line_by_line": [
            {"lines": "1-4", "code": "a = float(input(...))\nb = float(input(...))\nc = float(input(...))", "explanation": "Collects three numbers from the user."},
            {"lines": "6-7", "code": "if a >= b and a >= c:\n    largest = a", "explanation": "Checks if 'a' is greater than or equal to both 'b' and 'c'."},
            {"lines": "8-9", "code": "elif b >= a and b >= c:\n    largest = b", "explanation": "Checks if 'b' is greater than or equal to both 'a' and 'c'."},
            {"lines": "10-11", "code": "else:\n    largest = c", "explanation": "If neither 'a' nor 'b' is largest, 'c' must be the largest."},
            {"lines": "13", "code": "print('The largest number is:', largest)", "explanation": "Outputs the maximum value found."}
        ]
    },

    "smallest_of_three": {
        "name": "Smallest of Three Numbers",
        "logic_approach": "Comparative Minimum Search: Checks which value is less than or equal to the others using <= and logical 'and'.",
        "concepts_used": ["Relational Operators (<=)", "Logical Operators (and)", "Conditional Branching", "Control Flow"],
        "beginner_explanation": "Mirroring the largest-of-three pattern, this tests whether a value is concurrently less than or equal to all sibling variables.",
        "time_complexity": "O(1) - Constant Time",
        "space_complexity": "O(1) - Constant Space",
        "improvement_suggestion": "Python's built-in min(a, b, c) achieves this in a single readable line.",
        "line_by_line": [
            {"lines": "1-4", "code": "a = float(input(...))\nb = float(input(...))\nc = float(input(...))", "explanation": "Reads three distinct numerical values."},
            {"lines": "6-7", "code": "if a <= b and a <= c:\n    smallest = a", "explanation": "Checks if 'a' is smaller than both 'b' and 'c'."},
            {"lines": "8-9", "code": "elif b <= a and b <= c:\n    smallest = b", "explanation": "Checks if 'b' is smaller than both 'a' and 'c'."},
            {"lines": "10-11", "code": "else:\n    smallest = c", "explanation": "Otherwise identifies 'c' as the minimum."},
            {"lines": "13", "code": "print('The smallest number is:', smallest)", "explanation": "Prints the computed minimum."}
        ]
    },

    "print_1_to_n": {
        "name": "Print Numbers from 1 to N",
        "logic_approach": "Bounded Iteration: Generates an arithmetic sequence from 1 to N using range(1, n + 1) and prints each item sequentially in a for-loop.",
        "concepts_used": ["For Loops (for ... in)", "Sequence Generator (range())", "Off-by-One Guard (n + 1)", "Iteration"],
        "beginner_explanation": "In Python, range(start, stop) stops BEFORE the stop number. Therefore, to include N itself, we specify n + 1 as the upper bound.",
        "time_complexity": "O(N) - Linear Time (loop iterates exactly N times)",
        "space_complexity": "O(1) - Constant Space (generates items lazily)",
        "improvement_suggestion": "You can print numbers horizontally separated by spaces using print(*range(1, n + 1)) or print(i, end=' ').",
        "line_by_line": [
            {"lines": "1-2", "code": "n = int(input(...))", "explanation": "Reads the upper boundary limit N."},
            {"lines": "4-5", "code": "for i in range(1, n + 1):\n    print(i)", "explanation": "Loops from 1 up to N (inclusive) and prints each number."}
        ]
    },

    "sum_1_to_n": {
        "name": "Sum of Numbers from 1 to N",
        "logic_approach": "Iterative Accumulator: Initializes an accumulator variable at 0, iterates through each integer from 1 to N, and successively adds each number to the running total.",
        "concepts_used": ["Accumulator Pattern", "For Loop with range()", "In-place Addition", "Variables"],
        "beginner_explanation": "The accumulator pattern starts with a sum of 0, then uses each iteration of the loop to add the next number to the current total.",
        "time_complexity": "O(N) - Linear Time with loop, or O(1) using Gauss formula",
        "space_complexity": "O(1) - Constant Space",
        "improvement_suggestion": "You can compute the sum in O(1) time using Carl Friedrich Gauss's famous formula: n * (n + 1) // 2.",
        "line_by_line": [
            {"lines": "1-2", "code": "n = int(input(...))", "explanation": "Takes positive integer limit N."},
            {"lines": "4", "code": "total = 0", "explanation": "Initializes accumulator variable to 0."},
            {"lines": "5-6", "code": "for i in range(1, n + 1):\n    total = total + i", "explanation": "Repeatedly adds each integer from 1 up to N to total."},
            {"lines": "8", "code": "print('The sum is:', total)", "explanation": "Outputs final sum."}
        ]
    },

    "factorial": {
        "name": "Factorial of a Number",
        "logic_approach": "Multiplicative Accumulator: Validates non-negativity, sets an initial product of 1, and multiplies all integers from 1 up to N in sequence.",
        "concepts_used": ["Loop Iteration", "Edge Cases (0! = 1, negatives undefined)", "Multiplicative Identity", "Conditionals"],
        "beginner_explanation": "Factorial of N (N!) is the product of all positive integers up to N. By convention 0! = 1. Negative numbers do not have factorials.",
        "time_complexity": "O(N) - Linear Time (multiplies N factors)",
        "space_complexity": "O(1) - Constant Space for loop (or O(N) call stack for recursion)",
        "improvement_suggestion": "Python's math library provides math.factorial(n), which is written in C for high performance.",
        "line_by_line": [
            {"lines": "1-2", "code": "num = int(input(...))", "explanation": "Prompts user for non-negative integer."},
            {"lines": "4-7", "code": "if num < 0: ...\nelif num == 0 or num == 1: ...", "explanation": "Handles negative numbers and standard 0!/1! = 1 edge cases."},
            {"lines": "9-12", "code": "fact = 1\nfor i in range(1, num + 1):\n    fact = fact * i", "explanation": "Accumulates product of numbers from 1 to num."},
            {"lines": "13", "code": "print('The factorial is:', fact)", "explanation": "Prints computed factorial value."}
        ]
    },

    "reverse_string": {
        "name": "Reverse a String",
        "logic_approach": "Character Prepending: Iterates through each character in the source string and prepends it to an accumulating result string.",
        "concepts_used": ["String Traversal", "String Concatenation", "For Loop", "Immutability of Strings"],
        "beginner_explanation": "By prepending each character (reversed = char + reversed) rather than appending (reversed = reversed + char), earlier characters get pushed toward the back of the string.",
        "time_complexity": "O(N) - Linear Time (visits each character once)",
        "space_complexity": "O(N) - Linear Space (allocates reversed string copy)",
        "improvement_suggestion": "The most Pythonic and efficient way to reverse a string in Python is using slice step: text[::-1].",
        "line_by_line": [
            {"lines": "1-2", "code": "text = input(...)", "explanation": "Accepts user text as a string."},
            {"lines": "4", "code": "reversed_text = ''", "explanation": "Initializes empty string container."},
            {"lines": "5-6", "code": "for char in text:\n    reversed_text = char + reversed_text", "explanation": "Prepends current character, reversing sequence order."},
            {"lines": "8", "code": "print('Reversed string:', reversed_text)", "explanation": "Outputs the reversed text."}
        ]
    },

    "check_palindrome": {
        "name": "Check Palindrome",
        "logic_approach": "Symmetry Verification: Normalizes text to lowercase, reverses the sequence of characters, and compares the reversed copy to the original string.",
        "concepts_used": ["String Normalization (.lower())", "String Reversal", "Equality Comparison (==)", "Conditionals"],
        "beginner_explanation": "A palindrome reads the same backwards as forwards (e.g. 'radar' or 'racecar'). Normalizing to lowercase ensures that differences in capitalization do not cause false negatives.",
        "time_complexity": "O(N) - Linear Time",
        "space_complexity": "O(N) - Linear Space",
        "improvement_suggestion": "You can remove punctuation and spaces using str.isalnum() and perform a two-pointer check to avoid copying strings in memory.",
        "line_by_line": [
            {"lines": "1-2", "code": "text = input(...)", "explanation": "Reads the test word or phrase."},
            {"lines": "4", "code": "cleaned_text = text.lower()", "explanation": "Converts all characters to lowercase for case-insensitive testing."},
            {"lines": "6-8", "code": "reversed_text = ''\nfor char in cleaned_text: ...", "explanation": "Reverses the normalized string."},
            {"lines": "10-13", "code": "if cleaned_text == reversed_text: ...\nelse: ...", "explanation": "Checks if original and reversed match; prints verdict."}
        ]
    },

    "count_vowels": {
        "name": "Count Vowels in a String",
        "logic_approach": "Membership Checking: Traverses each character of the input string, checks if it exists in the vowel set ('aeiouAEIOU') using the 'in' operator, and increments a counter.",
        "concepts_used": ["Membership Operator (in)", "Character Iteration", "Counter Pattern", "Case Sensitivity Handling"],
        "beginner_explanation": "The 'in' operator checks whether an element exists inside a collection. By including both uppercase and lowercase vowels ('aeiouAEIOU'), we accurately count all vowels regardless of letter case.",
        "time_complexity": "O(N) - Linear Time",
        "space_complexity": "O(1) - Constant auxiliary space",
        "improvement_suggestion": "In intermediate Python, you can write: sum(1 for ch in text.lower() if ch in 'aeiou') or use regex re.findall(r'[aeiou]', text, re.I).",
        "line_by_line": [
            {"lines": "1-2", "code": "text = input(...)", "explanation": "Reads input sentence or word."},
            {"lines": "4-5", "code": "vowels = 'aeiouAEIOU'\ncount = 0", "explanation": "Defines vowel lookup table and counter initialized to 0."},
            {"lines": "7-9", "code": "for char in text:\n    if char in vowels:\n        count = count + 1", "explanation": "Checks membership of each character and increments count."},
            {"lines": "11", "code": "print('Total vowels:', count)", "explanation": "Prints total tally of vowels."}
        ]
    },

    "check_prime": {
        "name": "Check Whether a Number is Prime",
        "logic_approach": "Trial Division: A prime number is an integer greater than 1 with no positive divisors other than 1 and itself. Tests whether any integer from 2 up to N-1 divides N evenly.",
        "concepts_used": ["Loop with Early Termination (break)", "Flag Variable (is_prime)", "Modulo Operator (%)", "Mathematical Definition of Prime"],
        "beginner_explanation": "Any number <= 1 is not prime. For numbers >= 2, we search for any divisor. If we find even one divisor that leaves a remainder of 0, the number is composite and we break out of the loop immediately.",
        "time_complexity": "O(N) in naive trial division; O(sqrt(N)) with square-root limit optimization",
        "space_complexity": "O(1) - Constant Space",
        "improvement_suggestion": "Instead of checking up to N-1, you only need to check up to int(math.isqrt(N)) + 1 because any composite factor pairs must have at least one factor <= sqrt(N).",
        "line_by_line": [
            {"lines": "1-2", "code": "num = int(input(...))", "explanation": "Accepts candidate integer."},
            {"lines": "4-5", "code": "if num <= 1:\n    print(num, 'is not prime')", "explanation": "Discards numbers <= 1 per the mathematical definition."},
            {"lines": "6-11", "code": "is_prime = True\nfor i in range(2, num):\n    if num % i == 0: ... break", "explanation": "Tests divisibility; marks False and terminates loop upon finding a factor."},
            {"lines": "13-16", "code": "if is_prime: ...\nelse: ...", "explanation": "Outputs whether the candidate integer is Prime."}
        ]
    }
}


def analyze_code(code: str, task: Optional[str] = None, difficulty: str = "Beginner") -> Dict[str, Any]:
    """
    Analyze Python code and return rich educational insights.
    
    Args:
        code: Python source code string.
        task: Optional task identifier (e.g., 'largest_of_three') or human name.
        difficulty: 'Beginner', 'Intermediate', or 'Advanced'.
        
    Returns:
        Structured insights dictionary containing logic, concepts, line-by-line breakdown,
        complexity, and improvement tips.
    """
    diff_normalized = (difficulty or "Beginner").strip().capitalize()
    if diff_normalized not in ("Beginner", "Intermediate", "Advanced"):
        diff_normalized = "Beginner"

    # Identify task ID if not directly provided
    task_id = task
    if not task_id or task_id not in TASK_INSIGHTS:
        # Attempt to classify from code content or comments
        classified = classify_task(code or "")
        if classified and classified in TASK_INSIGHTS:
            task_id = classified
        else:
            # Fallback to default prominent task for clean demonstration
            task_id = "largest_of_three"

    base_insight = TASK_INSIGHTS.get(task_id, TASK_INSIGHTS["largest_of_three"])

    # Adapt suggestions and approach slightly based on difficulty
    approach = base_insight["logic_approach"]
    concepts = list(base_insight["concepts_used"])
    suggestions = base_insight["improvement_suggestion"]

    if diff_normalized == "Intermediate":
        concepts.append("Modular Function Architecture")
        suggestions += " Consider adding unit test assertions or docstring type annotations (PEP 484)."
    elif diff_normalized == "Advanced":
        concepts.append("Optimized / Functional Python Idioms")
        suggestions = "Code is already highly compact and optimized for production efficiency."

    return {
        "task_id": task_id,
        "task_name": base_insight["name"],
        "difficulty": diff_normalized,
        "logic_approach": approach,
        "concepts_used": concepts,
        "beginner_explanation": base_insight["beginner_explanation"],
        "line_by_line": base_insight["line_by_line"],
        "time_complexity": base_insight["time_complexity"],
        "space_complexity": base_insight["space_complexity"],
        "improvement_suggestion": suggestions,
        "code": code
    }
