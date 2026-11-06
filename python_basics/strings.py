import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")

with app.setup:
    import marimo as mo


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Strings and String Operations

    - Strings are iterable
    - Strings are immutable
    - Indexing in strings works the same as in lists
    - To modify strings, construct a new string and assign operations
    """)
    return


@app.cell
def _():
    name = "Rahul"

    print(name[0:2])

    print(name[0])

    print(len(name))

    print(name[-1])
    return (name,)


@app.cell
def _(name):
    new_name = "K" + name[1:]

    print(new_name)
    return


@app.cell
def _():
    # Concatenation

    greeting = "Hello"

    greeting = greeting + "," + " World!"

    print(greeting)
    return


@app.cell
def _():
    # Slicing

    text = "Programming"

    print(text[0:4])

    print(text[4:10])

    print(text[10:5:-1])

    print(text[::-1])
    return


@app.cell
def _():
    # Repeat strings

    symbol = "="

    print(symbol * 30)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Looping in strings
    """)
    return


@app.cell
def _():
    new_text = "Python Programming"

    n = len(new_text)


    for i in range(0, n):
        print(new_text[i])
    return n, new_text


@app.cell
def _(n, new_text):
    # Count the number of "o" chars

    total = 0

    for j in range(0, n):
        if new_text[j] == "o" or new_text[j] == "O":
            total+=1

    print(total)
    return


@app.cell
def _():
    # Use while loop

    name_p = "Python Programming"

    new_total = 0
    ch = 0

    while ch < len(name_p):
        if name_p[ch] == "o" or name_p[ch] == "O":
            new_total+=1
        ch+=1
    print(f"Total number of 'O': {new_total}")
    return


@app.cell
def _(new_text):
    # Use enumerate

    for ind, char in enumerate(new_text, start=0):
        print(f"index: {ind} and char: {char}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Membership Operators
    """)
    return


@app.cell
def _(new_text):
    print("p" in new_text)
    return


@app.cell
def _(new_text):
    print("P" in new_text)
    return


@app.cell
def _(new_text):
    print("Z" not in new_text)
    return


@app.cell
def _(new_text):
    print("gram" in new_text)
    return


@app.cell
def _():
    test_str = "progrAmming"

    vowels = "aeiouAEIOU"

    tot_v = 0

    for cha_v in test_str:
        if cha_v in vowels:
            tot_v+=1
    print(tot_v)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Built-in functions in Strings

    - len()
    - min() - Alphabetical sort and return the first char
    - max() - Alphabetical sort and return the last char
    - sorted() - Sort the iterable in ascending order
    """)
    return


@app.cell
def _():
    uni_str = "Shreyaszxde0"

    print(f"Minimum: {min(uni_str)} and unicode value: {ord(min(uni_str))}")

    print(f"\nMinimum: {max(uni_str)} and unicode value: {ord(max(uni_str))}")

    print(f"\nSorted text: {sorted(uni_str)}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Questions

    - Q1: Input name and print first char, last char and the total length of the name
    - Q2: Accept a string as input, print the reverse using string slicing
    - Q3: Input a sentence, count and print the total number of vowels and present it using a for loop
    - Q4: Given a string input print every alternate char from the first char using sting slicing
    """)
    return


@app.cell
def _():
    # Q1

    usr_name = input("Enter your name: ")

    print(f"First char: {usr_name[0]}")
    print(f"\nLast char: {usr_name[-1]}")
    print(f"\nTotal Length: {len(usr_name)}")
    return


@app.cell
def _():
    # Q2

    string_q2 = input("Enter a string: ")

    reverse_str = string_q2[::-1]

    print(f"Reversed String: {reverse_str}")
    return


@app.cell
def _():
    # Q3

    sent_q3 = input("Enter a sentence: ")

    total_v = 0

    for char_v in sent_q3:
        if char_v in "aeiouAEIOU":
            total_v+=1

    print(f"Total number of vowels: {total_v}")
    return


@app.cell
def _():
    # Q4 Given a string input print every alternate char from the first char using sting slicing

    str_q4 = input("Enter a string: ")

    alt_ch = str_q4[0::2]

    print(f"Alternate char in string: {alt_ch}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### String Methods
    """)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    **Case Conversion**
    """)
    return


@app.cell
def _():
    text_str = "Hello, World! from Python"

    print(f"Lowercase: {text_str.lower()}")

    print(f"\nUppercase: {text_str.upper()}")

    print(f"\nCapitalize: {text_str.capitalize()}")

    print(f"\nSwapcase: {text_str.swapcase()}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    **Checking Content**
    """)
    return


