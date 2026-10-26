import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Lambda Functions

    - A lambda function is an anonymous function written in a single line
    - Lambda functions are used to define simple functions

    ```
    # Normal function
    def square(n):
        return n**2
    ```
    ```
    # lambda function
    square = lambda n: n**2
    ```
    ```
    print(square(5)) --> 25
    ```
    """)
    return


@app.cell
def _():
    square = lambda n: n**2

    print(square(10))
    return


@app.cell
def _():
    # Using Ternary operator
    is_adult = lambda x: True if x>=18 else False

    print(is_adult(18))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Practice Questions
    - Q1: Write a lambda function that takes a number and returns its cube. Store it in a variable and call it.
    - Q2: Write a lambda function that takes a number and returns "Positive" or "Negative"
    """)
    return


@app.cell
def _():
    # Q1
    cube = lambda x: x**3
    print(cube(2))
    return


@app.cell
def _():
    # Q2
    num_1 = lambda x: "Positive" if x>0 else "Negative"

    print(num_1(-5))
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
