def is_perfect_square (num):

  if num < 0:
    return False

  sqrt = num ** 0.5
  return sqrt == int(sqrt)

number = 16

if is_perfect_square(number):
  print(f"{number} is a perfect square.")
else:
  print(f"{number} is not a perfect square.")