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
def _():
    new_marks = {
        "science": 99,
        "maths": 100,
        "computer_science": 88,
        "hindi": 43,
        "history": 71,
    }
    return (new_marks,)


@app.cell
def _(new_marks):
    # print keys
    for subject in new_marks.keys():
        print(subject)
    return


@app.cell
def _(new_marks):
    # Print both keys and values along with total
    total = 0

    for subj in new_marks.keys():
        print(f"Subject = {subj} and marks = {new_marks[subj]}")
        total += new_marks[subj]

    print(f"\nTotal marks: {total}")
    return


@app.cell
def _(new_marks):
    # Print values
    for mark in new_marks.values():
        print(mark)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    **The items method**
    - Output both the keys and values of a dictionary
    """)
    return


@app.cell
def _(new_marks):
    print(new_marks.items())
    return


@app.cell
def _(new_marks):
    for detail in new_marks.items():
        subject_i = detail[0]
        marks_i = detail[1]
        print(f"Subject: {subject_i} and Marks: {marks_i}")
    return


@app.cell
def _(new_marks):
    # Unpack the tuples in the for loop
    for k_i, v_i in new_marks.items():
        print(f"Subject: {k_i} and Marks: {v_i}")
    return


@app.cell
def _(new_marks):
    # Conditional Logic

    for subj_i, mark_i in new_marks.items():
        if subj_i in ["science", "hindi", "history"] and mark_i >= 60:
            print(f"{subj_i} : Marks level 'Excellent'")
    return


@app.cell
def _(new_marks):
    for subj_k, mark_v in new_marks.items():
        if mark_v>80:
            print(f"{subj_k} level 'Excellent'")
        elif mark_v>50 and mark_v<=80:
            print(f"{subj_k} level 'Good'")
        elif mark_v>0 and mark_v<=50:
            print(f"{subj_k} level 'OK'")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Questions
    - Q1: Create a dictionary called student_profile. Include keys like name, age, city and marks (as a list of scores). Print each piece of information using its key
    - Q2: Define a dictionary with five subjects and their respective marks. Utilize the get() method to try accessing a subject that is not in the dictionary. Ensure the output prints "Not Available" as a default
    - Q3: Construct a dictionary containing four product names and their prices. Prompt the user to enter a product name. Use the "in" keyword to eheck if it exists. If yes, display its price. Otherwise inform the user that product is not found
    - Q4: Create a dictionary mapping five countries to their capitals. Iterate through the dictionary using the items() method and print each pair in the format Country -->  Capital
    - Q5: Given a dictionary of marks for different subjects, loop over its values() to calculate and print the total marks and the average mark obtained
    - Q6: Populate a dictionary with six student names and corresponding marks. Iterate through the dictionary and print all the names of students who scored greater than 80
    - Q7: Write a function named merge_dicts to merge two dictionaries. It should accept two arguments d1 and d2 and return a new dictionary d3
    """)
    return


@app.cell
def _():
    # Q1
    student_profile = {
        "name": "student_1",
        "age": 40,
        "city": "Bangalore",
        "marks": [30, 12, 20, 22, 24]
    }

    for sp in student_profile.keys():
        print(f"Attribute: {sp} and Value: {student_profile[sp]}")
    return


@app.cell
def _():
    # Q2

    five_subjects = {
        "geography": 40,
        "history": 64,
        "maths": 38,
        "physics": 47,
        "chemistry": 62
    }

    not_avail = five_subjects.get("computer_science", "Not Available")

    print(not_avail)
    return


@app.cell
def _():
    # Q3

    prod_dict = {
        "rice": 89,
        "rin": 10,
        "vim": 8,
        "ginger": 30
    }

    enter_prod_name = input("Enter a product name: ")

    clean_prod_name = enter_prod_name.strip().lower()

    if clean_prod_name in prod_dict.keys():
        print(f"Price of product {enter_prod_name} is {prod_dict[clean_prod_name]}")
    else:
        print("Product not found")
    return


