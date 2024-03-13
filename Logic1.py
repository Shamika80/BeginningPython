def boolean_logic(value1, value2, operator):
    """Performs boolean operations based on the given values and operator."""

    if operator.upper() == "AND":
        return value1 and value2
    elif operator.upper() == "OR":
        return value1 or value2
    elif operator.upper() == "NOT":
        if value2 is not None:  
            raise ValueError("NOT operator requires only one value.")
        return not value1
    else:
        raise ValueError(f"Invalid operator. Please use 'AND', 'OR', or 'NOT'. Examples: boolean_logic(True, False, 'AND')")

value_a = True
value_b = False


result_and = boolean_logic(value_a, value_b, "AND")
result_or = boolean_logic(value_a, value_b, "OR")

print(f"value_a AND value_b: {result_and}")
print(f"value_a OR value_b: {result_or}")
print(f"NOT value_a: {boolean_logic(value_a, None, 'NOT')}")

try:
    invalid_result = boolean_logic(value_a, value_b, "XOR")  
except ValueError as e:
    print(e)