# clean.py
"""Refactored version of messy.py with descriptive names and docstrings."""

from unicodedata import numeric


BONUS_THRESHOLD = 50
ADJUSTMENT = 10

def calculate_product (first, second) :
    """Return the product of two numbers."""
    return first * second

def apply_mode_adjustment (product, first, mode) :
    """Adjust the product by 'first' depending on the mode.

    Args:
    product: Product of the first two inputs.
    first: The first input value.
    mode: 1 adds 'first' and doubles the result; any other value
    subtracts 'first' and triples the result.

    Returns:
    The scaled, adjusted value.
    """
    if mode == 1:
        return (product + first) * 2
    return (product - first) * 3

def apply_threshold_correction (value) :
    """Subtract 10 if value exceeds 50, otherwise add 10."""
    if value > BONUS_THRESHOLD:
        return value - ADJUSTMENT
    return value + ADJUSTMENT

def process(first, second, mode) :
    """Run the full calculation pipeline.

    Args:
    first: First numeric input.
    second: Second numeric input.
    mode: Mode selector (1 or any other value).

    Returns:
    The final computed result.
    """
    product = calculate_product (first, second)
    adjusted = apply_mode_adjustment (product, first, mode)
    return apply_threshold_correction (adjusted)

print (process (4, 6, 1) )