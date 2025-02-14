"""confused_math_bc.py
------------------------

Import hook that performs bytecode changes,
swapping BINARY_ADD and BINARY_MULTIPLY.

Note: If code contains something like a + b, or a * b, where
a and b are integer literals (e.g. 2 + 4), the operations are
done prior to the creation of a code object and thus are
not captured by this transformation.
"""
import dis
import sys
from types import CodeType
from ideas import import_hook

# The actual bytecode used can change with different Python version.
# Instead of attempting to hard-code some actual bytecode values
# we extract the actual value used in the current Python version.
ADD = dis.opmap["BINARY_ADD"]
MUL = dis.opmap["BINARY_MULTIPLY"]


def swap_add_mul(bytecode):
    """Interchange BINARY_ADD and BINARY_MULTIPLY"""
    new_bc = []
    for i, b in enumerate(bytecode):
        if b == ADD and i % 2 == 0:
            new_bc.append(MUL)
        elif b == MUL and i % 2 == 0:
            new_bc.append(ADD)
        else:
            new_bc.append(b)
    return bytes(new_bc)


def create_new_co(code_object):
    """Recursively creates new code objects from old ones, swapping
    BINARY_ADD and BINARY_MULTIPLY.
    """
    new_code = swap_add_mul(code_object.co_code)
    new_const = []
    for c in code_object.co_consts:
        if isinstance(c, CodeType):
            new_const.append(create_new_co(c))
        else:
            new_const.append(c)

    if sys.version_info.minor in (6, 7):
        new_code_object = CodeType(
            code_object.co_argcount,
            code_object.co_kwonlyargcount,
            code_object.co_nlocals,
            code_object.co_stacksize,
            code_object.co_flags,
            new_code,
            tuple(new_const),
            code_object.co_names,
            code_object.co_varnames,
            code_object.co_filename,
            code_object.co_name,
            code_object.co_firstlineno,
            code_object.co_lnotab,
            code_object.co_freevars,
            code_object.co_cellvars,
        )
    else:
        new_code_object = CodeType(
            code_object.co_argcount,
            code_object.co_posonlyargcount,  # new in Python 3.8
            code_object.co_kwonlyargcount,
            code_object.co_nlocals,
            code_object.co_stacksize,
            code_object.co_flags,
            new_code,
            tuple(new_const),
            code_object.co_names,
            code_object.co_varnames,
            code_object.co_filename,
            code_object.co_name,
            code_object.co_firstlineno,
            code_object.co_lnotab,
            code_object.co_freevars,
            code_object.co_cellvars,
        )
    return new_code_object


def transform_bytecode(code_object, **_kwargs):
    """Transforms the code object into a new code object"""
    new_code_object = create_new_co(code_object)
    return new_code_object


def add_hook(**_kwargs):
    """Creates and automatically adds the import hook in sys.meta_path"""
    hook = import_hook.create_hook(
        hook_name=__name__,
        transform_bytecode=transform_bytecode,
    )
    return hook
