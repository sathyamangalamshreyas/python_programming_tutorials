import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Escape Sequences

    1. \n - Newline
    2. \t - Tab Space
    3. \\ - Backslash
    4. \" - Double Quotes
    5. \' - Single Quotes
    """)
    return


@app.cell
def _():
    print(f"Hello, World!")

    print(f"Hello, \nWorld!")

    print(f"Hello, \tWorld!")

    print(f"Hello, \\World!") # for the "\" to appear in a print statement

    print(f'My name is "Shreyas"') # use double quotes within single quotes

    print(f"My name is 'Shreyas'") # use single quotes within double quotes

    print(f"My name is \"Shreyas\"") # use the escape character "\" to print double quotes within double quotes

    print(f'My name is \'Shreyas\'') # use the escape character "\" to print single quotes within single quotes
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Arithmetic Operators
    #### Operator Precedence follow BODMAS rule
    """)
    return


@app.cell
def _():
    a = 20
    b = 9

    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a//b) # Floor division
    print(a**b) # Exponent
    print(a%b) # Modulus (remainder)
    return a, b


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Comparison Operators
    #### Comparison operators always return a boolean (True or False)
    """)
    return


@app.cell
def _(a, b):
    c = 5
    d = 10

    print(c==d)
    print(a>b)
    print(a<b)
    print(a>=b)
    print(a<=b)
    print(a!=b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Logical Operators
    #### Logical Operators can be used to combine multiple conditions together
    #### Output is always a boolean (True or False)
    """)
    return


@app.cell
def _():
    chemistry = 45
    physics = 36

    # And Operator
    print(chemistry>35 and physics>35)

    # Or Operator
    print(chemistry>35 or physics>35)

    # Not operator (reverses the results)
    print(f"{not chemistry>10}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Other Operators include
    - Identity Operators
    - Membership Operators
    - Bitwise Operators
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Practice
    - Q1: Take two numbers as input from the user. Print sum, differences, product and remainder
    - Q2: Take a number as input. Print whether it is odd or even using the "%" operator and a comparison operator
    - Q3: Take the user's age as input. Check and print whether they are eligible to vote (age>=18) and whether they are a senior citizen(age>=60). Print both results.
    - Q4: A student scored marks in 3 subjects. Take all three as input, calculate the total and average, and print both using an f-string.
    """)
    return


@app.cell
def _():
    # Q1
    num_1 = input("Input a number:")
    num_2 = input("Input second number:")

    num_1 = int(num_1)
    num_2 = int(num_2)

    print(f"Sum: {num_1+num_2}")
    print(f"Difference: {num_1-num_2}")
    print(f"Product: {num_1*num_2}")
    print(f"Remainder: {num_1%num_2}")
    return


@app.cell
def _():
    # Q2
    usr_inp = input("Input a number:")

    ust_inp_int = int(usr_inp)

    if ust_inp_int%2 == 0:
        print(f"User Input is even")
    else:
        print(f"User input is odd")
    return


@app.cell
def _():
    # Q3
    usr_age = input("Enter your age:")
    usr_age_int = int(usr_age)

    can_vote = usr_age_int>=18
    senior_citizen = usr_age_int>=60

    print(f"The can vote: {can_vote}")
    print(f"The user is a senior citizen: {senior_citizen}")
    return


@app.cell
def _():
    # Q4
    sub_1 = int(input("Enter Subject 1 Marks:"))
    sub_2 = int(input("Enter Subject 2 Marks:"))
    sub_3 = int(input("Enter Subject 3 Marks:"))

    total = sub_1+sub_2+sub_3

    average = (sub_1+sub_2+sub_3)/3

    print(f"Total Marks in three subjects: {total}")
    print(f"Average Marks in three subjects: {average:.2f}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
