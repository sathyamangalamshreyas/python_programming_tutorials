import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Functions
    - A function is a re-usable block of code that performs a specific task. Instead of writing the same logic again and again, the logic is written inside a fucntion and can be called when needed.
    - This follows the DRY (Don't Repeat Yourself) principle
    - Functions make the code easier to read, maintain and debug
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    - Functions are defined using the "def" keyword
    - "def" is followed by the function name and paranthesis
    - It is called by the name followed by paranthesis
    ```
    # Defining a function:
    def function_name():
        # Define function logic
    ```
    ```
    # Calling a function
    function_name()
    ```
    """)
    return


@app.cell
def _():
    # Define a function
    def greet():
        """Simple funtion to greet by time of day"""
        print("Good Morning")
        print("Good Afternoon")
        print("Good Night")

    # Call the function
    greet()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Function that asks a number from a user and prints if that number is odd or even
    """)
    return


@app.cell
def _():
    # Define the function
    def odd_even() -> None:
        """
        Check if a number is odd or even based on user input
        """
        num = int(input("Enter a number: "))
        if num%2 == 0:
            print(f"The number {num} is even")
        else:
            print(f"The number {num} is odd")

    # Call the function
    odd_even()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Write a function that prints all the factors of a number entered by a user
    """)
    return


@app.cell
def _():
    # Define the function
    def usr_factor() -> None:
        """
        List all the factors of number entered by a user
        """
        num_fac = int(input("Enter a number"))
        for i in range(1, num_fac+1):
            if num_fac%i == 0:
                print(i, end=' ')

    # call the function
    usr_factor()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Parameters and Arguments
    - A *parameter* is a variable listed inside the function definition
    - An *argument* is the actual value passed when calling the function
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    '''
    - def greet(*name*): # *name* is a parameter in the function greet
         - print(f"Hello, {name}!")
    '''

    ```
    greet("name_1") # name_1 is the argument
    greet("name_2") # name_2 is the argument
    ```
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Take 3 integers as parameters and print the total
    """)
    return


@app.cell
def _():
    def int_total(num_1: int, num_2: int, num_3: int) -> None:
        """
        input three integers and print the total
        """
        total = num_1 + num_2 + num_3
        print(f"The sum of {num_1},{num_2},and {num_3} is: {total}")

    # call the function twice
    int_total(num_1=1, num_2=2, num_3=3)
    int_total(num_1=3, num_2=4, num_3=5)
    return


@app.cell
def _():
    def usr_details(name: str, age: int, gender: str) -> None:
        """
        Input user details and print them out
        """
        print(f"Name: {name}, Age:{age}, Gender:{gender}")

    # call the function
    usr_details(name="Shreyas", age=44, gender="male")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Questions🪗

    Q1: Write a function called **add** that takes two numbers as parameters and prints their sum

    Q2: Write a function called **rectangle_area** that takes the length and breadth as parameters and prints the area

    Q3: Write a function called **find_max** that takes three numbers as parameters and prints the largest one

    Q4: Write a function called **discount_price** that takes the **original_price** and **discount_percent** as parameters and prints the final price after discount
    """)
    return


@app.cell
def _():
    # Q1
    def add(num_1: float, num_2: float) -> None:
        """
        add two numbers and print the sum
        """
        total = num_1+num_2
        print(f"The sum of {num_1} and {num_2} is: {total}")

    # call add
    add(num_1=5, num_2=10)
    return


@app.cell
def _():
    # Q2
    def rectangle_area(length: float, breadth: float) -> None:
        """
        compute the area of a rectangle
        """
        area = length*breadth
        print(f"The area of the rectangle is: {area}")

    # call rectangle_area
    rectangle_area(length=10, breadth=10)
    return


@app.cell
def _():
    # Q3
    def find_max(n1: float, n2: float, n3: float) -> None:
        """
        find max of three numbers
        """
        max_num = max(n1, n2, n3)
        print(f"The max of {n1}, {n2}, and {n3} is: {max_num}")

    # call find_max
    find_max(n1=30, n2=20, n3=5)
    return


@app.cell
def _():
    # Q4
    def discount_price(original_price: float, discount_percent: float) -> None:
        """
        print discounted price
        """
        price_after_discount = original_price * (discount_percent/100)

        print(f"Discounted price: {price_after_discount}")

    # call discount_price
    discount_price(original_price=100, discount_percent=50)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### return statement
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    - The return statement is used inside a function to send a value back to the place where the function was called
    - Once return is executed, the function stops running, and any code written after it is ignored
    - If no value is returned, Python automatically returns None
    """)
    return


@app.cell
def _():
    # Add three numbers

    def addition(n1: int|float, n2: int|float, n3: int|float) -> int |float:
        """
        returns the sum of three numbers
        """
        total = n1+n2+n3
        return total

    # call addition
    ans = addition(n1=10, n2=20, n3=30)
    print(ans)
    return


@app.cell
def _():
    # Return if a user can vote if age is >=18

    def vote_elig(age: int) -> bool:
        """
        returns if a user can vote based on age criteria
        """
        if age>=18:
            return True
        elif age<0:
            return False
        elif age<18 and age>0:
            return False

    # call the funciton
    vote_crit = vote_elig(age=18)
    print(vote_crit)
    return


