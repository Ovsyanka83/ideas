# ideas

**Easy creation of custom import hooks to try out new ideas for Python.**

![ideas logo](ideas.png)


[Documentation](https://aroberge.github.io/ideas/docs/html/)

## Installation

```
pip install ideas
```

## Usage

Suppose that you want to use `function` as a keyword in Python, to mean
the same thing as `lambda`, enabling you to write

```python
square = function x: x**2
print(f"{square(4)} is the square of 4.")
```

You could do this by creating the following program

```python
# Lets's call this 'loader.py'

from ideas.examples import function
function.add_hook()

import my_script
```

and then run

```
python loader.py
```

So, `my_script.py` and any other module loaded by it would recognize that
`function` is a valid alternative to `lambda`.

Many more examples can be found in the [documentation](https://aroberge.github.io/ideas/docs/html/).

## Infrequently asked questions ... and comments

The following list has been created before anyone else knew about
this project.

> Why?

Because it is fun.

If you want a longer answer, have a look at
[motivation](https://aroberge.github.io/ideas/docs/html/motivation.html).

> Is it safe to use in production code?

No.

> I found a bug.

Please, by all means, file an issue so that I can fix it.

> I found a cool use of import hooks in another project, different from
> all of your examples.

Please, give me the details and I will see if I can include a similar example.

> Can I contribute code for a new example?

Yes, by all means. But I suggest that you first create an issue that gives
an overview of what you wish to accomplish.

> I think that the explanation you have written for X could be improved upon.

Please, by all means, file an issue or create a pull-request.

> I have an idea for a new example, but do not know how to write the code for it.

File an issue ... but please don't be offended if I don't write code for it
and end up closing the issue: I already have too many ideas of my own and not
enough time to implement them.

> In file X.py, you do not respect convention Y from PEP-8. This is unacceptable
> in a Python project.

Seriously?  This project is all about looking at introducing changes
to Python's syntax, some of which are downright crazy, and you complain
about a PEP-8 violation? ...  Ok, perhaps you can tell me and it might
make sense to change what I wrote.

> People from the Python-ideas mailing lists mentioned that I should look
> at this project for my idea, but I don't know where to start.

Please, have a look at the [documentation](https://aroberge.github.io/ideas/docs/html/).

> Why this silly name for a project? The word "ideas" has nothing to do with
> import hooks in Python.

For this project, I was thinking of using `importhook` (singular) or
`importhooks` (plural). However, there is already a project named
`importhook` on Pypi and I thought that using the plural form would
likely be just too confusing.

I settled on `ideas` as I am guessing that the main application would be
for people to try out suggestions from or for python-ideas.


## Tools

This project uses black for formatting, pytest for running tests,
and flake8 for linting.

## Contact:

You can either file an issue or email me at <Andre.Roberge@gmail.com>.


## License

MIT



