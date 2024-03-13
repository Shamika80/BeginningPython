def evaluate_expression(expression):

  return eval(expression) 

expression1 = "2 + 3 * 4"  
expression2 = "(2 + 3) * 4"  

result1 = evaluate_expression(expression1)
result2 = evaluate_expression(expression2)

print(f"Expression 1: {expression1} = {result1}")
print(f"Expression 2: {expression2} = {result2}")

if result1 == result2:
  print("Results match.")
else:
  print("Results differ.")
