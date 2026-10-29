import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Dictionary
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### A dictionary in Python is an ordered collection of data values
    - It is used to store data in **key-value** pairs
      - Ex. A real dictionary which is used to loop up a word **(the key)** to find its meaning **(the value)**

    Difference between list and dictionary
    *List*
    ```
    marks = [85, 90, 70]
    print(marks[0])

    # Output
    85
    ```
    NOTE: There is no indication of what this number "85" means

    *Dictionary*
    ```
    marks = {
    "math": 85,
    "science": 90,
    "english": 70,
    }
    print(marks["math"])

    # Output
    85
    ```
    """)
    return


@app.cell
def _():
    marks = {
        "science": 99,
        "maths": 100,
        "computer_science":88,
        "can_be_list": [1, 2, 3, 4],
        (10, 12): "reading", # Tuple can be a key as they are immutable
    }

    print(marks)
    print(type(marks))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Accessing dictionary elements
    """)
    return


@app.cell
def _():
    marks_access = {
        "science": 99,
        "maths": 100,
        "computer_science":88,
        "hindi": 43,
        "history": 71,
    }

    print(marks_access["computer_science"])

    a = marks_access.get("hindi")
    print(a)

    # If the key does not exist, then the return type can be changed
    b = marks_access.get("geo", -1)
    print(b)
    return (marks_access,)


@app.cell
def _(marks_access):
    usr_inp = input("Enter a subject:")

    usr_inp_clean = usr_inp.strip().lower()

    if usr_inp_clean in marks_access.keys():
        print(f"Marks scored: {marks_access.get(usr_inp_clean)} ")
    else:
        print("Subject not found")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Manipulating dictionary
    """)
    return


@app.cell
def _():
    student = {
        "name": "Rahul",
        "age": 21,
    }
    return (student,)


@app.cell
def _(student):
    # Update
    student["age"] = 30

    print(student)
    return


@app.cell
def _(student):
    # Add new values
    student["gender"] = "male"

    print(student)
    return


@app.cell
def _(student):
    # Update method

    student.update({
        "city": "surat",
        "phone": 12344545,
    })

    print(student)
    return


@app.cell
def _(student):
    # Removing key-value pairs

    student.pop("name")

    print(student)
    return


@app.cell
def _(student):
    del student["age"]

    print(student)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Membership Operators

    - Check for existance of keys
    """)
    return


@app.cell
def _():
    new_dict = {
        "name": "Rahul",
        "age": 30,
        "gender": "Male",
        "city": "Surat",
    }

    print(new_dict)
    return (new_dict,)


@app.cell
def _(new_dict):
    print("age" in new_dict)

    print(30 in new_dict)
    return


@app.cell
def _(new_dict):
    k = input("Enter Key = ")

    if k in new_dict:
        print(new_dict[k])
    else:
        print("Key does not exist")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Dictionary methods

    **keys()**
    - Returns a view object that displays the *list of all keys*

    **values()**
    - Returns a view object that displays the *list of all values*

    **items()**
    - Returns a view object that displays a list of a dictionary's *key-value pairs as tuples*

    **update**
    - *Add or update key-value pair(s)* within a dictionary

    **get()**
    - Method to access *values* by using the corresponding *key*; Returns "None" by default if the specified *key* is not found

    **copy()**
    - Creates a *shallow* copy
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Looping through a dictionary
    """)
    return


@app.cell
def _():
    # Looping over keys (default method)
    loop_dict = {
        "name": "rahul",
        "age": 30,
        "city": "delhi",
    }


    for key in loop_dict:
        print(key)

    print()

    # Making this explict
    for key in loop_dict.keys():
        print(key)
    return (loop_dict,)


@app.cell
def _(loop_dict):
    # Looping over values
    for val in loop_dict.values():
        print(val)
    return


@app.cell
def _(loop_dict):
    # accessing keys and values
    for vals in loop_dict.keys():
        print(loop_dict[vals])
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### 8 hr and 38 mins into the video
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
