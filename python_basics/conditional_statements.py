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
    #### If Statement: If the condition is true, then the indented block is executed. If the condition is false, the Python interpretor simply skips it
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### If-Else Statement: One of the two blocks are always executed
    """)
    return


@app.cell
def _():
    # No output if the condition is false
    age = int(input("Enter your Age:"))

    if age>=18:
        print(f"User can vote")
    return


@app.cell
def _():
    # statements outside the if statement are executed regardless
    usr_age = int(input("Enter Your Age:"))

    if usr_age>=18:
        print(f"User can vote")

    print("Will execute regardless") # Outside the loop
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### During if-elif-else loops, Python interpreter checks each condition from top to bottom.
    - It exits where the condition is first satisfied
    - The rest of the conditions are skipped
    """)
    return


@app.cell
def _():
    # If-Elif-Else
    physics_marks = int(input("Enter Physiscs marks:"))
    chem_marks = int(input("Enter Chemistry marks:"))

    if physics_marks>=35 and chem_marks>=35:
        print(f"Passed both subjects")
    elif physics_marks>=35 and chem_marks<35:
        print(f"Passed in Physics and Failed in Chemistry")
    elif physics_marks<35 and chem_marks>=35:
        print(f"Failed in Physics and Passed in Chemistry")
    elif physics_marks<35 and chem_marks<35:
        print(f"Failed in both Physics and Chemistry")
    else:
        print(f"Invalid Input")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ##### Nested If statements

    Nesting is useful when the first condition is satisfied and a second condition is needed
    """)
    return


@app.cell
def _():
    candidate_age = int(input("Enter your age: "))

    candidate_cert = input("Enter 'Yes' if you have a certificate else enter 'No'")

    # Optional: convert string to boolean using the eval function
    bool_map = {
        'Yes': True,
        'No': False,
        'yes': True,
        'no': False
    }

    bool_value = bool_map.get(candidate_cert.strip().lower(), False)

    if candidate_age>=18:
        if bool_value == True:
            print(f"Potential Candidate")
        else:
            print(f"No Certificate")
    else:
        print(f"Cannot hire, underage")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### Ternary Operator
    If-Else statement in a single line
    """)
    return


@app.cell
def _():
    # Regular If-Else
    age_status = int(input("Enter your age:"))

    if age_status>=18:
        print(f"Adult")
    else:
        print(f"Minor")
    return


@app.cell
def _():
    # Ternary Operator
    tern_status = int(input("Enter your age"))

    tern_status_print = "Adult" if tern_status>=18 else "Minor"

    print(f"Status is: {tern_status_print}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Practice Questions

    Q1: Take a number as input. Print whether the number is positive, negative or zero

    Q2: Take two numbers as input. Print the greater of the two. If they are equal, print "Both are equal"

    Q3: Take a students marks as input. Print their grade based on this scale:
    - 90 and above --> A
    - 75 to 89 --> B
    - 60 to 74 --> C
    - 40 to 59 --> D
    - Below 40 --> F

    Q4: Take a year as input. Check if it is a leap year. A year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
    """)
    return


@app.cell
def _():
    # Q1
    num_1 = float(input("Input any number"))

    if num_1>0:
        print(f"Sign is positive")
    elif num_1<0:
        print("Sign is Negative")
    elif num_1==0:
        print(f"Equal to Zero")
    return


@app.cell
def _():
    # Q2
    num_q2_1 = float(input("Enter first number:"))
    num_q2_2 = float(input("Enter second number:"))

    if num_q2_1>num_q2_2:
        print(f"The greater number is: {num_q2_1}")
    elif num_q2_1==num_q2_2:
        print(f"Both numbers are equal")
    else:
        print(f"The greater number is: {num_q2_2}")
    return


@app.cell
def _():
    # Q3
    stu_marks = float(input("Enter your marks:"))

    if stu_marks>89:
        print("Grade A")
    elif stu_marks>=75 and stu_marks<=89:
        print("Grade B")
    elif stu_marks>=60 and stu_marks<=74:
        print("Grade C")
    elif stu_marks>=40 and stu_marks<=59:
        print("Grade D")
    elif stu_marks>=0 and stu_marks<40:
        print("Grade F")
    else:
        print("Invalid Input")
    return


@app.cell
def _():
    #Q4
    inp_year = int(input("Enter a year:"))

    if inp_year % 4 == 0:
        print(f"Year {inp_year} is a leap year")
    elif inp_year % 100 == 0:
        print(f"Year {inp_year} is not a leap year")
    elif inp_year % 400 == 0:
        print(f"Year {inp_year} is a leap year")
    else:
        print(f"Year {inp_year} is not a leap year")
    return


@app.cell
def _():
    # Q4 alternate verion
    inp_year_alt = int(input("Enter Year:"))

    if (inp_year_alt % 4 == 0 and inp_year_alt % 100 !=0) or (inp_year_alt % 400 == 0):
        print(f"Year {inp_year_alt} is a leap year")
    else:
        print(f"Year {inp_year_alt} is not a leap year")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
