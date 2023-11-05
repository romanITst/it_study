#
#
# MY COPY of Lesson: Introduction to Python Programming
#
#
#
#
#

## Learning Objectives

- Understand the basics of Python programming language.
- Explore essential concepts such as pip, basic data types, virtual environments (venv), and Jupyter Notebook.

## Agenda

1. [Introduction to Python](https://github.com/zm99by/devops_linux_course/tree/python/lesson_01#1-introduction-to-python)
    - What is Python?
    - Why Python?
    - Python's simplicity and readability.

2. [Installing Python](https://github.com/zm99by/devops_linux_course/tree/python/lesson_01#2-installing-python)
    - How to download and install Python on your system.
    - Verifying your Python installation.

3. [PIP - Python Package Installer](https://github.com/zm99by/devops_linux_course/tree/python/lesson_01#3-pip---python-package-installer)
    - What is pip?
    - How to install packages using pip.
    - Managing dependencies with pip and requirements.txt.

4. [Basic Data Types in Python](https://github.com/zm99by/devops_linux_course/tree/python/lesson_01#4-basic-data-types-in-python)
    - Numeric Data Types (*int*, *float*).
    - Strings (*str*).
    - Boolean (*bool*).
    - Variables and assignments.
    - Multi-assignment in Python.
    - Chained assignment in Python.

5. [Virtual Environments (venv)](https://github.com/zm99by/devops_linux_course/tree/python/lesson_01/#5-virtual-environments-venv)
    - What is a Virtual Environment?
    - Why Use Virtual Environments?
    - Creating and activating a virtual environment.
    - Deactivating and deleting a virtual environment.

6. [IPython](https://github.com/zm99by/devops_linux_course/tree/python/lesson_01#6-IPython)
    - What is IPython?
    - Interactive Coding
    - Tab Completion
    - Introspection and Help
    - Magic Commands
    - Execute Shell Commands

## Lesson Content

### 1. Introduction to Python

**What is Python?**

Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python is widely used in web development, data science, machine learning, and various other fields.

**Why Python?**

- Readable and easy to learn.
- Large, active community.
- Versatile and applicable in various domains.
- Extensive library support.

**Python's Simplicity and Readability**

Python's syntax emphasizes code readability, which makes it an excellent choice for beginners. It uses indentation to define code blocks, eliminating the need for braces or semicolons.

### 2. Installing Python

**How to Download and Install Python**

You can download Python from the [official website](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

For Linux Ubuntu you can do following steps:
    - sudo apt update
    - sudo apt install software-properties-common
    - sudo add-apt-repository ppa:deadsnakes/ppa
    - sudo apt update
    - sudo apt install python3.11/12/13

**Verifying Your Python Installation**

Open a terminal or command prompt and run python --version. It should display the installed Python version.

### 3. PIP - Python Package Installer

**What is pip?**

- Pip is a package manager for Python, used to install and manage libraries and packages.
- It simplifies the process of installing third-party packages and their dependencies.

**How to Install Packages Using pip?**

You can use the following commands to install a package:

- Using pip:

```bash
pip install package_name
```

- Using python -m pip:

```bash
python -m pip install package_name
```

Both of these commands will install the specified package. You can replace package_name with the name of the package you want to install.

**Managing Dependencies with pip and requirements.txt**

Pip allows you to manage project dependencies using a requirements.txt file. This file lists all the required packages for your project, making it easy to install them all at once. To create a requirements.txt file, follow these steps:

1. Create a new text file and name it requirements.txt.
2. List the required packages, one per line, in the requirements.txt file. For example:

```txt
package1
package2
package3==1.0.0
```

To install the packages listed in requirements.txt, you can use either of the following commands:

- Using pip:

```bash
pip install -r requirements.txt
```

- Using python -m pip:

```bash
python -m pip install -r requirements.txt
```

Both commands will read the requirements.txt file and install all the specified packages and their versions.

Managing dependencies with requirements.txt is essential for ensuring that your project can be easily reproduced on different systems or by other developers. It simplifies the process of sharing and deploying your Python projects while ensuring consistency in package versions.

### 4. Basic Data Types in Python

**Numeric Data Types**

- int (*integers*)
- float (*floating-point numbers*)

**Strings (*str*)**

Strings are sequences of characters enclosed in single, double, or triple quotes. Example: "Hello, World!".

**Boolean (*bool*)**

Booleans represent True or False values and are used in logical operations.

**Variables and Assignments**

- Variables are used to store data.
- Assign values to variables using the assignment operator =.

| Data Type          | Description                                 | Example               |
|--------------------|---------------------------------------------|-----------------------|
| `int` (Integer)   | Whole numbers without a decimal point.     | `42`, `-123`, `0`     |
| `float` (Floating-Point) | Real numbers with a decimal point.   | `3.14`, `-0.01`, `2.0` |
| `str` (String)    | Text or sequence of characters.            | `"Hello, Python"`, `'123'` |
| `bool` (Boolean)  | Binary values representing `True` or `False`. | `True`, `False`     |
| `dict` (Dictionary)| Key-value pairs.                         | `{'name': 'John', 'age': 30}` |
| `set` (Set)       | Collection of unique elements.            | `{1, 2, 3}`, `{'apple', 'banana'}` |
| `list` (List)     | Ordered, mutable collection of items.    | `[1, 2, 3]`, `['apple', 'banana']` |
| `tuple` (Tuple)   | Ordered, immutable collection of items.  | `(1, 2, 3)`, `('apple', 'banana')` |
| `frozenset`       | Immutable set, like `set` but cannot be changed. | `frozenset([1, 2, 3])` |

Data Type Examples

#### Integer (`int`)

```python
my_integer = 42
print(my_integer)        # Output: 42
print(type(my_integer))  # Output: <class 'int'>
```

#### Float (`float`)

```python
my_float = 3.14
print(my_float)        # Output: 3.14
print(type(my_float))  # Output: <class 'float'>
```

#### String (`str`)

```python
my_string = "Hello, World!"
print(my_string)        # Output: Hello, World!
print(type(my_string))  # Output: <class 'str'>
```

#### Boolean (`bool`)

```python
my_boolean = True
print(my_boolean)        # Output: True
print(type(my_boolean))  # Output: <class 'bool'>
```

#### List (`list`)

```python
my_list = [1, 2, 3, 4, 5]
print(my_list)        # Output: [1, 2, 3, 4, 5]
print(type(my_list))  # Output: <class 'list'>
```

#### Tuple (`tuple`)

```python
my_tuple = (10, 20, 30)
print(my_tuple)        # Output: (10, 20, 30)
print(type(my_tuple))  # Output: <class 'tuple'>
```

#### Dictionary (`dict`)

```python
my_dict = {"name": "Alice", "age": 30}
print(my_dict)        # Output: {'name': 'Alice', 'age': 30}
print(type(my_dict))  # Output: <class 'dict'>
```

#### Set (`set`)

```python
my_set = {1, 2, 3, 4, 4}
print(my_set)        # Output: {1, 2, 3, 4}
print(type(my_set))  # Output: <class 'set'>
```

**Multi-Assignment in Python**

Python allows you to assign multiple variables in a single line using a single expression. This is known as multi-assignment. Here are some examples:

```python
a, b = 1, 2  # Assigns 1 to a and 2 to b
x, y, z = 10, 20, 30  # Assigns 10 to x, 20 to y, and 30 to z
name, age = "Alice", 30  # Assigns "Alice" to name and 30 to age
a, b, *c = 1, 2, 3, 4  # Assigns 1 to a, 2 to b, and [3, 4] to c
a, b = b, a
```

**Chained Assignment in Python**

Python also allows chained assignment, where multiple variables are assigned the same value or receive multiple values in a single line. Here are some examples:

- Assigning the same value to multiple variables:

```python
  a = b = c = 1  # Assigns the value 1 to a, b, and c
```

### 5. Virtual Environments (venv)

**What is a Virtual Environment?**

A virtual environment is an isolated environment that allows you to manage project-specific dependencies separately from the system-wide Python installation.

**Why Use Virtual Environments?**

- Avoid conflicts between project dependencies.
- Ensure reproducibility of projects.
- Manage different Python versions for various projects.

**Creating and Activating a Virtual Environment**

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

**Deactivating and Deleting a Virtual Environment**

To deactivate the environment:

```bash
deactivate
```

To delete the environment, simply delete its directory.

### 6. IPython

**1. What is IPython?**

- Python's standard interactive shell is helpful, but there's more. We'll introduce you to IPython, an enhanced interactive Python environment that makes coding and experimenting more efficient.

```bash
pip install ipython
```

**2. Interactive Coding:**
   - In a IPython, you can execute Python code interactively. For example:

   ```python
   a = 10
   b = 20
   result = a + b
   result
   ```

**3. Tab Completion:**
   - IPython's tab completion feature allows you to quickly access variable names and function names. Type the beginning of a variable or function and press `Tab` to see suggestions. For example:

   ```python
   some_very_long_variable_name = "Hello, World!"
   # Type 'some_very_l' and press 'Tab' to complete the variable name.
   ```

**4. Introspection and Help:**
   - Use `?` to access documentation and information about objects or functions. For example:

   ```python
   # Get information about a function or module
   import math
   math.log?

   # Get more detailed information
   math.log??
   ```

**5. Magic Commands:**
   - IPython provides magic commands, such as `%run` for running external scripts and `%timeit` for timing code. For example:

   ```python
   # Run an external Python script
   %run my_script.py

   # Measure the execution time of a code block
   %timeit [x for x in range(1000)]
   ```

**6. Execute Shell Commands:**
   - You can run shell commands within a Jupyter Notebook cell by prefixing them with `!`. For example:

   ```python
   # List files in the current directory
   !ls
   ```

## Conclusion

Python is a versatile and powerful programming language with a wealth of libraries and tools. Understanding the basics of Python, managing packages with pip, using Jupyter Notebook, and working in virtual environments are crucial skills for any Python programmer. With this knowledge, you can start your journey into the world of Python development and data analysis.


## Homework

1. Install python3.11/12/13 on your VM
2. Install virtualenv tool
3. Create 2 virtual environments, activate them, deactivate
4. Install ipython, try to create several variable with diffrent data types, check their types and use help (?, ??).
5. Try to print "Hello, world!"
