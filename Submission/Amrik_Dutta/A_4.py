print("Program to compute simple and compound interest :")
p = float(input("Enter principle amount: "))
r = float(input("Enter duration in years: "))
t = float(input("Enter rate of interest: "))
si = (p+((p*r*t)/100))
ci = p * (pow((1 + r / 100), t))
print("The simple interest amount including principal is: ",si)
print("The compound interest amount including principal is :  ",ci)
