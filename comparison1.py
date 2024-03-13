number1 = 10
number2 = 20

# Call the swap_values function and unpack the returned tuple
swapped_num1, swapped_num2 = 'swap_values'(number1, number2)

# Compare the original and swapped values to confirm swapping
print("\nVerifying the swap:")
if number1 != swapped_num2 or number2 != swapped_num1:
  print("Error: Values not swapped correctly.")
else:
  print("Values swapped successfully!")