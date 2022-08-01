""""
 lets make a BMI balculator
1.declare a variable with the name "weight".
2. ask user to input heir weight on lb.
3. assiin user input to the variable "weight"
4.to change string to number value use float().
5. declare other variable height.
6. ask user to input the height on inch
7. assign the input value with the varaible "height"
8. change the input to number using float() function.
9. declare one more variable with the name BMI
10. give the variable with the value (weight/height**)*703 which is the formula of BMI.
11. display the value og BMI with your BMI is ,BMI."""
weight=input("enter your weight on lb ")
weight=float(weight)
height=input("input your height on inches ")
height=float(height)
BMI=weight/(height*height)
BMI=BMI*703
print("you BMI is ",BMI)


