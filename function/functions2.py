def Name(): 
    name =input("Enter Your Name: ")
    return name

def Age(): 
    age=input("Enter your Age: ")
    # print("Name: " + Name() + ('\n') + "Age: "+ str(age)) 
    print(Name(), age)
   
Age()