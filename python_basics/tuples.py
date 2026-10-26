import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Tuples
    7 hr and 57 mins into the video
    """)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