@app.cell
def _():
    # Return True if a number is prime, else return False

    def is_prime(num: int) -> bool:
        """
        returns True if number is Prime else False
        """
        count = 0
        for i in range(1, num+1):
            if num%i==0:
                count+=1
        if count == 2:
            return True
        else:
            return False

    # Call is_prime
    prime_num = is_prime(num=20)
    print(prime_num)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Practice Questions
    - Q1: Write a function called *square* that takes a number and returns its square. Print the output
    - Q2: Write a function called *min_of_three* that takes three numbers and returns the smallest without using any in-built function
    - Q3: Write a function called *absolute_value* that takes a number and returns its absolute value without using the built-in abs() function
    """)
    return


@app.cell
def _():
    # Q1
    def square(num: int | float) -> int | float:
        """
        Returns the square of the number
        """
        num_square = num**2
        return num_square

    # call square
    ans_sq = square(num=10)
    print(ans_sq)
    return


@app.cell
def _():
    # Q2
    def min_of_three(n1: int|float, n2: int|float, n3: int|float) -> int|float:
        """
        returns min of three numbers
        """
        if n1<n2 and n1<n3:
            min_num = n1
        elif n2<n1 and n2<n3:
            min_num = n2
        elif n3<n1 and n3<n2:
            min_num = n3
        else:
            min_num = min_num

        return min_num

    # call min_of_three
    min_num = min_of_three(n1=50, n2=10, n3=5)
    print(min_num)
    return


@app.cell
def _():
    # Q3
    def absolute_value(num: int|float) -> int|float:
        """
        returns the absolute value of a number
        """
        abs_value = 0
        if num<0:
            abs_value = num*(-1)
        else:
            abs_value = num

        return abs_value

    # call the function
    abs_value = absolute_value(num=-10)
    print(abs_value)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Default and Keyword Arguments

    ##### From reddit
    A **default argument** is in how it is defined:
    ```
    def ask_ok(prompt, retries=4):
        print "prompt:", prompt, "retries:", retries
    ```

    - prompt is required. retries is not required, and if not given, it will default to 4.
    ```
    >>> ask_ok(1)
    prompt: 1 retries: 4
    >>> ask_ok(1, 5)
    prompt: 1 retries: 5
    >>> ask_ok()
    TypeError (at least 1 value is required, for prompt)
    ```
    A **keyword argument** is in how it is called

    - If I list arguments sequentially when I call ask_ok, they will be put into the parameters in order:

    ```
    >>> ask_ok(1, 5)
    prompt: 1 retries: 5
    ```

    However, I can also reference either parameter by name to specifically slot an argument into a parameter:

    ```
    >>> ask_ok(1, retries=4)
    prompt: 1 retries: 4
    >>> ask_ok(prompt=1, retries=4)
    prompt: 1 retries: 4
    ```
    - Can even be out of order, as long as all positional arguments come before keywords

    ```
    >>> ask_ok(retries=4, prompt=1)
    prompt: 1 retries: 4
    ```
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Local and Global Variables
    - **Scope** refers to where a variable is accessible in the code
    - A variable inside a function is **local** if it exists inside the function
    - A variable created outside all functions is **global** and can be accessed from anywhere in the code
    - Inside a function, *local* variable is given presidence over *global* variable unless specified
    - **Global** keyword can be used to select global variables

    ```
    name = "Shreyas" -> # Global Variable

    def greet():
        message = "Hello" -> # Local Variable
        print(f"{message}, {name}!") -> The global variable can be read from within the function
    ```
    ```
    greet() -> Output -> Hello, Shreyas!
    ```
    ```
    print(message) -> Output -> NameError (because "message" is a local variable)
    ```
    """)
    return


@app.cell
def _():
    # Local variable
    def addition_three(n1: int = 10, n2: int = 10, n3: int = 10) -> int:
        """Add three numbers"""
        total = n1+n2+n3 # total is a local variable
        return total

    # call addition
    ans_add = addition_three()
    print(ans_add)
    return


@app.cell
def _():
    # Global Variable
    name = "Shreyas"

    def greet_name():
        print(f"Hi, {name}!")

    greet_name()
    return


@app.cell
def _():
    # Local presidence over global
    name_1 = "Shreyas"

    def greeting():
        name_1 = "Muskan"
        print(f"Hi, {name_1}!")

    greeting()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Gloabl Keyword
    """)
    return


@app.cell
def _():
    count=0

    def increase():
        global count
        count = 1
        print(f"Value of 'count' inside the function: {count}")

    increase()
    print(f"Value of 'count' outside the function: {count}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Assignment Question

    Write a function *fizzbuzz* that takes a single number and prints *Fizz* if the number is divisible by 3, *Buzz* if the number is divisible by 5, and *FizzBuzz* if the number is divisible by both, otherwise print the number itself
    """)
    return


@app.cell
def _():
    def fizzbuzz(num: int) -> int:
        """
        compute modulus and display fizz, buzz or fizzbuzz
        depending on the modulus
        """
        if num%3 == 0 and num%5 == 0: 
            print("FizzBuzz")
        elif num%5 == 0:
            print("Buzz")
        elif num%3 == 0:
            print("Fizz")
        else: 
            print(f"{num}")

    # call fizzbuzz
    fizzbuzz(15)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
