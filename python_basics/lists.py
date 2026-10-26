import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo
    import math


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Lists
    ##### Lists are a DataType in Python like int, float, str
    **Properties of Lists**
    - *Ordered*: Items in a list stay in the same order in which they are created unless changed
    - *Mutable*: Items can be changed, added and removed after a list is created
    - *Allows Duplicates*: The same value can appear multiple times; List DataType does not enforce uniqueness
    - *Multiple DataTypes*: A single list can contain multiple DataTypes
    - Each value stored within a list is referred to as **element** or **item**
    """)
    return


@app.cell
def _():
    x = ["name_1", "name_2", "name_3", 10, True, 5.5]
    print(x)
    print()
    print(type(x))
    return


@app.cell
def _():
    # Duplicate list elements by using the multiplication operator
    marks = [10, 10, 10]

    # Duplicate marks twice
    print(marks*2)
    # repeats the list items 2 times
    return


@app.cell
def _():
    # Combine two lists using the the addition operator
    list_1 = [1, 1, 1]
    list_2 = [2, 2, 2]

    print(list_1 + list_2)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Build-in functions for lists
    - lenght: len
    - minimum: min
    - maximum: max
    - summation: sum
    - sorting elements: sorted (Note: Sorts in ascending order by default and returns a new list)
    """)
    return


@app.cell
def _():
    list_3 = [45, 78, 21, 89, 100, 5, 34]

    # Length of list_2
    list_3_len = len(list_3)
    print(f"Length: {list_3_len}")

    print()

    # Maximum element
    list_3_max = max(list_3)
    print(f"Maximum: {list_3_max}")

    print()

    # Minimum element
    list_3_min = min(list_3)
    print(f"Minimum: {list_3_min}")

    print()

    # Summation
    list_3_sum = sum(list_3)
    print(f"Sum: {list_3_sum}")

    print()

    # Sort
    list_3_sort = sorted(list_3)
    print(f"Sorted List: {list_3_sort}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### List Indexing: Accessing List Elements

    - **Positive Indexing**:
        - Use positive indexes to access elements from the beginning of the list, moving towards the right.
        - **The first element is always at index 0**
    ```
    fruits = ["apple", "mango", "banana", "grapes", "orange"]
               **0**    **1**     **2**     **3**     **4**

    print(fruits[0]) # Output: apple
    print(fruits[1]) # Output: mango
    print(fruits[4]) # Output: orange
    ```

    - **Negative Indexing**:
        - Negative indexes allow us to access elements from the end of the list, moving towards to the left
        - **The last element is always at index -1**
    ```
    fruits = ["apple", "mango", "banana", "grapes", "orange"]
               **-5**   **-4**   **-3**    **-2**    **-1**

    print(fruits[-1]) # Output: orange
    print(fruits[-2]) # Output: grapes
    print(fruits[-4]) # Output: mango
    ```

    **Updating elements using Index**
    - You can modify a list element by assigning a new value to its specific index
    - This modifies the element at that position
    ```
    fruits = ["apple", "mango", "banana", "grapes", "orange"]

    fruits[1] = "kiwi" # Replaces "mango" with "kiwi"

    print(fruits) # Output ["apple", "kiwi", "banana", "grapes", "orange"]
    ```
    """)
    return


@app.cell
def _():
    list_ind = ["name_1", "name_2", 10, 50.5, 100, "city"]

    print(list_ind[0])
    print(f"\n{list_ind[1]}")
    print(f"\n{list_ind[5]}")

    print(f"\nNegative_index: {list_ind[-2]}")

    # Use list length to find last element in the list
    # The last element will be "length - 1"
    len_list_ind = len(list_ind)

    print(f"\nLength based index: {list_ind[len_list_ind -1]}")
    return


@app.cell
def _():
    # Update based on index
    list_update = [1, 10, 100]
    print(f"Original List: {list_update}")

    list_update[0] = 20
    print(f"\nUpdated list: {list_update}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Practice Questions
    - Q1: Create a list of numbers. Print the first, last and middle number(s) from the list
          - Use both positive and negative indexing where appropriate
    - Q2: Create a list of 5 numbers. Replace the second and fourth elements of this list with the number 0 using indexing
    """)
    return


