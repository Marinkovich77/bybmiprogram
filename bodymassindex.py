#This file calculates body mass index


weight = float(input ("Enter weight in kg:"))
height = float(input ("Enter height in cm:"))

BMI = weight / (height/100)**2

print("BMI is", BMI)