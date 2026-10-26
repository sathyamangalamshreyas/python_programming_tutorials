import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### what is a loop?
    a loop lets you run the same block of code multiple times with repeating it.
    Example:

    instead of:
    - print("Hello, World!")
    - print("Hello, World!")
    - print("Hello, World!")

    There are two main types of loops in Python:
    - While loop
    - For loop

    While loop syntax:
    - i = 0
    - while i < 3:
    -    print("Hello, World!")
    -    i += 1
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### A While loop keeps running as long as the condition is True.
    - The Python interpreter checks the condition before each iteration
    - When the condition becomes false, the loop stops
    """)
    return


@app.cell
def _():
    # Print Hello 5 times
    i = 0
    while i < 5:
        try:
            print("Hello")
        except Exception:
            print("Not true")
        i += 1
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print 1 to 10
    """)
    return


@app.cell
def _():
    x = 0
    while x < 10:
        x+=1
        print(x, end=" ")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print 1 to "n", where "n" is a user input
    """)
    return


@app.cell
def _():
    usr_num = int(input("Enter a number:"))

    a = 1
    while a<=usr_num:
        print(a, end=" ")
        a += 1
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### print start to end using while loop
    """)
    return


@app.cell
def _():
    starting_num = int(input("Enter starting number: "))
    ending_num = int(input("Enter ending number: "))

    # Never directly change the input directly in the loop counter
    # while starting_num<=ending_num:
    #     print(starting_num, end=" ")
    #     starting_num+=1

    start_num = starting_num
    end_num = ending_num

    while start_num<=end_num:
        print(start_num, end=" ")
        start_num+=1
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print even numbers based on user input range
    """)
    return


@app.cell
def _():
    usr_inp_1 = int(input("Enter first number in a range: "))
    usr_inp_2 = int(input("Enter second number in a range: "))

    range_start = usr_inp_1
    range_end = usr_inp_2

    # When a decision is needed use a conditional:
    while range_start<=range_end:
        if range_start%2 == 0:
            print(range_start)
        range_start += 1
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print all numbers divisible by both "3" and "4" within a range
    """)
    return


@app.cell
def _():
    usr_inp_3 = int(input("Enter range start value: "))
    usr_inp_4 = int(input("Enter range start value: "))

    r_1 = usr_inp_3
    r_2= usr_inp_4

    while r_1<=r_2:
        if r_1%3 == 0 and r_1%4 == 0:
            print(r_1, end=" ")
        r_1 += 1
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### print 10 to 1
    """)
    return


@app.cell
def _():
    b = 10
    while b>=1:
        print(b, end=" ")
        b -= 1
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print reverse order based on user input
    """)
    return


@app.cell
def _():
    usr_rev_1 = int(input("Enter first number in range: "))
    usr_rev_2 = int(input("Enter last number in range: "))

    c = usr_rev_1
    d = usr_rev_2

    if c<=d:
        while d>=c:
            print(d, end=" ")
            d = d - 1
    else:
        while c>=d:
            print(c, end=" ")
            c = c - 1
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Practice Questions:
    - Q1: Print all the numbers which are divisible by 3, and 5, from 1 to 100
    - Q2: Sum of all numbers from 1 to 100
    - Q3: Sum of all numbers from 1 to 100 divisible by 2 and 7
    - Q4: Ask a number from the user print the multiplication table upto 10
    - Q5: As a number from the user and print all the factors
    """)
    return


@app.cell
def _():
    # Q1
    num_1 = 1
    num_2 = 100

    while num_1<=num_2:
        if num_1%3 == 0 and num_1%5 == 0:
            print(num_1, end=" ")
        num_1 += 1
    return


@app.cell
def _():
    #Q2

    to_add = 1
    amount = 0

    while amount<=100:
            to_add += amount
            amount += 1
    print(to_add)
    return


@app.cell
def _():
    #Q3
    start = int(input("Enter start number: "))
    end = int(input("Enter end number: "))

    i = start
    total = 0

    while i<=end:
        if i%2 == 0 and i%7 == 0:
            total += i
        i += 1

    print(f"Total: {total}")
    return


@app.cell
def _():
    #Q4

    usr_inp_mul = int(input("Enter a number: "))

    a_usr_mul = usr_inp_mul
    i_m = 1

    while i_m<=10:
        print(f"{a_usr_mul} x {i_m} = {a_usr_mul*i_m}")
        i_m += 1
    return


@app.cell
def _():
    #Q5

    fact_usr_inp = int(input("Enter a number: "))

    i_f = 1

    while i_f<=fact_usr_inp:
        if fact_usr_inp%i_f == 0:
            print(f"{i_f} is a factor of {fact_usr_inp}")
        i_f+=1
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### For Loops
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Used to iterate over a sequence - a range of numbers, a string, a list, and so on.

    - Unlike a while loop, we do not have to manage the counter, the Python interpreter manages it
    - Syntax "for variable in sequence:"
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Basic For Loop

    - For the "range" in-built class the syntax is:
         - start(inclusive), stop(exclusive), step(default value of 1)
    """)
    return