@app.cell
def _():
    # Q4

    count_cap = {
        "India": "Delhi",
        "Pakistan": "Islamabad",
        "USA": "Washington DC",
        "France": "Paris",
        "Germany": "Berlin"
    }

    for country, capital in count_cap.items():
        print(f"{country} --> {capital}")
    return


@app.cell
def _():
    # Q5

    subj_marks = {
        "geography": 40,
        "history": 64,
        "maths": 38,
        "physics": 47,
        "chemistry": 62
    }

    avg_marks = 0

    total_marks = sum(subj_marks.values())

    # for marks_obt in subj_marks.values():
    #     total_marks += marks_obt

    avg_marks = total_marks/len(subj_marks)

    print(f"Total Marks: {total_marks} and Average Marks: {avg_marks}")
    return


@app.cell
def _():
    # Q6

    name_marks = {
        "name_1": 68,
        "name_2": 83,
        "name_3": 94,
        "name_4": 39,
        "name_5": 85,
        "name_6": 74
    }

    for name, score in name_marks.items():
        if score > 80:
            print(f"{name} scored {score}")
    return


@app.function
# Q7

def merge_dicts(d1, d2):
    
    d3 = {}
    d3.update(d1)
    d3.update(d2)
    
    return d3


@app.cell
def _():
    d1 = {
        "key_1": 10,
        "key_2": 20,
    }

    d2 = {
        "key_3": 30,
        "key_4": 40,
    }
    print(merge_dicts(d1, d2))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Built-in functions on Dictionaries
    """)
    return


@app.cell
def _():
    python_marks = {
        "math": 85,
        "science": 92,
        "english": 78,
        "hindi": 60,
    }

    # Use the len function for find the number of keys in the dictionary
    print(f"Length of dict: {len(python_marks)}")

    # sum of all values
    print(f"\nSum of values: {sum(python_marks.values())}")

    # min and max of values
    print(f"\nMinimun value in the dict: {min(python_marks.values())}")

    print(f"\nMaximum value in the dict: {max(python_marks.values())}")

    # min and max of keys
    print(f"\nMinimun key in the dict: {min(python_marks.keys())}")

    print(f"\nMaximum key in the dict: {max(python_marks.keys())}")

    # Sorting the dict by keys
    print(f"\nDict sorted by keys: {sorted(python_marks)}")

    # Sorting the dict using items method
    sorted_dict = dict(sorted(python_marks.items()))
    print(f"\nSorted using items method: {sorted_dict}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Nested Dictionaries
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ##### Store complex, heirarchical data
    ```
    students = {
        "101": {"name": "Rahul", "age": 21, "city": "Delhi"},
        "102": {"name": "Priya", "age": 20, "city": "Mumbai"},
        "103": {"name": "Karan", "age": 22, "city": "Pune"},
    }

    - Accessing nested values - Chain the keys:
    print(students["101"]["name"])

    # Output
    Rahul

    print(students["102"]["city"])

    #Output
    Mumbai

    - Adding a new element

    students.update({
        "104": {"name": "Sana", "age": 19, "city": "Chennai"},
        "105": {"name": "S1", "age": 43, "city": "c1"},
    })

    - Updating an element

    students["101"]["city"] = "Bangalore"

    - Looping
    for roll, info in students.items():
        print(f"Student Roll {roll}: {info['name']} from {info['city']}")

    # Output

    Student Roll 101: Rahul from Bangalore
    Student Roll 102: Priya from Mumbai
    Student Roll 103: Karan from Pune
    Student Roll 104: Sana from Chennai
    Student Roll 105: S1 from c1
    ```
    """)
    return


@app.cell
def _():
    students = {
        "101": {"name": "Rahul", "age": 21, "city": "Delhi"},
        "102": {"name": "Priya", "age": 20, "city": "Mumbai"},
        "103": {"name": "Karan", "age": 22, "city": "Pune"},
    }

    print(students["101"]["name"])
    print(students["102"]["city"])
    return (students,)


@app.cell
def _(students):
    students.update({
        "104": {"name": "n1", "age": 12, "city": "c1"},
        "105": {"name": "n2", "age": 24, "city": "c2", "details": {"phone_no": 1234567891, "gender": "female"}}
    })
    return


