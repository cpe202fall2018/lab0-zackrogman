def weight_on_planets():
   a = input("What do you weigh on earth? ") #asks for input
   w = int(a) #casting the given weight as an int
   M = "On Mars you would weigh" #making a string variable
   J = "On Jupiter you would weigh" #making a string variable
   if w >= 0: #making sure inputed weight is valid
      print("\n" + M,w*.38,"pounds.\n" + J,w*2.34,"pounds.") #output with casted strings and the calculations
   else: #if inputed weight is not valid
      print("\nEntered weight is not valid.") #output informing user that weight entered is not valid
   
if __name__ == '__main__':
   weight_on_planets()
