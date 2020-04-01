#created on 22/aug/2019
#author: samuvel
print("BMI calculator")
name=str(input('enter your name'))
a=float(input('enter the height in meters:'))
b=float(input('enter the weight in kilograms:'))#getting name,hight and weight of the user
if(a>6):
    a=a/100# meter to cm
c=b/a**2#bmi formulae
if(c>=25.0):#separating categery based on the result
              print("you come under overweight and your BMI is",c)
elif(c>=18.5 and c<=24.9):
              print("you come under  healthy and your BMI is",c)
elif(c<18.5):
              print("sorry you come  under underweight and your BMI is",c)
elif(c<0):
              print("the given hight or weight is wrong")# if anything goes wrong 
print("THANK YOU FOR USING CALC Mr. "+name)
print("and im IRON MAN")