@app.cell
def _():
    # Print all numbers from 1 to 10

    for num_3 in range(1, 11):
        print(f"{num_3}", end=" ")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Steps in for loop
    """)
    return


@app.cell
def _():
    for num_4 in range(1, 11, 2):
        print(num_4, end=" ")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Print all nums from 10 to 1
    """)
    return


@app.cell
def _():
    for num_5 in range(10, 0):
        print(num_5)

    # Does not produce an output because step is positive and equal to 1: This means the counter moves from left to right, but the defined for loop moves right to left
    return


@app.cell
def _():
    # Specify step as (-1)
    for num_6 in range(10, 0, -1):
        print(num_6, end=" ")
    return


@app.cell
def _():
    # Print all numbers that are divisible by 2

    for num_7 in range(1, 11):
        if num_7%2==0:
            print(f"The number {num_7} is even")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Dynamic For Loops
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Ask user input for two numbers and print all the numbers in-between
    """)
    return


@app.cell
def _():
    for_usr_inp_1 = int(input("Enter starting number:"))
    for_usr_inp_2 = int(input("Enter ending number: "))

    for z in range(for_usr_inp_1, for_usr_inp_2 + 1): # Note all +1 as stop in exclusive
        print(z, end=" ")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Ask for two inputs, sum all numbers between them
    """)
    return


@app.cell
def _():
    for_inp_num1 = int(input("Enter start num: "))
    for_inp_num2 = int(input("Enter end num: "))

    for_total = 0

    for y in range(for_inp_num1, for_inp_num2+1):
        for_total += y
    print(f"The sum of all numbers between {for_inp_num1} and {for_inp_num2} is {for_total}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Control Statements
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Break Statement:
    - break immediately stops the loop and exits, even if the condition is still True and there are items left in sequence to execute

    #### Continue Statement
    - continue skips the rest of the current iteration and jumps straight to the next one. The loop does not stop, it just skips that particular cycle
    """)
    return


@app.cell
def _():
    # Break statement
    br_i = 1
    br_i_2 = 1

    while br_i <= 10:
        print(f"{br_i}", end=" ")
        br_i += 1

    print(f"\n")

    while br_i_2 <= 10:
        print(f"{br_i_2}", end= " ")
        if br_i_2 == 5:
            break
        br_i_2 += 1
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Practice Question
    Take numbers as input from the user one-by-one. Skip negative numbers and keep adding positive ones. Stop when the user enters 0 and print the total. Use both continue and break statements.
    """)
    return


@app.cell
def _():
    total = 0
    while True:
        usr_num_7 = int(input("Enter a number:"))
        if usr_num_7 == 0:
            break
        if usr_num_7<0:
            continue
        total += usr_num_7
    print(f"Total: {total}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Using "continue" within a for loop
    """)
    return


@app.cell
def _():
    for i_br in range(1, 11):
        if i_br%2 == 0:
            continue
        print(f"{i_br}", end=' ')
    return


if __name__ == "__main__":
    app.run()