@app.cell
def _(students):
    print(students["105"]["details"]["phone_no"])
    return


@app.cell
def _(students):
    for k_c, v_c in students.items():
        print(f"k = {k_c} and v = {v_c}")
    return


@app.cell
def _(students):
    for roll_com, val_com in students.items():
        if roll_com == "105":
            print(f"Special: {roll_com}, phone = {val_com['details']['phone_no']}")
        else:
            print(f"Roll Number: {roll_com}, name: {val_com['name']}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Lists in Dictionaries
    """)
    return


@app.cell
def _():
    student_details = {
        "name": "Rahul",
        "age": 21,
        "subjects": ["Math", "Science", "English"],
        "marks": [85, 92, 78],
    }

    student_details
    return (student_details,)


@app.cell
def _(student_details):
    # Accessing list elemets in a dictionary
    print(student_details["subjects"])
    print()
    print(student_details["subjects"][0])
    print()
    print(student_details["subjects"][1])
    return


@app.cell
def _(student_details):
    # Update the list in the dictionary

    student_details["subjects"].append("Hindi")
    student_details["marks"].append(70)

    student_details
    return


@app.cell
def _(student_details):
    print(sum(student_details["marks"]))
    return


@app.cell
def _():
    company = {
        "engineering": ["emp_1", "emp_2", "emp_3"],
        "marketing": ["emp_4", "emp_5"],
        "hr": ["emp_6"],
    }
    company
    return (company,)


@app.cell
def _(company):
    for dept, employees in company.items():
        print(f"Dept {dept} has {employees}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Sorting using lambda functions
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    List of dictionaries
    """)
    return


@app.cell
def _():
    student_details_1 = [
        {"name": "Rahul", "marks": 85},
        {"name": "Priya", "marks": 92},
        {"name": "Karan", "marks": 78},
        {"name": "Sana", "marks": 95},
    ]
    return (student_details_1,)


@app.cell
def _(student_details_1):
    # Sort by marks

    by_marks = sorted(student_details_1, key=lambda x: x["marks"])
    print("Sorted by marks ascending")
    for x in by_marks:
        print(x)

    print()
    print()

    by_marks = sorted(student_details_1, key=lambda x: x["marks"], reverse=True)
    print("Sorted by marks descending")
    for y in by_marks:
        print(y)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Sorting a dictionary by its values
    """)
    return


@app.cell
def _():
    marks_s = {
        "math": 85,
        "science": 92,
        "english": 60,
        "hindi": 78,
    }
    return (marks_s,)


@app.cell
def _(marks_s):
    # Sort by values
    sorted_marks = sorted(marks_s.items(), key=lambda item: item[1])
    sorted_marks_dict = dict(sorted_marks)
    print("Sorted by values ascending")
    print(sorted_marks_dict)

    print()

    sorted_marks = sorted(marks_s.items(), key=lambda item: item[1], reverse=True)
    sorted_marks_dict = dict(sorted_marks)
    print("Sorted by values descending")
    print(sorted_marks_dict)
    return


@app.cell
def _(marks_s):
    # Sort by keys
    sorted_subj = sorted(marks_s.items(), key=lambda item: item[0])
    sorted_subj_dict = dict(sorted_subj)
    print("Sorted by keys ascending")
    print(sorted_subj_dict)

    print()

    sorted_subj = sorted(marks_s.items(), key=lambda item: item[0], reverse=True)
    sorted_subj_dict = dict(sorted_subj)
    print("Sorted by keys ascending")
    print(sorted_subj_dict)
    return


@app.cell
def _():
    marks_dl = {
        "aksay": [43, 12, 98, 10, 22],
        "priya": [76, 55, 34, 89, 61],
        "rahul": [20, 45, 67, 30, 88],
        "sneha": [91, 73, 50, 14, 62],
        "karan": [38, 82, 47, 95, 29],
    }
    return (marks_dl,)


@app.cell
def _(marks_dl):
    # sort based on 4th index in the list
    marks_dl_sorted = dict(sorted(marks_dl.items(), key=lambda z: z[1][-1], reverse=True))

    print(marks_dl_sorted)
    return


@app.cell
def _(marks_dl):
    # sort based on total of list
    summation = dict(sorted(marks_dl.items(), key= lambda s: sum(s[1])))
    print(f"Total from dict: {summation}")        
    return


@app.cell
def _():
    student_asc_marks = {
        "anirudh": {"math": 87, "science": 92, "english": 74},
        "priya": {"math": 65, "science": 78, "english": 90},
        "rahul": {"math": 55 , "science": 60, "english": 48},
        "sneha": {"math": 95 , "science": 88, "english": 82},
        "karan": {"math": 70 , "science": 45, "english": 63},
    }
    return (student_asc_marks,)


@app.cell
def _(student_asc_marks):
    # sort based on lowest marks in math
    low_math = dict(sorted(student_asc_marks.items(), key= lambda z: z[1]["math"]))
    print(low_math)
    return


@app.cell
def _(student_asc_marks):
    # sort descending based on total marks
    total_marks_dict = dict(sorted(student_asc_marks.items(), key= lambda m: m[1]["math"] + m[1]["science"] + m[1]["english"], reverse=True))

    print(total_marks_dict)
    return


@app.cell
def _(student_asc_marks):
    # Better method to sum total marks
    total_marks_alt = dict(sorted(student_asc_marks.items(), key= lambda q: sum(q[1].values()), reverse=True))

    print(total_marks_alt)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Dictionary Comprehension

    - general format

    '''
    {keys: values (some operation), values in dict.items() (some comdition)}
    ```

    ```
    {key: value for item in iterable}
    ```
    """)
    return