@app.cell
def _():
    # check if all chars are alpabets

    alpha_str = "aeiou"
    print(f"All Alphabets: {alpha_str.isalpha()}")

    # Check if string is alphaneumeric only
    alpha_num = "a1b2c3"
    print(f"\nAlphanumeric: {alpha_num.isalnum()}")

    # Check if all string values are digits
    dig_chk = "1234"
    print(f"\nAll digits: {dig_chk.isdigit()}")

    # Check if all string values are decminals
    dig_chk_dec = "0.532"
    print(f"\nDigits with decimals: {dig_chk_dec.isdigit()}")
    return


@app.cell
def _():
    # Checking the prefix and suffix of a string

    filename_str = "report_2024.pdf"

    print(f"Prefix: {filename_str.startswith("report")}")
    print(f"\nSuffix: {filename_str.endswith(".pdf")}")
    print(f"\nSuffix false: {filename_str.endswith(".docx")}")
    return


@app.cell
def _():
    # Input validation

    usr_int_chk = input("Enter an integer: ")

    if usr_int_chk.isdigit():
        usr_int_chk=int(usr_int_chk)
        print(f"\nuser entered an integer correctly")
    else:
        print(f"\nUser did not enter an integer")
    return


@app.cell
def _():
    # Input Validation

    usr_name_chk = input("Enter your name: ")

    if usr_name_chk.isalpha():
        print(f"\nEntered name is proper: {usr_name_chk}")
    else:
        print(f"\nEntered string consists of non-alphanumeric chars")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Searching and replacing
    """)
    return


@app.cell
def _():
    sentence = "Python is great and Python is powerful"
    return (sentence,)


@app.cell
def _(sentence):
    # count() - Return the number of non-overlapping occurrences of a sub-string in the string

    print(f"{sentence.count("Python")}")

    print(f"\n{sentence.count("is")}")

    print(f"\n{sentence.count("java")}")
    return


@app.cell
def _(sentence):
    # find() - Locate first occurance: Returns the lowest index in the string where the substring is found. If the substring is found, it returns -1

    print(sentence.find("great"))

    print(f"\n{sentence.find("java")}")
    return


@app.cell
def _(sentence):
    # index() - Locate with error: similar to find(), but retruns an error is substring is not found

    print(f"{sentence.index("great")}")

    print(f"\n{sentence.index("java")}")
    return


@app.cell
def _(sentence):
    # replace() - returns a new string with all the occurances of old substring removed and new substrig in place, option to replace specific number of occurances

    new_sentence = sentence.replace("Python", "Java")

    print(new_sentence)

    new_sentence_1 = sentence.replace("Python", "Java", 1)

    print(f"\n{new_sentence_1}")
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Splitting and Joining
    """)
    return


@app.cell
def _():
    # split(): split string into list

    # Split by space - Default option
    python_sent = "Python is a fun and powerful language"

    words = python_sent.split()

    print(words)

    # Split based on specified operator
    csv_fr = "apple, mango, banana, grapes"

    fruits = csv_fr.split(",")

    print(f"\n{fruits}")

    # splitting an email address
    email_id = "mail@email.com"
    parts = email_id.split("@")

    print(f"\n{parts}")
    print(f"\n{parts[0]}")
    print(f"\n{parts[1]}")
    return


