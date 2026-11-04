import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Sets
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    **A set is a collection of values where every values is unique**

    Duplicate values, if present, are ignored in a set

    Properties of sets:
    - Unordered
      - There is no concept of ordering based on index in a set
    - Unique values only
    - Mutable
      - Elements can be added or removed from a set
    - No Indexing
    - Immutable Elements
      - Lits and dicts cannot be elements of a set
    - Membership operators work in sets
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Creating sets
    """)
    return


@app.cell
def _():
    ## Create an empty set

    empty_set = set()

    print(type(empty_set))
    return


@app.cell
def _():
    fruits_set = {"apple", "mango", "banana"}

    print(fruits_set)
    return


@app.cell
def _():
    num_set = {1, 2, 3, 4, 5}

    print(num_set)
    return


@app.cell
def _():
    mixed_set = {"rahul", 34, True, 7.9}

    print(mixed_set)
    return


app._unparsable_cell(
    r"""
    # Create a set from a list (removed duplicates)

    list_set = [1, 2, 2, 3, 5, 5, 7, 8, 9, 8]

    unique_list = list(set(list_set))

    print(unique_list)f
    """,
    name="_"
)


@app.cell
def _():
    # removing duplicate words in a collection
    sentence = "python is great and python is easy"

    unique_words = set(sentence.split())

    print(len(unique_words))

    print(unique_words)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Membership operators work in sets
    """)
    return


@app.cell
def _():
    new_fruits_set = {"apple", "mango", "banana", "guava"}

    print(f"{'mango' in new_fruits_set}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Adding and Removing elements in sets
    """)
    return


@app.cell
def _():
    a_new_fruits_set = {"apple", "mango", "banana", "guava"}

    a_new_fruits_set.add("kiwi")

    print(a_new_fruits_set)
    return (a_new_fruits_set,)


@app.cell
def _(a_new_fruits_set):
    # The update method is used to add iterables to sets

    a_new_fruits_set.update(
        ["kiwi", "grapes", "lichi"]
    )
    print(a_new_fruits_set)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Remove gives an error if the element does not exist
    """)
    return


@app.cell
def _(a_new_fruits_set):
    a_new_fruits_set.remove("apple")

    print(a_new_fruits_set)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Use discard if not sure weather the element exists in the set
    """)
    return


@app.cell
def _(a_new_fruits_set):
    a_new_fruits_set.discard("apple")

    print(a_new_fruits_set)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Set Operations

    Union and Intersection
    """)
    return


@app.cell
def _():
    a = {1, 2, 3, 4, 5}

    b = {3, 4, 5, 6, 7}

    print(a | b)
    return a, b


@app.cell
def _(a, b):
    print(a & b)
    return


@app.cell
def _(a):
    print(len(a))

    print(min(a))

    print(max(a))

    print(sum(a))
    return


@app.cell
def _():
    # Sorting

    my_set = {10, 50, 35, 5, 80, 11}

    print(sorted(my_set))

    print(sorted(my_set, reverse=True))
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Looping through a set
    """)
    return


@app.cell
def _(a_new_fruits_set):
    for fruit in a_new_fruits_set:
        print(fruit)
    return


@app.cell
def _(a_new_fruits_set):
    # Using enumerate

    for i, fruit_e in enumerate(a_new_fruits_set):
        print(f"{i} : {fruit_e}")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
