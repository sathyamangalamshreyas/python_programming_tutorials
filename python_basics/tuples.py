import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ## Tuples
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    **Tuples** are collection of elements where the collection is immutable.
    - Once created, tuple elements cannot be modified, added or removed
    ```
    cities_tuple = ("city_1", "city_2", "city_3")
    print(cities_tuple)
    # Output
    ('city_1', 'city_2', 'city_3')

    print(type(cities_tuple))
    # Output
    <class 'tuple'>
    ```
    **Key Properties of tuples**
    - Ordered: Elements stay in the order that they were created
    - Immutable: Cannot be modified after creation
    - Allows duplicates: Same element can appear multiple times
    - Can hold multiple data types: int, float, str, bool data types are supported
    """)
    return


@app.cell
def _():
    tup_1 = (1, 2, 3, "name_1", True)

    print(tup_1)
    print(type(tup_1))
    return (tup_1,)


@app.cell
def _(tup_1):
    print(tup_1[0:2])
    return


@app.cell
def _(tup_1):
    print(tup_1[::-1])
    return


@app.cell
def _(tup_1):
    n = len(tup_1)

    for i in range(0, n):
        print(tup_1[i], end=' ')
    return


@app.cell
def _(tup_1):
    for ele in tup_1:
        print(ele, end=' ')
    return


@app.cell
def _(tup_1):
    for ind, val in enumerate(tup_1):
        print(ind, val)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### NOTE
    - Sorting a tuple using the sorted() function outputs a list
    """)
    return


@app.cell
def _():
    tup_2 = (12, 10, 34, 11, 20)

    result = sorted(tup_2)

    print(result)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Packing and unpacking

    - Packing and unpacking are python features that allow users to:
      - assign multiple values to a single variable **(packing)**
      - or extract multiple values from a tuple into separate variables **(unpacking)**
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    **Packing**: Grouping values into a tuple
    - Packing occurs when multiple values are assigned to a single variable without explictly using parentheses
    - Python groups these values into a tuple
    """)
    return


@app.cell
def _():
    # Packing
    pack_1 = "name_1", "21", "city_1"

    print(pack_1)
    print(type(pack_1))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    **Unpacking**: Extracting values from a tuple
    - Unpacking of elements happens happens when elements of a tuple are assigned to a individual variables
    - The number of variables on the left side of the assignment must exactly match the number of elements in the tuple
    """)
    return


@app.cell
def _():
    # Unpacking
    unpack_1 = ("name_2", 22, "city_2")

    name, num, loc = unpack_1
    print(name)
    print(type(name))
    print(num)
    print(type(num))
    print(loc)
    print(type(loc))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### To store a single element as a tuple, use a comma at the end
    ```
    single_tuple = 1,

    print(single_tuple)

    #Output
    (1,)

    print(type(single_tuple))
    <class 'tuple'>
    ```
    """)
    return


@app.cell
def _():
    single_tuple = 1,
    print(single_tuple)
    print(type(single_tuple))
    return


@app.cell
def _():
    # Function returns a tuple
    def min_max(list) -> tuple:
        min_ele = min(list)
        max_ele = max(list)

        return min_ele, max_ele

    result_min_max = min_max([1, 2, 3, 4, 5])

    print(result_min_max, type(result_min_max))
    return


@app.cell
def _():
    # Unpack the result:

    def min_max_un(list) -> tuple:
        min_ele = min(list)
        max_ele = max(list)

        return min_ele, max_ele

    result_min_max_un = min_max_un([1, 2, 3, 4, 5])

    print(result_min_max_un)

    # Unpack the results
    fir_ele, sec_ele = result_min_max_un

    print(fir_ele, type(fir_ele), sec_ele, type(sec_ele))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Questions:
    - Q1: Create a tuple of 5 songs. Print the first, last and middle songs using indexing
    - Q2: Create a tuple of 8 numbers. Using slicing, print the first 3, last 3 and every alternate element
    - Q3: Create a tuple of 6 numbers, print the highest, lowest and average
    - Q4: Take 5 numbers as input from the user, store them in a tuple, and print the tuple along with its minimum and maximum elements
    - Q5: Write a function get_stats(nums) that takes a tuple of numbers and returns a tuple containing the sum, average, minimum and maximum elements. Unpack the returned tuple and print each value.
    """)
    return


@app.cell
def _():
    # Q1
    song_tup = "song_1", "song_2", "song_3", "song_4", "song_5", "song_6"

    n_song_tup = len(song_tup)

    middle_song = n_song_tup//2

    if n_song_tup%2 !=0:
        print(f"First Song: {song_tup[0]}")
        print(f"Middle Song: {song_tup[middle_song + 1]}")
        print(f"Last Song: {song_tup[-1]}")
    elif n_song_tup%2 ==0:
        print(f"First Song: {song_tup[0]}")
        print(f"Middle Songs: {song_tup[middle_song-1], song_tup[middle_song]}")
        print(f"Last Song: {song_tup[-1]}")
    return


@app.cell
def _():
    # Q2
    tup_8 = [1, 2, 3, 4, 5, 6, 7, 8]

    first_3 = tup_8[0:3]
    print(first_3)

    last_3 = tup_8[-1:-4:-1]
    print(last_3)

    alt_ele = tup_8[::2]
    print(alt_ele)
    return


@app.cell
def _():
    # Q3

    tup_6 = 1, 2, 3, 4, 5, 6

    tup_6_max = max(tup_6)
    print(tup_6_max)

    tup_6_min = min(tup_6)
    print(tup_6_min)

    tup_6_avg = sum(tup_6)/len(tup_6)
    print(tup_6_avg)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### 8 hr and 14 mins into the video
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
