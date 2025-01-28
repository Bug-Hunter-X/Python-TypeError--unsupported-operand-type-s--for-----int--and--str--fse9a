# Python TypeError: unsupported operand type(s) for +: 'int' and 'str'

This example demonstrates a common Python error: `TypeError: unsupported operand type(s) for +: 'int' and 'str'`.  This occurs when attempting to use the `+` operator with an integer and a string, which are incompatible types for this operation. The solution involves type conversion to ensure both operands are of the same type before addition.

## Bug

The `bug.py` file contains a function that attempts to add an integer and a string. This directly results in a `TypeError`. 

## Solution

The `bugSolution.py` file shows the corrected code that converts the string to an integer before performing the addition, avoiding the error. This robust approach prevents runtime errors caused by mismatched data types.