@app.cell
def _():
    #Q1
    list_num_1 = [1, 2, 5, 10, 20, 55]

    print(f"First Number: {list_num_1[0]}")
    print(f"\nLast Number: {list_num_1[-1]}")

    list_num_1_len = len(list_num_1)

    odd_list = int(list_num_1_len//2) # for odd number of elements in the list

    # even number of elements in the list
    even_list_1 = int((list_num_1_len//2 - 1))
    even_list_2 = int((list_num_1_len//2))

    if list_num_1_len%2 == 0:
        print(f"\nMiddle numbers: {list_num_1[even_list_1]} and {list_num_1[even_list_2]}")
    else:
        print(f"\nMiddle Number: {int(list_num_1[odd_list])}")
    return


@app.cell
def _():
    # Q2
    list_5 = [10, 20, 25, 50, 5]

    print(f"Original List: {list_5}")

    list_5[1] = 0
    list_5[-2] = 0

    print(f"\nModified List: {list_5}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Slicing Python Lists

    - Slicing allows us to extract a specific portions or "slice" from a list
    - Slicing does not modify the original list; It returns a new list containing the selected elements
    - Useful for working with subsets of data

    #### Slicing Syntax

    **list_name[start:stop:step]**

    - *start index*: The index where the slice begins(inclusive)
           - If omitted, the start index defaults to 0 (i.e. the beginning of the list)
    - *stop index*: The index where the slice ends (exclusive)
          - The element at this position will **not** be included in the slice
          - If omitted, the stop index defaults to the end of the list
    - *step value*: Determines how many positions to jump between elements
          - If omitted, the step value defaults to 1
          - A negative step value reverses the order
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Examples of List Slicing

    ```
    nums = [10, 20, 30, 40, 50, 60, 70, 80]

    print(nums[1:5])
    - Output: [20, 30, 40, 50]
    - Elements from index 1 up to, but not including index 5

    print(nums[:4])
    - Output: [10, 20, 30, 40]
    - Starts at the beginning of the list and ends at index 4 (exclusive)

    print(nums[4:])
    - Output: [50, 60, 70, 80]
    - Starts from index 4 and goes till the end of the list

    print(nums[::2])
    - Output: [10, 30, 50, 70]
    - Starts at index 0, and goes till the end with a step size of 2

    print(nums[1:7:2])
    - Output: [20, 40, 60]
    - Starts at index 1, goes till index 7 (not inclusive) with a step size of 2

    print(nums[::-1])
    - Output: [80, 70, 60, 50, 40, 30, 20, 10]
    - Starts at the last index and ends at the first index
    - This effectively reverses the list
    ```
    """)
    return


@app.cell
def _():
    list_slice = [56, 39, 21, 99, 53, 18]

    ls_1 = list_slice[0:4]
    print(ls_1)

    ls_2 = list_slice[2:5]
    print(ls_2)

    ls_3 = list_slice[2:]
    print(ls_3)

    ls_4 = list_slice[:3]
    print(ls_4)

    ls_5 = list_slice[::-1]
    print(ls_5)

    ls_6 = list_slice[5:2:-1]
    print(ls_6)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Looping / Iterating through lists

    Iterating through a list allows us to perform operations on each list element

    * Using a **For** Loop*
      - Manages the list index automatically

    ```
    fruits = ["apple", "mango", "banana"]

    for element in fruits:
        print(element)

    Output:
    apple
    mango
    banana
    ```
    * Using a **While** Loop*
        - Need to manage the list index manually

    ```
    fruits = ["apple", "mango", "banana"]

    i = 0

    while i < len(fruits)
        print(fruits[i])
        i+=1

    Output:
    apple
    mango
    banana
    ```

    * Using **Enumerate** Operator*

    - Enumerate allows us to acess both the index and elements of a list while iterating through the list
    - Enumerate works by adding a counter to an iterable and returns it as an enumerate object
          - This object can then be used directly inside *for loops*

    ```
    fruits = ["apple", "mango", "banana"]

    for index, element in enumerate(fruits):
        print(f"{index}: {element}")

    Output:
    0: apple
    1: mango
    2: banana
    ```
    - Enumerate can also use a custom start index
    - In the example below, the index starts at 10

    ```
    fruits = ["apple", "mango", "banana"]

    for index, element in enumerate(fruits, start=10):
        print(f"{index}: {fruit}")

    Output:
    10: apple
    11: mango
    12: banana
    ```
    """)
    return


@app.cell
def _():
    nums = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    j = 0

    while j<len(nums):
        print(f"Element {nums[j]} is at index {j}")
        j+=1
    return


@app.cell
def _():
    # Count all the odd numbers in the list
    nums_odd = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    k = 0
    count = 0

    while k<len(nums_odd):
        if nums_odd[k]%2 !=0:
            print(f"Element {nums_odd[k]} is odd")
            count+=1
        k+=1

    print(f"\nTotal count of odd numbers: {count}")
    return


@app.cell
def _():
    # Reverse list iteratively using negative step
    rev_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    n = len(rev_list)

    a = (n-1)

    while a>=0:
        print(rev_list[a], end=' ')
        a-=1
    return


@app.cell
def _():
    # Use for loop to iterate through the list
    for_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    for b in range(len(for_list)):
        print(for_list[b], end=' ')
    return


@app.cell
def _():
    # Find the total of all elements in the list using a for loop
    sum_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    test=0

    for c in range(len(sum_list)):
        test += sum_list[c]
    print(test)
    return


@app.cell
def _():
    # Find the total directly without accessing the element via
    # its index

    sum_list_1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    total = 0

    for num in sum_list_1:
        total+=num
    print(total)
    return


@app.cell
def _():
    # Use enumerate to print both index and value of the list

    enum_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    for index, value in enumerate(enum_list):
        print(f"Index: {index} and Value: {value}")
    return


@app.cell
def _():
    # Print the index of all the even numbers

    even_enum = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    for i, v in enumerate(even_enum):
        if v%2 == 0:
            print(f"Index {i} of even number {v}")
        else:
            continue
    print("done!")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Practice Questions

    - Q1: Find the largest element in a list without using the in-built max function
    - Q2: Check for target existence: Accept a number as input as check for it's existence in a list without using the in-built "in" operator
    - Q3: Calculate the average of all elements in list. Use len but do not use the max operator
    - Q4: Element-wise sum of lists: Given two lists of the same length, write a function that loops through the lists and calculates the sum of corresponding elements and prints a new list
    - Q5: Check is a list is sorted in ascending order: Print True if it is sorted in ascending order
    """)
    return


@app.cell
def _():
    # Q1
    list_q1 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    is_max = -math.inf

    for v_max in list_q1:
        if v_max>is_max:
            is_max=v_max

    print(is_max)
    return


@app.cell
def _():
    # Q2
    list_q2 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    usr_input = int(input("Enter a number:"))

    match = 0

    for i_q2 in range(0, len(list_q2)-1):
        if usr_input==list_q2[i_q2]:
            match += 1
            print(f"{usr_input} is present in the list at positon {i_q2}")
    else:
        print(f"The input {usr_input} is not in the list")
    return


@app.cell
def _():
    # Q3
    list_q3 = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

    len_q3 = len(list_q3)

    avg = 0
    summ = 0

    for ind_q3, val_q3 in enumerate(list_q3):
        summ += val_q3
        avg = summ/len_q3

    print(avg)
    return


@app.cell
def _():
    # Q4
    list_q4_1 = [1, 2, 3, 4, 5]

    list_q4_2 = [1, 2, 3, 4, 5]

    new_list = []

    for i_q4 in range(len(list_q4_1)):
        new_list.append(list_q4_1[i_q4] + list_q4_2[i_q4])
    print(new_list)
    return


@app.cell
def _():
    # Q5
    list_asc_1 = [7, 0]

    boolean_val = True

    for i_asc in range(0, len(list_asc_1)-1):
        if list_asc_1[i_asc] > list_asc_1[i_asc + 1]:
            boolean_val = False
    print(f"Is the list sorted in ascending order: {boolean_val}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### List Methods
    -*List Methods* are Python's built-in functions that operate directly on a list, allowing us to modify the lists
    - Unlike built-in *functions* like sorted() which return a new list, methods change the original list

    *List Methods*
    - **.append()**
    - Add elements to the end of the list
    ```
    fruits = ["apple", "mango"]
    fruits.append("banana")

    print(fruits)
    # Output:
    ["apple", "mango", "banana"]
    ```
    - **.remove()**
    - Removes the first occurance of the specified value from the list
    - If the element is not found, it raises a *ValueError*
    ```
    fruits = ["apple", "kiwi", "mango", "banana"]
    fruits.remove["mango"]

    print(fruits)
    # Output:
    ["apple", "kiwi", "banana"]
    ```

    - **.insert()**
    - Inserts an element at a specified index
    - The first argument is the index, the second is the value
    ```
    fruits = ["apple", mango", "banana"]
    fruits.insert(1, "kiwi")

    print(fruits)
    # Output:
    ["apple", "kiwi", "mango", "banana"]
    ```

    - **.pop()**
    - Removes and returns the element at a given index
    - If the index is not specified, it removes and returns the last element
    ```
    fruits = ["apple", "kiwi", "banana"]
    popped_list = fruits.pop()

    print(f"Popped: {popped_list} & list: {fruits}")
    # Output
    Popped: banana & list: ['apple', 'kiwi']

    popped_first = fruits.pop(0)
    print(f"Popped: {popped_first} & list: {fruits}")
    # Output
    Popped: apple & list: ['kiwi']
    ```
    """)
    return


@app.cell
def _():
    mix_lst = ["name_1", 20, 34.5, 90, True, "city"]

    print(mix_lst)
    print()

    mix_lst.append(100)
    print(mix_lst)

    print()

    mix_lst.insert(2, "ocean")
    print(mix_lst)

    print()

    x_pop = mix_lst.pop()
    print(x_pop)
    print(mix_lst)

    print()
    mix_lst.remove("ocean")
    print(mix_lst)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### List Methods:

    **Sorting and Reversing Elements**
    - **.sort()** - Sort in place
    - Sorts the elements of the list (default is ascending order), modifying the list
    - specifying *reverse=True* sorts in descending order
    ```
    nums = [40, 30, 50, 20, 10]
    num.sort()

    print(nums)
    #Output
    [10, 20, 30, 40, 50]
    ```
    ```
    nums_lst = [40, 30, 50, 20, 10]
    nums_lst.sort(reverse=True)

    print(nums_lst)
    # Output
    [50, 40, 30, 20, 10]
    ```

    - **Sorting and Counting Elements**
    - **.index()** - Find Element Index
    - Returns the index of the first occurance of the specified value
    ```
    fruits = ["apple", "mango", "banana", "mango"]
    print(fruits.index('mango'))

    # Output
    1
    ```
    - **.count()** - Count Element Occurances
    - Returns the number of times a specified value appears in the list
    ```
    fruits = ["apple", "mango", "banana", "mango"]
    print(fruits.count('mango'))

    # Output
    2
    ```

    - **.reverse()** - Reverse a list
    ```
    fruits = ["apple", "mango", "banana"]
    print(fruits.reverse())

    # Output
    ['banana', 'mango', 'apple']
    ```

    - **.copy()** - Create a shallow copy
    - Returns a new list that is a shallow copy of the orginal

    ```
    original_list = [10, 20, 30]
    new_list = original_list.copy()

    new_list.append(40)
    print(new_list)

    # Output
    [10, 20, 30, 40]

    print(original_list)
    [10, 20, 30]
    ```

    - **clear()** - Removes all elements
    - Removes all elements from a list, effectively making it an empty list
    - Modifies the list in-place

    ```
    nums = [10, 20, 15, 30, 40]
    print(nums)

    # Output
    [10, 20, 15, 30, 40]

    nums.clear()
    print(nums)

    # Output
    []
    ```
    """)
    return


@app.cell
def _():
    nums_list = [1, 2, 2, 10, 4]

    print(f"orig list: {nums_list}")
    nums_list.sort()
    print(f"\nSorted List in ascending order: {nums_list}")

    nums_list.sort(reverse=True)
    print(f"\nSorted list in descending order: {nums_list}")

    _ = nums_list.count(2)
    print(f"\nNumber of occurances of value '2': {_}")
    return


@app.cell
def _():
    nums_index = [10, 20, 15, 30, 40]

    _ = nums_index.index(30)

    print(f"Index of element '30': {_}")

    new_nums = nums_index.copy()
    new_nums.append(70)

    print(new_nums)
    print(nums_index)
    return


@app.cell
def _():
    nums_clear = [10, 20, 15, 30, 40]

    print(nums_clear)

    nums_clear.clear()
    print(nums_clear)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Membership Operators

    - Used to test if a sequence (like a list) contains a specified element
    - Returns a boolean value based on the result
    - Useful for conditional logic

    - **in** operator
    - Returns true if the specified value is found within the list
    - False if not found

    ```
    fruits = ["apple", "banana", "cherry"]
    print("banana" in fruits)

    # Output
    True

    print("grapes" in fruits)
    False
    ```

    - **not in** operator
    - Returns True if the specified value is NOT found within the list and False if it is found

    ```
    fruits = ["apple", "banana", "cherry"]
    print("grapes" not in fruits)

    # Output
    True

    print("banana" not in fruits)
    False
    ```
    """)
    return


@app.cell
def _():
    fruits = ["apple", "banana", "cherry"]
    print("apple" not in fruits)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Questions
    - Q1: Find the largest and smallest number in a list without using built-in functions like max() or min()
    - Q2: Reverse a list without using the .reverse() method or slicing the list using [::-1]
    - Q3: Given two lists merge them into a single new list without modifying the originals
      - Use the "+" operator to combine lists
    - Q4: Given a list, remove all duplicate elements while preserving the original order of the unique items
    - Q5: Seperate a list of integers into two distinct lists: One containing all the even numbers and the other containing all the odd numbers
    - Q6: Create a list containing the square of numbers from 1 to 10
    - Q7: Given a list of numbers (which may contain duplicates), write a Python script that takes an integer as input from the user and removes all occurances of that integer from the list
    - Q8: Iterate through a list of integers and replace every negative number found in that list with the value 0
    """)
    return


@app.cell
def _():
    # Q1
    q1_list = [1, 2, 3, 4, -1, 10, 30, 50, 50, 20, 2, 4, -7]

    iter_q1 = -math.inf
    for lar in q1_list:
        if lar>iter_q1:
            iter_q1=lar
    print(iter_q1)

    iter_2_q1 = math.inf
    for sml in q1_list:
        if sml<iter_q1:
            iter_2_q1=sml
    print(iter_2_q1)
    return


@app.cell
def _():
    # Q2
    q2_list = [1, 2, 3, 4, -1, 10, 30, 50, 50, 20, 2, 4, -7]

    nn = len(q2_list)

    rev_list_q2 = []

    for ind in range(nn-1, -1, -1):
        rev_list_q2.append(q2_list[ind])

    print(rev_list_q2)
    return


@app.cell
def _():
    # Q3
    q3_list_1 = [1, 2, 3, 4, 5]
    q3_list_2 = [6, 7, 8, 9, 10]

    combined_list_q3 = q3_list_1 + q3_list_2

    print(combined_list_q3)
    return


@app.cell
def _():
    # Q4
    q4_list = [10, 10, 10, 10, 20]

    q4_len = len(q4_list)

    test_list = q4_list.copy()

    for i_q4_d in range(0, q4_len-1):
        if q4_list[i_q4_d] == q4_list[i_q4_d + 1]:
            test_list.remove(q4_list[i_q4_d])
    print(test_list)

    ## Alternate logic

    q4_new_list = []
    for num_q4 in q4_list:
        if num_q4 not in q4_new_list:
            q4_new_list.append(num_q4)
    print(q4_new_list)
    return


@app.cell
def _():
    # Q5
    q5_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    q5_even = []
    q5_odd = []

    for ind_q5, val_q5 in enumerate(q5_list):
        if val_q5%2 == 0:
            q5_even.append(val_q5)
        else:
            q5_odd.append(val_q5)

    print(q5_even)
    print(q5_odd)
    return


@app.cell
def _():
    # Q6

    q6_list = []

    for i_q6 in range(1, 11):
        q6_list.append(i_q6**2)

    print(q6_list)
    return


@app.cell
def _():
    # Q7
    q7_list = [1, 2, 3, 4, -1, 10, 30, 50, 50, 50, 20, 2, 4, -7]

    q7_usr_inp = int(input("Enter a number: "))

    q7_usr_inp_copy = q7_usr_inp

    q7_len = len(q7_list)

    q7_new_list = []

    for i_q7 in range(0, q7_len):
        if q7_usr_inp_copy != q7_list[i_q7]:
            q7_new_list.append(q7_list[i_q7])

    print(q7_new_list)
    return


@app.cell
def _():
    #Q8

    q8_list = [1, 2, 3, 4, -1, 10, 30, 50, 50, 50, 20, 2, 4, -7]

    len_q8 = len(q8_list)

    for i_q8 in range(0, len_q8):
        if q8_list[i_q8]<0:
            q8_list[i_q8] = 0

    print(q8_list)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
