expression = (3 + 2) * 4 < 10 and (15 % 3 == 0 or 7 // 2 == 3)
prediction = False  # (3 + 2) * 4 is 20, which is greater than 10 (False)
result = eval('expression')
print(f"Prediction: {prediction}")
print(f"Result: {result}")

if prediction == result:
  print("Prediction is correct!")
else:
  print("Prediction is incorrect.")