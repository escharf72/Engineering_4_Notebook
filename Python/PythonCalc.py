#Calculator
#Written by: Abigail Paquette and Elisabeth Scharf
num = 1
def doMath(a,b,c):
  int1 = int(a)
  int2 = int(b)
  rep = int(c)
  #print(rep)
  if rep == 1:
    return("The sum is: " + str(int1 + int2))
  if rep ==2:
    return("The difference is:" + str(int1-int2))
  if rep == 3:
    return("The product is:" + str(int1*int2))
  if rep == 4:
    div = round((int1/int2),2)
    return("The quotient is:" + (str(div)))
  if rep == 5:
    return("The modulo is:" + str(int1%int2))


while True:
  if num == 1:
    a = input("Please enter you first number:")
    b = input("Please enter your second number:")
    num = 2
  print(doMath(a,b,1))
  print(doMath(a,b,2))
  print(doMath(a,b,3))
  print(doMath(a,b,4))
  print(doMath(a,b,5))
  num = 1
