def calculate_savings(initial_amount, interest_rate):

  if not isinstance(interest_rate, (float, int)):
    raise ValueError("Interest rate must be a number.")

  interest_earned = initial_amount * interest_rate

  total_amount = initial_amount + interest_earned

  return total_amount

initial_amount = 1000.00
interest_rate = 0.05  

try:
  total_amount = calculate_savings(initial_amount, interest_rate)
  print(f"Total amount after a year: ${total_amount:.2f}")
except ValueError as e:
  print(e)