@app.cell
def _():
    marks_com = {
        "math": 85,
        "science": 92,
        "english": 60,
        "hindi": 45,
    }
    return (marks_com,)


@app.cell
def _(marks_com):
    # Keep only subkects where marks is greater than 80
    gt_80 = {sub: m for sub, m in marks_com.items() if m > 80}
    print(gt_80)
    return


@app.cell
def _(marks_com):
    # Transform aquare all marks
    sq_mks = {mks: m ** 2 for mks, m in marks_com.items()}

    print(sq_mks)
    return


@app.cell
def _():
    # Create a dictionary from two lists

    subjects_com = ["math", "science", "english"]
    scores_com = [85, 92, 78]

    result_com = {keys: values for keys, values in zip(subjects_com, scores_com)}

    print(result_com)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Using the "zip" function
    """)
    return


@app.cell
def _():
    student_zip = ["Alice", "Bob", "Charlie", "David"]

    maths = [90, 85, 70, 95]

    science = [80, 90, 75, 85]

    english = [85, 80, 90, 95]
    return english, maths, science, student_zip


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    Use zip() to iterate over all four lists simultaneously.

    Calculate the average marks for each student.

    Print the student's name and average.

    Identify the student with the highest average.

    Create a dictionary containing student names as keys and their average marks as values.

    Bonus challenge: Can you solve the entire problem using zip() and dictionary comprehension, without explicitly writing a traditional for loop?
    """)
    return


@app.cell
def _(english, maths, science, student_zip):
    for stu_nme, mat, sci, eng in zip(student_zip, maths, science, english):
        avg_mks = (mat + sci + eng) / 3
        print(f"{stu_nme} scored {avg_mks:.3f} on average")
    return


@app.cell
def _(english, maths, science, student_zip):
    student_avg_dict = {
        name_av: (mat_av + sci_av + eng_av) / 3
        for name_av, mat_av, sci_av, eng_av in zip(student_zip, maths, science, english)
    }

    print(student_avg_dict)
    return (student_avg_dict,)


@app.cell
def _(student_avg_dict):
    top_student = max(student_avg_dict, key=student_avg_dict.get)

    print(f"Top Student: {top_student}")

    print(f"Avg marks of top student: {student_avg_dict[top_student]:.2f}")
    return


