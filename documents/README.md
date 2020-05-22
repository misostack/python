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

5. Datatypes

5.1. Numbers

> int, float, complex

> **Integers can be of any length, it is only limited by the memory available**

> **A floating-point number is accurate up to 15 decimal places**

5.2. List

> List is an ordered sequence of items. Declaring a list is pretty straight forward. Items separated by commas are enclosed within brackets [ ]

> Lists are mutable, meaning, the value of elements of a list can be altered.

5.3. Tuple

> Tuple is an ordered sequence of items same as a list. The only difference is that tuples are immutable. Tuples once created cannot be modified.

> Tuples are used to write-protect data and are usually faster than lists as they cannot change dynamically.

> It is defined within parentheses () where items are separated by commas.

5.4. String

> String is sequence of Unicode characters. We can use single quotes or double quotes to represent strings. Multi-line strings can be denoted using triple quotes, ''' or """

> Just like a list and tuple, the slicing operator [ ] can be used with strings. Strings, however, are immutable.

5.5. Set

> Set is an unordered collection of unique items. Set is defined by values separated by comma inside braces { }. Items in a set are not ordered.

> We can perform set operations like union, intersection on two sets. Sets have unique values. They eliminate duplicates.

> Since, set are unordered collection, indexing has no meaning. Hence, the slicing operator [] does not work.

5.6. Dictionary

> Dictionary is an unordered collection of key-value pairs.

> It is generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data. We must know the key to retrieve the value.

> In Python, dictionaries are defined within braces {} with each item being a pair in the form key:value. Key and value can be of any type.

5.7. Conversion between data types

> int(), float(), str()

> set([1,2,3])

> tuple({1, 2, 3})

> list('hello')

To convert to dictionary, each element must be a pair:

> dict([['a',2], ['b',4]])

6. Type Conversion

6.1. Implicit Type Conversion

> In Implicit type conversion, Python automatically converts one data type to another data type. This process doesn't need any user involvement.

> Python always converts smaller data types to larger data types to avoid the loss of data

> Python is not able to use Implicit Conversion when you want to convert from "str" to "num"

> Explicit Type Conversion is also called Type Casting, the data types of objects are converted using predefined functions by the user.

> In Type Casting, loss of data may occur as we enforce the object to a specific data type.

7. Python Input, Output and Import

> print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

Output formatting

Input

**Import**

```python
import math
from math import pi

import sys
print(sys.path)
```