@app.cell
def _():
    # Join(): Combine list into string
    words_list = ["Python", "is", "fun"]

    # Join with space as separator
    words_to_sent = " ".join(words_list)
    print(f"{words_to_sent}")

    # Join with hyphen as separator
    words_to_sent_hy = "-".join(words_list)
    print(f"\n{words_to_sent_hy}")

    # Join with no separator
    words_to_sent_no = "".join(words_list)
    print(f"\n{words_to_sent_no}")

    # Practical example
    items = ["bread", "milk", "eggs", "butter"]

    items_to_sent = ", ".join(items)

    print(f"\nShopping List: {items_to_sent}")
    return


@app.cell
def _():
    # joining list with multiple types
    multi_list = ["s", "h", "r", 1]

    multi_list_sent = " ".join(str(ch) for ch in multi_list)

    print(multi_list_sent)
    print(multi_list_sent[6])
    return


@app.cell
def _():
    # reverse the sentence
    text_q = "anirudh is a good coder and is learning python"

    text_q_split = text_q.split(" ")

    rev_split = text_q_split[::-1]

    print(rev_split)

    final = " ".join(rev_split)

    print(final)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    #### Questions

    - Q1: Take an email as input and validate that it contains exactly one "@" symbol and at-least one ".", print "Valid" or "Invalid"
    - q2: Take a phone number as input in the format +91-98765-43210. Remove all hyphens and country code. Print the cleaned phone number
    - Q3: Input a sentence and split it into words. Print all words starting with a vowel and the word count as well
    - Q4: Input a list of comma separated names. Split them, sort them alphabetically and join them with a "|" as separator
    - Q5: Input a sentence as print the longest word in the sentence
    """)
    return


@app.cell
def _():
    # Q1

    def mail_chk(usr_mail_id: str):

        if usr_mail_id.count("@") == 1 and "." in usr_mail_id:
            print(f"Email ID: {usr_mail_id} is valid")
        else:
            print(f"Email ID is not valid")

    mail_chk("shr@shr.com")
    return


@app.cell
def _():
    #Q2

    def pho_chk(phone_num: str):

        phone_num = phone_num.split("-")[1:]
        clean_num = "".join(phone_num)
        print(clean_num)

    pho_chk("+91-98765-43210")


    # Alternate way
    def phone_number(phone_num: str):

        phone_num = phone_num.replace("-", "")
        alt_clean = phone_num.replace("+91", "")
        print(alt_clean)

    phone_number("+91-98765-43210")
    return


@app.cell
def _():
    #Q3

    def vow_cnt(sent: str):

        tot_w = 0
        all_vowels = "aeiouAEIOU"

        words_fr_sent = sent.split(" ")
        for word in words_fr_sent:
            if word[0] in all_vowels:
                tot_w+=1
                print(word, end=' ')
        print(f"\n\nTotal num of words starting with a vowel: {tot_w}")

    vow_cnt("Uhis zs a Entence")
    return


@app.cell
def _():
    # Q4

    def comma_names(name_list: list[str]):

        joined_names = ",".join(name_list)
        split_names_list = joined_names.split(",")
        sorted_names = "|".join(sorted(split_names_list))

        print(f"Sorted names: {sorted_names}")

    name_list = ["Charlie,Alice,Bob", "David,Eve,Frank"]

    comma_names(name_list)
    return


@app.cell
def _():
    # Q5

    def longest_word(sent: str):

        word_len = 0

        word_len_lst = []

        word_lst = sent.split(" ")

        for wrd in word_lst:
            word_len = len(wrd)
            word_len_lst.append(word_len)

        interm_result = zip(word_lst, word_len_lst)

        result = sorted(interm_result, key=lambda x: x[1], reverse=True)[:1]

        print(result)

    sent = "Enter a sentence and the longest word is programming"
    longest_word(sent)


    # Alternate way

    def print_longest_word(sentence : str):
        words_q5 = sentence.split(" ")
        longest_word_q5 = max(words_q5, key=lambda x: len(x))

        print(longest_word_q5)

    print_longest_word(sent)
    return


@app.cell(hide_code=True)
def _():
    mo.md(r"""
    ### Strip method
    """)
    return


@app.cell
def _():
    url = "https://websiteurl.com/"

    clean_url = url.strip("https:/")

    print(clean_url)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
