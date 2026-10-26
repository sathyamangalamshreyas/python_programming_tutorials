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
    ##### Assign values to variables
    """)
    return


@app.cell
def _():
    name = "Shreyas"
    age = 44
    gender = "Male"
    is_student = True
    return age, gender, is_student, name


@app.cell
def _(age, gender, name):
    print(name)
    print(age)
    print(gender)
    return


@app.cell
def _():
    # Variables names are case sensitive
    age_1 = 44
    Age_1 = 45
    AGE_1 = 46

    print(age_1, Age_1, AGE_1)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Data Types
    """)
    return


@app.cell
def _(age, is_student, name):
    # data types of variables

    print(type(name))
    print(type(age))
    print(type(is_student))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Print Statement
    """)
    return


@app.cell
def _(age, gender, name):
    print("Hello",name, "your age is", age, "and your gender is", gender)
    return


@app.cell
def _(gender, name):
    # cannot use "+" in print statement with different datatypes
    print("My name is " + name, "and my gender is " + gender) # Both strings, works fine
    # print("My name is " + name, "and my gender is " + gender, "and my age is" + age) # Throws an error
    # HINT: 
    # Use print("My name is " + name, "and my gender is " + gender, "and my age is", age) and print ignores the "," separator
    return


@app.cell
def _(age, gender, name):
    # default separator is space
    print(name, age, gender, sep="|")
    return


@app.cell
def _(age, gender, name):
    # By default each print statement ends with a newline
    print(name)
    print(age)
    print(gender)

    print("-" * 50)

    # Modify the default endpoint with the "end" keyword
    print(name, end=" ")
    print(age, end=" ")
    print(gender)
    return


@app.cell
def _(age, name):
    # f-string (formatting string)
    print(f"My name is {name} and my age is {age}")

    # Expressions can be used
    print(f"My future age is {age+10}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Type Conversion
    """)
    return


@app.cell
def _():
    # Explicit Type Conversion
    num_1 = "100"
    num_2 = "200"
    print(num_1 + num_2)

    num_3 = int(num_1)
    num_4 = int(num_2)

    print(num_3 + num_4)
    return num_1, num_2


@app.cell
def _(num_1, num_2):
    # Can also be converted at runtime
    print(int(num_1) + int(num_2))

    print(type(num_1))
    print(type(num_2))
    return


@app.cell
def _():
    # Type Conversion uses the lower bound
    a = 10.9
    b = int(a)
    print(b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### User Input

    By Default the Input is considered as a string
    """)
    return


@app.cell
def _():
    inp_1 = input("Enter a number = ")
    print(f"You have entered a number: {inp_1}")
    return


@app.cell
def _():
    inp_2 = input("Enter a number: ")
    inp_3 = input("Enter another number: ")

    print(f"Total: {inp_2 + inp_3}")
    return


@app.cell
def _():
    # Convert the "type" of user input 
    inp_4 = int(input("Enter a number: "))
    inp_5 = int(input("Enter another number: "))

    print(f"Total: {inp_4 + inp_5}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
