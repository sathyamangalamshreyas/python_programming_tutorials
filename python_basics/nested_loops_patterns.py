import marimo

__generated_with = "0.25.1"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Nested Loops
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### A nested loop is loop inside another loop. The inner loop completes all its iterations for every iteration of the outer loop.
    """)
    return


@app.cell
def _():
    # for the 1st value of 'i', all the values of j are printed
    for i in range(1, 4):
        print(f"i: {i}")
        for j in range(10, 14):
            print(f"j: {j}")
        break

    print("-" * 50)

    # For every value of 'i', the inner loop 'j' executes fully

    for i in range(1, 4):
        print(f"i: {i}")
        for j in range(10, 14):
            print(f"j: {j}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### using nested loops print the pattern:
    ```
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    1 2 3 4 5
    ```
    """)
    return


@app.cell
def _():
    # i_m denotes number of rows and j_m denotes number of columns
    for i_m in range(1, 6):
        for j_m in range(1, 6):
            print(j_m, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Print the pattern:
    ```
    1 1 1 1 1
    2 2 2 2 2
    3 3 3 3 3
    4 4 4 4 4
    5 5 5 5 5
    ```
    """)
    return


@app.cell
def _():
    # a_m == num rows in matrix, b_m == num cols in matrix
    for a_m in range(1, 6):
        for b_m in range(1, 6):
            print(a_m, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Print the pattern:
    ```
    5 5 5 5 5
    4 4 4 4 4
    3 3 3 3 3
    2 2 2 2 2
    1 1 1 1 1
    ```
    """)
    return


@app.cell
def _():
    # c_m == num rows in matrix and d_m == num_cols in martix
    for c_m in range(5, 0, -1):
        for d_m in range(5, 0, -1):
            print(c_m, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    print the pattern:
    ```
    *
    **
    ***
    ****
    *****
    ```
    """)
    return


@app.cell
def _():
    # here columns ('j') is dependent on rows ('i')
    for i_s in range(1, 6):
        for j_s in range(1, i_s+1):
            print("*", end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    print the pattern:
    ```
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    ```
    """)
    return


@app.cell
def _():
    for i_num in range(1, 6):
        for j_num in range(1, i_num+1):
            print(j_num, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    print the pattern
    ```
    1
    2 1
    3 2 1
    4 3 2 1
    5 4 3 2 1
    ```
    """)
    return


@app.cell
def _():
    for i_pat in range(1, 6):
        for j_inv in range(i_pat, 0, -1):
            print(j_inv, end= ' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    print the pattern same pattern above dynamically based on user input
    """)
    return


@app.cell
def _():
    usr_inp_dyn_mat = int(input("Enter a number: "))
    # say usr_inp_dyn_mat = 3 then the result should be:
    """
    ```
    1
    2 1
    3 2 1
    ```
    """

    for i_dyn_m in range(1, usr_inp_dyn_mat+1):
        for j_dyn_m in range(i_dyn_m, 0, -1):
            print(j_dyn_m, end= ' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Print the pattern

    ```
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    ```
    """)
    return


@app.cell
def _():
    for _i in range(5, 0, -1):
        for _j in range(1, _i+1):
            print(_j, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Print the pattern:

    ```
    5 4 3 2 1
    5 4 3 2
    5 4 3
    5 4
    5
    ```
    """)
    return


@app.cell
def _():
    # when _im = 1: _jm becomes (5, 1-1, -1) == (5, 0, -1) == 5 4 3 2 1

    # when _im = 2: _jm becomes (5, 2-1, -1) == (5, 1, -1) == 5 4 3 2

    for _im in range(1, 6):
        for _jm in range(5, _im -1, -1):
            print(_jm, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Take input from user and print the same pattern as above
    """)
    return


@app.cell
def _():
    usr_inp = int(input("Enter a number: "))

    for i_usr in range(1, usr_inp+1):
        for j_usr in range(usr_inp, i_usr-1, -1):
            print(j_usr, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print the pattern
    ```
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
    ```
    """)
    return


@app.cell
def _():
    for _ in range(5, 0, -1):
        for _j_ in range(_, 0, -1):
            print(_j_, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print the pattern
    ```
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4
    1 2 3
    1 2
    1
    ```
    """)
    return


@app.cell
def _():
    for i_tri in range(1, 6):
        for j_tri in range(1, i_tri + 1):
            print(j_tri, end=' ')
        print()
    for i_tri in range(4, 0, -1):
        for j_tri in range(1, i_tri + 1):
            print(j_tri, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print the pattern
    ```
    5
    5 4
    5 4 3
    5 4 3 2
    5 4 3 2 1
    5 4 3 2
    5 4 3
    5 4
    5
    ```
    """)
    return


@app.cell
def _():
    for i_inv_tri in range(5, 0, -1):
        for j_inv_tri in range(5, i_inv_tri-1, -1):
            print(j_inv_tri, end=' ')
        print()
    for i_inv_tri in range(2, 6):
        for j_inv_tri in range(5, i_inv_tri-1, -1):
            print(j_inv_tri, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print the pattern
    ```
            1
          1 2
        1 2 3
      1 2 3 4
    1 2 3 4 5
    ```
    """)
    return


@app.cell
def _():
    for i_at in range(1, 6):
        for j_at in range(1, 6-i_at):
            print(" ", end=' ')
        for k_at in range(1, i_at+1):
            print(k_at, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print the pattern
    ```
            5
          5 4
        5 4 3
      5 4 3 2
    5 4 3 2 1
    ```
    """)
    return


@app.cell
def _():
    for _ in range(5, 0, -1):
        for k_inv_at in range(1, _):
            print(" ", end=' ')
        for j_inv_at in range(5, _-1, -1):
            print(j_inv_at, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print the pattern
    ```
            1
          1 2 3
        1 2 3 4 5
      1 2 3 4 5 6 7
    1 2 3 4 5 6 7 8 9
      1 2 3 4 5 6 7
        1 2 3 4 5
          1 2 3
            1
    ```
    """)
    return


@app.cell
def _():
    for i_mul in range(1, 6):
        for j_mul in range(1, 5 - i_mul + 1):
            print(" ", end=' ')
        for k_mul in range(1, (i_mul*2)-1 +1):
            print(k_mul, end=' ')
        print()
    for i_mul in range(4, 0, -1):
        for j_mul in range(1, 5 - i_mul + 1):
            print(" ", end=' ')
        for k_mul in range(1, (i_mul*2)-1 +1):
            print(k_mul, end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Print the pattern
    ```
            *
          * * *
        * * * * *
      * * * * * * *
    * * * * * * * * *
      * * * * * * *
        * * * * *
          * * *
            *
    ```
    """)
    return


@app.cell
def _():
    for i_st in range(1, 6):
        for j_st in range(1, 5 - i_st + 1):
            print(" ", end=' ')
        for k_st in range(1, (i_st*2)-1 +1):
            print("*", end=' ')
        print()
    for i_st in range(4, 0, -1):
        for j_st in range(1, 5 - i_st + 1):
            print(" ", end=' ')
        for k_st in range(1, (i_st*2)-1 +1):
            print("*", end=' ')
        print()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
