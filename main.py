# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = round(weight/(height*height))
if bmi<18.5:
  print(f"Your bmi is {bmi}, you are underweight")
elif bmi<25:
  print(f"Your bmiis {bmi}, you have a normal weight ")
elif bmi<30:
  print(f"Your bmi is {bmi},you are slightly over weight")
elif bmi<35:
  print(f"Your bmi is {bmi},you are obese")
elif bmi>35:
  print(f"Your bmi is {bmi},you are clinically obese")
else:
  print("Try again")





