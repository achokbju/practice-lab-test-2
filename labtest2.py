# -----------------------------------------------------------
# File:   labtest2.py
# Author: Asher Chok  User ID: achok776   Class: CPS 110
# Desc:   This program is a practice test for lab test 2.
# ----------------------------------------------------------- 

def split_n_splice(s, sep, glue):
    """split <s> on <sep> and return a list of the split words separated by <glue>



    if <sep> is not found in <s>, return [<s>, <glue>]



    if <s> is empty, return [<glue>]



    >>> split_n_splice('1-2-3', '-', ' baNAna ')

    ['1', ' baNAna ', '2', ' baNAna ', '3']



    >>> split_n_splice('1', '-', '...fred...')

    ['1', '...fred...']



    >>> split_n_splice('', '+', 'NATCH')

    ['NATCH']

    """

    if len(s) == 0:
        return [glue]
    else:
        # For situations where delimiter is not found, splitted s will still be same size
        # where "1,2,3".split(".") ==> returns ["1,2,3"] which is length of 1
        # but "1,2,3".split(",") ==> returns ["1","2", "3"] which is length not of 1
        splitted_string_s = s.split(sep)
        if len(splitted_string_s) == 1:
            return [s, glue]
        else:
            # Glue is always -1 of the amount of elements in s, so
            # n elements of s will have n-1 elements of glue
            sandwich = []
            for i in range(len(splitted_string_s)):
                sandwich.append(splitted_string_s[i])
                if i != len(splitted_string_s) - 1: # If not last element
                    sandwich.append(glue)

            return sandwich

def extract(items, filter_key, filter_value, capture_key):
    """extract values from a list of dictionaries based on filter/capture parameters



    <items>: a list of dictionaries ("items")

    <filter_key>: key to look up when checking for <filter_value>

    <filter_value>: value to compare against when deciding to take/drop this item;

                    i.e., if this item's <filter_key> value matches <filter_value>,

                    take the item; otherwise, ignore the item

    <capture_key>: if an item is "taken" (by <filter_key>/<filter_value>), take the

                    value stored under this key (ignore this item if no such key exists)



    >>> extract([

    ...     {"state": "MA", "city": "Boston"},

    ...     {"state": "SC", "city": "Greenville"},

    ...     {"state": "SC", "city": "Taylors"},

    ... ], "state", "SC", "city")

    ['Greenville', 'Taylors']



    >>> extract([

    ...     {"state": "MA", "city": "Boston"},

    ...     {"state": "SC", "city": "Greenville"},

    ...     {"state": "SC", "village": "Pumpkin Town"},

    ... ], "state", "SC", "city")

    ['Greenville']

    """
    found_values = []
    for dict in items:
        if dict[filter_key] == filter_value:
            try:
                found_values.append(dict[capture_key])
            except:
                # ignore this dict if no such key exists
                pass

    return found_values

def parsify(junk: str) -> dict:
    """parse <junk> into a dictionary of name/values using these rules:

    

    <junk> is a string containing one or more "definitions"

    a "definition" looks like this: "(name value that may contain spaces)"

    neither names nor values can contain "(" or ")" characters



    `parsify` should return a dictionary mapping the names to the values

    e.g., {"name": "value that may contain spaces"}



    basic level: you may assume that each definition has a unique name



    extra credit level: allow multiple definitions; if a name is defined

                        MORE THAN ONCE, the dictionary should map that

                        name to a list of the values (but ONLY if there

                        are multiple definitions; single definitions should

                        still have the name map directly to the value

    

    >>> parsify("  (a bat) (wonderful stuff with stuff)       (num 42)")

    {'a': 'bat', 'wonderful': 'stuff with stuff', 'num': '42'}



    >>> parsify("(a one) (a two) (b wan)")  # extra-credit level test

    {'a': ['one', 'two'], 'b': 'wan'}

    """

    # Save them first
    sentences = []
    current_sentence = ""
    is_open_bracket = False

    for char in junk:
        if char == "(":
            is_open_bracket = True
            current_sentence = "" # Reset
            continue
        elif char == ")":
            is_open_bracket = False
            sentences.append(current_sentence)
            continue
        elif is_open_bracket == True:
            current_sentence += char
            continue

    dict = {}

    for s in sentences:
        spliced = s.strip().split()   # Returns to an array object 

        if spliced[0] in dict:
            # Save current value
            temp = dict[spliced[0]]
            dict[spliced[0]] = [temp, spliced[1]]
            pass
        else:
            dict[spliced[0]] = " ".join(spliced[1:])

    return dict

def test_split_n_splice():
    assert split_n_splice('1-2-3', '-', ' baNAna ') == ['1', ' baNAna ', '2', ' baNAna ', '3']
    assert split_n_splice('1', '-', '...fred...') == ['1', '...fred...']
    assert split_n_splice('', '+', 'NATCH') == ['NATCH']

def test_extract():
    assert extract([{"state": "MA", "city": "Boston"},
                    {"state": "SC", "city": "Greenville"},
                    {"state": "SC", "city": "Taylors"},], 
                    "state", "SC", "city") == ['Greenville', 'Taylors']
    
    assert extract([{"state": "MA", "city": "Boston"},
                   {"state": "SC", "city": "Greenville"},
                   {"state": "SC", "village": "Pumpkin Town"},], 
                    "state", "SC", "city") == ['Greenville']
    
def test_parsify():
    assert parsify("  (a bat) (wonderful stuff with stuff)       (num 42)") == {'a': 'bat', 'wonderful': 'stuff with stuff', 'num': '42'}
    assert parsify("(a one) (a two) (b wan)") == {'a': ['one', 'two'], 'b': 'wan'}