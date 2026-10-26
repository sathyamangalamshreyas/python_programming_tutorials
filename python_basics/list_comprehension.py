import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### List Comprehension
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    *List comprehension offers a concise and reliable way to create new lists from existing sequences or ranges*
    - **1. Basic Usage**: For Loop vs. List Comprehension
    ```
    ## Using a For Loop ##
    squares = []
    for i in range(1, 6):
        squares.append(i * i)
    print(squares)

    # Output
    [1, 4, 9, 16, 25]

    ## Using List Comprehension ##
    squares = [i * i for i in range(1, 6)]
    print(squares)

    # Output
    [1, 4, 9, 16, 25]
    ```

    - **2. Conditional Filtering**
    ```
    evens = [i for i in range(1, 21) if i%2 == 0]
    print(evens)

    # Output
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    ```

    ```
    marks = [85, 60, 92, 45, 78, 95, 50]

    passed = [m for m in marks if m > 80]
    print(passed)

    # Output
    [85, 92, 95]
    ```

    - **3. Transforming Elements**
    ```
    names = ["rahul", "priya", "karan"]
    upper = [name.upper() for name in names]

    print(upper)

    # Output
    ["RAHUL", "PRIYA", "KARAN"]
    ```
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Using List Comprehension solve:
    - Q1: Create a list of squares of all odd numbers from 1 to 20
    - Q2: Given a list of numbers create a new list that contains numbers above 75
    """)
    return


@app.cell
def _():
    # Q1

    li_com_q1 = [(o * o) for o in range(1, 21) if o%2 != 0]

    print(li_com_q1)
    return


@app.cell
def _():
    # Q2

    nums = [100, 124, 65, 2, 50, 345, 890, 4, 0]


    li_com_q2 = [n for n in nums if n>75]

    print(li_com_q2)
    return


@app.cell
def _():
    # List of numbers divisible by both 3 and 7

    li_com_two_cond = [i for i in range(1, 101) if i%3 == 0 and i%7 ==0]

    print(li_com_two_cond)
    return


@app.cell
def _():
    # List all primes from 1 to 100
    def is_prime(num):
        factors = 0
        for p in range(1, num+1):
            if num%p == 0:
                factors += 1
        if factors == 2:
            return True
        return False


    prime_list = [p for p in range(2, 50) if is_prime(p) == True]

    print(prime_list)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
