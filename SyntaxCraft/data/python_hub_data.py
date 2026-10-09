"""
SyntaxCraft - Python Hub Learning Data
17 essential beginner topics with explanations, syntax, examples, and practice questions.
"""

HUB_TOPICS = [
    {
        "id": "variables",
        "title": "1. Variables",
        "category": "Basics",
        "explanation": "Variables are named storage containers that hold data values in memory. Python uses dynamic typing, meaning you don't need to declare variable types explicitly.",
        "syntax": "variable_name = value",
        "example": "score = 95\nplayer_name = \"Alex\"\nis_game_over = False\n\nprint(player_name, score)",
        "question": "Create a variable named 'student_id' storing 101, and print its value."
    },
    {
        "id": "data_types",
        "title": "2. Data Types",
        "category": "Basics",
        "explanation": "Python features built-in primitive types: int (whole numbers), float (decimals), str (text), and bool (True/False). Use type() to inspect any object's type.",
        "syntax": "type(variable)",
        "example": "age = 21            # int\ngpa = 3.85          # float\nbranch = \"CSE\"      # str\nis_enrolled = True  # bool\n\nprint(type(gpa))    # <class 'float'>",
        "question": "What is the data type of the expression: 10 / 2?"
    },
    {
        "id": "input_output",
        "title": "3. Input and Output",
        "category": "Basics",
        "explanation": "input() captures keyboard input as a string. print() displays text or variables to the screen with optional sep and end arguments.",
        "syntax": "user_text = input('Prompt: ')\nprint(val1, val2, sep=', ', end='\\n')",
        "example": "name = input(\"Enter your name: \")\nprint(f\"Hello, {name}! Welcome to SyntaxCraft.\")",
        "question": "Write a snippet to ask for an age and convert it to an integer."
    },
    {
        "id": "operators",
        "title": "4. Operators",
        "category": "Basics",
        "explanation": "Operators perform computations: Arithmetic (+, -, *, /, //, %, **), Comparison (==, !=, <, >, <=, >=), and Logical (and, or, not).",
        "syntax": "result = a + b\nis_valid = (x > 0) and (y < 10)",
        "example": "a, b = 15, 4\nprint(\"Floor Division:\", a // b)  # 3\nprint(\"Remainder:\", a % b)       # 3\nprint(\"Exponent:\", a ** 2)        # 225",
        "question": "What is the result of 17 % 5 in Python?"
    },
    {
        "id": "conditionals",
        "title": "5. Conditional Statements",
        "category": "Control Flow",
        "explanation": "Conditionals execute specific code blocks only when a boolean condition is True, using four-space indentation to define scope.",
        "syntax": "if condition1:\n    # code block\nelif condition2:\n    # code block\nelse:\n    # fallback block",
        "example": "marks = 82\nif marks >= 90:\n    print(\"Grade A\")\nelif marks >= 75:\n    print(\"Grade B\")\nelse:\n    print(\"Grade C\")",
        "question": "Write an if-else check that prints 'Access Granted' if age >= 18."
    },
    {
        "id": "loops",
        "title": "6. Loops",
        "category": "Control Flow",
        "explanation": "for-loops iterate over sequences (like range, list, or string). while-loops repeat statements as long as a boolean condition remains True.",
        "syntax": "for item in iterable:\n    ...\nwhile condition:\n    ...",
        "example": "# Loop through range 1 to 5\nfor i in range(1, 6):\n    print(i, end=\" \")\nprint()\n\n# While loop countdown\ncount = 3\nwhile count > 0:\n    print(count)\n    count -= 1",
        "question": "How many times does range(0, 10, 2) iterate?"
    },
    {
        "id": "strings",
        "title": "7. Strings",
        "category": "Data Structures",
        "explanation": "Strings are immutable sequences of Unicode characters. They support slicing [start:stop:step] and helpful methods like upper(), strip(), replace().",
        "syntax": "s = \"python\"\nslice = s[start:stop:step]",
        "example": "course = \"  python programming  \"\nprint(course.strip().title())   # 'Python Programming'\nprint(course[2:8])              # 'python'",
        "question": "How do you reverse the string s = 'hello' using slicing?"
    },
    {
        "id": "lists",
        "title": "8. Lists",
        "category": "Data Structures",
        "explanation": "Lists are mutable, ordered collections that can hold mixed data types. Modify them using append(), insert(), pop(), or list slicing.",
        "syntax": "my_list = [item1, item2, item3]\nmy_list.append(new_item)",
        "example": "fruits = [\"apple\", \"banana\", \"cherry\"]\nfruits.append(\"mango\")\nfruits[1] = \"blueberry\"\nprint(fruits)  # ['apple', 'blueberry', 'cherry', 'mango']",
        "question": "Which method removes the last element from a list?"
    },
    {
        "id": "tuples",
        "title": "9. Tuples",
        "category": "Data Structures",
        "explanation": "Tuples are immutable ordered collections written with parentheses (). Because they cannot be altered after creation, they are faster and memory-safe.",
        "syntax": "coords = (x, y)\nvalue = coords[0]",
        "example": "point = (10, 20)\nx, y = point  # Tuple unpacking\nprint(f\"X={x}, Y={y}\")",
        "question": "Can you append an item to an existing tuple in Python? Why?"
    },
    {
        "id": "dictionaries",
        "title": "10. Dictionaries",
        "category": "Data Structures",
        "explanation": "Dictionaries store key-value pairs with fast O(1) average lookup times. Keys must be unique and immutable (such as strings or numbers).",
        "syntax": "my_dict = {key1: val1, key2: val2}\nval = my_dict[key1]",
        "example": "student = {\"name\": \"Priya\", \"roll\": 42, \"major\": \"IT\"}\nstudent[\"grade\"] = \"A+\"\nprint(student[\"name\"])  # Priya",
        "question": "How do you safely fetch a dictionary key without causing a KeyError if missing?"
    },
    {
        "id": "sets",
        "title": "11. Sets",
        "category": "Data Structures",
        "explanation": "Sets are unordered collections of unique elements. They automatically discard duplicate values and support union (|), intersection (&), and difference (-).",
        "syntax": "unique_items = {1, 2, 3}\nunique_items.add(4)",
        "example": "nums = [1, 2, 2, 3, 4, 4, 5]\nunique_set = set(nums)\nprint(unique_set)  # {1, 2, 3, 4, 5}",
        "question": "How do you find common elements between two sets s1 and s2?"
    },
    {
        "id": "functions",
        "title": "12. Functions",
        "category": "Functions",
        "explanation": "Functions are reusable blocks of code defined with the def keyword. They take arguments, execute statements, and return results.",
        "syntax": "def func_name(param1, param2):\n    return result",
        "example": "def calculate_area(length, width):\n    \"\"\"Calculate rectangular area.\"\"\"\n    return length * width\n\nprint(\"Area:\", calculate_area(5, 8))  # 40",
        "question": "What is returned by a Python function that does not include a return statement?"
    },
    {
        "id": "lambda",
        "title": "13. Lambda Functions",
        "category": "Functions",
        "explanation": "A lambda is a small anonymous function defined in a single line. It can take any number of arguments but only contains a single expression.",
        "syntax": "func = lambda arg1, arg2: expression",
        "example": "square = lambda x: x ** 2\nmultiply = lambda a, b: a * b\n\nprint(square(6))      # 36\nprint(multiply(3, 4)) # 12",
        "question": "Write a lambda function that checks if a number x is even."
    },
    {
        "id": "map",
        "title": "14. map() Function",
        "category": "Functional Tools",
        "explanation": "map(function, iterable) applies a specified function to every element in an iterable sequence and returns an iterator.",
        "syntax": "result_iterator = map(function, iterable)",
        "example": "numbers = [1, 2, 3, 4, 5]\nsquares = list(map(lambda x: x ** 2, numbers))\nprint(squares)  # [1, 4, 9, 16, 25]",
        "question": "Use map() to convert a list of string numbers ['1', '2', '3'] into integers."
    },
    {
        "id": "filter",
        "title": "15. filter() Function",
        "category": "Functional Tools",
        "explanation": "filter(function, iterable) constructs an iterator from elements of an iterable for which the predicate function returns True.",
        "syntax": "result_iterator = filter(predicate_function, iterable)",
        "example": "numbers = [12, 17, 24, 31, 40]\nevens = list(filter(lambda x: x % 2 == 0, numbers))\nprint(evens)  # [12, 24, 40]",
        "question": "Use filter() to select numbers greater than 10 from [5, 12, 8, 20]."
    },
    {
        "id": "oop",
        "title": "16. Object-Oriented Programming (OOP)",
        "category": "Advanced",
        "explanation": "OOP bundles data (attributes) and behavior (methods) into Classes. Objects are specific instances created from these class blueprints.",
        "syntax": "class ClassName:\n    def __init__(self, arg):\n        self.attr = arg",
        "example": "class Student:\n    def __init__(self, name, score):\n        self.name = name\n        self.score = score\n        \n    def has_passed(self):\n        return self.score >= 50\n\ns1 = Student(\"Rahul\", 78)\nprint(s1.name, s1.has_passed())  # Rahul True",
        "question": "What is the purpose of the 'self' parameter in Python class methods?"
    },
    {
        "id": "exceptions",
        "title": "17. Exception Handling",
        "category": "Advanced",
        "explanation": "Exception handling intercepts runtime errors gracefully using try, except, else, and finally blocks, preventing application crashes.",
        "syntax": "try:\n    # risky code\nexcept ErrorType as e:\n    # recovery code\nfinally:\n    # always executes",
        "example": "try:\n    num = int(input(\"Enter number: \"))\n    print(\"100 / num =\", 100 / num)\nexcept ZeroDivisionError:\n    print(\"Cannot divide by zero!\")\nexcept ValueError:\n    print(\"Invalid input! Please enter an integer.\")",
        "question": "Which block in try-except always executes whether an error occurred or not?"
    }
]
