# Documents

## Python Fundamentals

Ref : https://www.programiz.com/python-programming/first-program

1. Debug

Key | Type 
---------|----------
 **F9** | Toggle BreakPoint
 **F5** | Continue 
 **Shift + F5** | Stop Debugging

2. Keywords-Identifier

Ref : https://www.programiz.com/python-programming/keywords-identifier

2.1. Keywords

> All the keywords except **True**, **False** and **None** are in lowercase and they must be written as they are. The list of all the keywords is given below

2.2. Identifier

> An identifier is a name given to entities like class, functions, variables, etc. It helps to differentiate one entity from another.

> Python is a case-sensitive language. This means, Variable and variable are not the same

3. Statements & Comments

3.1. Statement && Multi-line statement

```python
x = 1 + 2 + 3 + 4 + 5 + 6

print(x)

x = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

print(x)

a = (1 + 2 + 3 +
    4 + 5 + 6 +
    7 + 8 + 9)

print(a)

colors = ['green',
          'blue',
          'red']

print(colors)

a = 1; b = 2; c = 3

print(a, b, c)
```

3.2. Python Indentation

> Generally, four whitespaces are used for indentation and are preferred over tabs. Here is an example.

3.3. Python Comments

```python
# single line

# line1
# line2
# line3

'''This is a multiline
comment in python which wrapped by
tripple quote'''
```

- https://www.programiz.com/python-programming/comments

- Standard: https://www.programiz.com/python-programming/docstrings

- Use comments to describe what a function does and not the specific details on how the function does it.
- Try to remove as many redundant comments as possible. Try writing code that can explain itself, using better function/variable name choice.
- Try to make the comments as short and concise as possible.

4. Variables, Constants and Literals

- Ref : https://www.programiz.com/python-programming/variables-constants-literals

> Note: Python is a **type-inferred** language, so you don't have to explicitly define the variable type

4.1. Variables

4.2. Constants

> In Python, constants are usually declared and assigned in a module. Here, the module is a new file containing variables, functions, etc which is imported to the main file. Inside the module, constants are written in all capital letters and underscores separating the words.

4.3. Rules and Naming Convention for Variables and constants

> If you want to create a variable name having two words, use underscore to separate them. For example: a_new_variable

4.4. Literals

> Literal is a raw data given in a variable or constant. In Python, there are various types of literals they are as follows:

- Numeric : integer, float, complex

- https://www.programiz.com/python-programming/numbers