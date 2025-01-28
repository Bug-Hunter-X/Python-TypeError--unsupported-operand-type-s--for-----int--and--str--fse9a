def function(a, b):
    try:
        b = int(b)  # Convert b to an integer
        return a + b
    except ValueError:
        return "Error: Cannot convert b to integer"

result = function(5, '10')
print(result)
result2 = function(5, 'abc')
print(result2)