import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Nested Lists
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### A nested list is a list that contains other lists as its elements

    - This structure allows Python to represent complex data such as grids, tables or matrices

    *Representing a matrix*
    - Consider a single 3x3 matrix; Each inner list represents a row in the matrix
    ```
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    ```

    **Accessing elements of a nested list**
    - To access elements of a nested list, multiple indexes are used
      - The first index specifies the inner list(row)
      - The second index specifies the element within the inner list (column)
    ```
    # Accessing Elements -> matrix[row][column]
    print(matrix[0]) # Output: [1, 2, 3] -> First Row all elements

    print(matrix[1][2]) # Output: 6 -> element at row 1 and column 2

    print(matrix[2][0]) # Output: 7 -> element at row 2 and column 0
    ```
    """)
    return


@app.cell
def _():
    # 3x3 matrix
    matrix = [
        [4, 8, 1],
        [9, 7, 2],
        [5, 6, 0],
    ]

    print(matrix)
    print(type(matrix))
    return (matrix,)


@app.cell
def _(matrix):
    print(matrix[0])
    return


@app.cell
def _(matrix):
    # Indexing maunally
    print(f"{matrix[0][0]}", end=' ')
    print(f"{matrix[0][1]}", end= ' ')
    print(f"{matrix[0][2]}", end= ' ')


    print(f"\n{matrix[1][0]}", end= ' ')
    print(f"{matrix[1][1]}", end= ' ')
    print(f"{matrix[1][2]}", end= ' ')


    print(f"\n{matrix[2][0]}", end= ' ')
    print(f"{matrix[2][1]}", end=' ')
    print(f"{matrix[2][2]}", end= ' ')
    return


@app.cell
def _(matrix):
    # Indexing using a for loop

    for i in range(0, 3):
        for j in range(0, 3):
            print(f"{matrix[i][j]}", end=' ')
        print()
    return


@app.cell
def _(matrix):
    # Add all the elements in the matrix

    total = 0
    for a in range(0, 3):
        for b in range(0, 3):
            total += matrix[a][b]

    print(total)
    return


@app.cell
def _():
    new_matrix = [
        [5, 7, 2, 3, 1],
        [6, 3, 8, 1, 3],
        [6, 4, 9, 0, 2],
        [3, 6, 3, 8, 1],
    ]

    print(f"{new_matrix}")
    print(type(new_matrix))
    return (new_matrix,)


@app.cell
def _(new_matrix):
    # Dynamic for loop
    len_rows = len(new_matrix)
    print(f"Number of rows: {len_rows}")

    len_cols = len(new_matrix[0])
    print(f"\nNumber of columns: {len_cols}")

    print()

    for r in range(0, len_rows):
        for c in range(0, len_cols):
            print(f"{new_matrix[r][c]}", end=' ')
        print()
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Questions
    - Q1: Create a 3x3 matrix and then use a nested loop to calculate and print the sum of all its elements
    - Q2: Given a 3x3 matrix print its lower triangle. Replace all elements in the upper triangle by an astrix
    - Q3: Given a 3x3 matrix print its upper triangle. Replace all elements in the lower triangle by an astrix
    - Q4: Given a 3x3 matrix print only the diagonal. Replace all other elements with an astrix
    - Q5: Given a 3x3 matrix print only the anti-diagonal. Replace all other elements with an astrix
    - Q6: Given a 4x4 matrix, print only the border elements and replace the inner elements with an astrix
    """)
    return


@app.cell
def _():
    q_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]

    print(q_matrix)
    print(f"\n{type(q_matrix)}")

    rows = len(q_matrix)
    cols = len(q_matrix[0])

    print(f"\n{rows}")
    print(f"\n{cols}")
    return cols, q_matrix, rows


@app.cell
def _(cols, q_matrix, rows):
    # Q1

    total_q = 0
    for k in range(0, rows):
        for v in range(0, cols):
            total_q += q_matrix[k][v]
        
    print(f"Sum of all elements: {total_q}")
    return


@app.cell
def _(cols, q_matrix, rows):
    # Q2
    def _():
        q2_matrix = [row.copy() for row in q_matrix]

        for r in range(0, rows):
            for c in range(0, cols):
                if r < c:
                    q2_matrix[r][c] = "*"
        for row in q2_matrix:
            print(row)

    _()
    return


@app.cell
def _(cols, q_matrix, rows):
    # Q3
    def _():
        q3_matrix = [row.copy() for row in q_matrix]

        for r in range(0, rows):
            for c in range(0, cols):
                if c < r:
                    q3_matrix[r][c] = "*"
        for row in q3_matrix:
            print(row)

    _()
    return


@app.cell
def _(cols, q_matrix, rows):
    # Q4
    def _():
        q4_matrix = [row.copy() for row in q_matrix]

        for r in range(0, rows):
            for c in range(0, cols):
                if r != c:
                    q4_matrix[r][c] = "*"
        for row in q4_matrix:
            print(row)

    _()
    return


@app.cell
def _(cols, q_matrix, rows):
    # Q5
    def _():
        q5_matrix = [row.copy() for row in q_matrix]
        length_q5 = len(q5_matrix)

        for r in range(0, rows):
            for c in range(0, cols):
                if r + c != length_q5-1:
                    q5_matrix[r][c] = "*"
        for row in q5_matrix:
            print(row)
    _()

    # ```
    # Notice what happens to the row and column indices:

    #     q_matrix[0][2] → 0 + 2 = 2

    #     q_matrix[1][1] → 1 + 1 = 2

    #     q_matrix[2][0] → 2 + 0 = 2

    # The sum is always 2, which is len(q_matrix) - 1.
    # ```
    return


@app.cell
def _():
    # Q6
    def _():
        q6_matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
        ]
    
        q6_copy = [row.copy() for row in q6_matrix]
    
        row_len = len(q6_matrix)
        col_len = len(q6_matrix[0])

        for r in range(1, row_len-1):
            for c in range(1, col_len-1):
                q6_copy[r][c] = "*"
        for row in q6_copy:
            print(row)
    _()
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
