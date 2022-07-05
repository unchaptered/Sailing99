# Python

- Installation
- Python Settings
- Python Modules
- Python Syntax

## Installation

- Local Python 3.9
- Lecture Python 3.8

<hr>

## Python Settings

When I initialization of Python Virtual Env, using PyCharm.
I have 2 Folders right these.

| name  | info |
| :---- | :--- |
| .idea | Project Folders Settings for Launch [more](https://rider-support.jetbrains.com/hc/en-us/articles/207097529-What-is-the-idea-folder-) |
| venv  | Files for Virtual Environments |

<hr>

## Python Modules

```cmd
 <!-- for ajax -->
requests

<!-- for Crolling-->
bs4

<!-- for Conenct to MongoDB Atlas>
pymongo
dnspython
```
<hr>

## Python Syntax

### print

```python
print('Hello, world!');
```

### variable

```python
a = 3;
```

### list

```python
alphabets = ['a', 'b', 'c'];

print(alphabets);
```

### dictionary

```python
user = {
    'name': 'unchaptered',
    'age': 27
}
```

### function

```python
def sum(a, b):
    return a+b;
```

example

```python
def sum(a, b):
    return a+b;

result = sum(1, 2);
print(result);
```

### condition

```python
def isAudult(age):
    if age > 20:
        print('Adult');
    else:
        print('Not Adult');
```

### loop

```python
for fruit in fruits:
    print(fruit)
```

example

```python
for person in people:
    if person['age'] > 20:
        print(ppp['name']);
```