@app.cell
def _():
    students_list = ["Alice", "Bob", "Charlie", "David"]

    maths_list = [90, 85, 70, 95]
    science_list = [80, 90, 75, 85]
    english_list = [85, 80, 90, 95]

    # Create dictionary of student averages
    student_avg_dict_f = {
        name: (mat + sci + eng) / 3
        for name, mat, sci, eng in zip(students_list, maths_list, science_list, english_list)
    }

    # Find the highest-scoring student
    top_student_f = max(student_avg_dict_f, key=student_avg_dict_f.get)

    # Display results
    print("Student averages:", student_avg_dict_f)
    print("Top student:", top_student_f)
    print("Highest average:", student_avg_dict_f[top_student_f])
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Questions

    - Q1: Create a dict of 6 subjects and corresponding marks. Print the subject with the highest marks and one with the lowest. Use max(), min() functions along with a lambda expression
    - Q2: Create a dict with details for 4 students. Include name, age, and city. Write a loop to print the full details of each student
    - Q3: Create a dict where each key is a student's name and the corresponding value is a list of their marks in three different subjects. Calculate and print total marks and avg marks for each student
    - Q4: Given a dict of subject and marks, sort marks by descending order and print only the top three marks
    - Q5: using dict comprehension create a new dict where keys are numbers from 1 to 10(inclusive) and values are cubes of each number
    - Q6: Given an existing dictionary of subjects and marks, use dictionary comprehension to generate a new dictionary such that only subjects where the student scored 40 or more are present
    - Q7: Create two separate lists, one containing subject names and another containing the corresponding marks. Create a ditionary using list comprehension that combines corresponding elements of both lists
    """)
    return


@app.cell
def _():
    # Q1
    dict_q1 = {
        "maths": 50,
        "physics": 48,
        "chemistry": 60,
        "biology": 59,
        "history": 62,
        "geography": 61
    }

    min_subj_tup = min(dict_q1.items(), key=lambda m: m[1])
    max_subj_tup = max(dict_q1.items(), key=lambda ma: ma[1])

    print(min_subj_tup)
    print(max_subj_tup)
    return


@app.cell
def _():
    # Q2: Create a dict with details for 4 students. Include name, age, and city. Write a loop to print the full details of each student

    return


@app.cell
def _():
    # Q3

    dict_q3 = {
        "stu_1": [94, 70, 70],
        "stu_2": [78, 92, 46],
        "stu_3": [39, 68, 57]
    }


    total_marks_q3 = {nme_q3: sum(m) for nme_q3, m in dict_q3.items()}

    avg_marks_q3 = {nme_q3: (sum(m)/len(m)) for nme_q3, m in dict_q3.items()}

    print(total_marks_q3)
    print(avg_marks_q3)
    return


@app.cell
def _():
    # Q4

    dict_q4 = {
        "maths": 50,
        "physics": 48,
        "chemistry": 60,
        "biology": 59,
        "history": 62,
        "geography": 61
    }

    top_sorted_q4 = sorted(dict_q4.items(), key= lambda x: x[1], reverse=True)[:3]

    for subject_q4, marks_q4, in top_sorted_q4:
        print(f"Subject {subject_q4} and marks {marks_q4}")
    return


@app.cell
def _():
    # Q5


    dict_q5 = {q5_key: q5_key**3 for q5_key in range(1, 11)}

    print(dict_q5)
    return


@app.cell
def _():
    # Q6

    dict_q6 = {
        "maths": 38,
        "physics": 48,
        "chemistry": 60,
        "biology": 59,
        "history": 62,
        "geography": 20
    }

    new_dict_q6 = {key_q6: val_q6 for key_q6, val_q6 in dict_q6.items() if val_q6>40}

    print(new_dict_q6)
    return


@app.cell
def _():
    # Q7: Create two separate lists, one containing subject names and another containing the corresponding marks. Create a ditionary using list comprehension that combines corresponding elements of both lists

    list_q7_sub = ["maths", "physics", "chemistry", "biology", "history", "geography"]

    list_q7_mks = [38, 48, 50, 78, 84, 79]

    combined_list_q7 = {nme_q7: mks_q7 for nme_q7, mks_q7 in zip(list_q7_sub, list_q7_mks)}

    print(combined_list_q7)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
