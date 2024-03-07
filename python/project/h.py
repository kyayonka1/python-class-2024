# super market registor program

  # class with dictionary of items available and their prices
class Buys:
    dict1={"pens":"price = 1100ugx per piece","color pencils":"price = 2000ugx per piece ",
           "pencils":"price = 3000ugx per piece","books":"books" = 3000ugx per piece","ruler":"price = 5000ugx per loaf"}
    
    dict2={"pens":1100 ,"color pencils":2000 ,
           "pencils":3000 ,"books": 3000 ,"": 5000 }
    def __init__(self):
        pass

    
    

  # class implimentation
T = Buys.dict2.get("pens")
O = Buys.dict2.get("pencils")
C = Buys.dict2.get("color pencils")
L = Buys.dict2.get("books")
B = Buys.dict2.get("ruler")
    
    
    
print("......................................................")
print("             welcome to our store                     ")
print("......................................................")




  # program process code
print("                                   ")
print("What do you want to buy?")
print("1. pens \n2. pencils \n3. pencils \n4. color pencils \n5. books" )

Answer_1 = input("Enter your answer :")

def Process():
    
    if Answer_1 == "1":
        print(Buys.dict1.get("pens"))
        Answer_2 = int(input("How many do you want : "))
    
        print("Your total is = ",Answer_2*T, "ugx")
        

    
    elif Answer_1 =="2":
        print(Buys.dict1.get("pencils"))
        Answer_2 = int(input("How many do you want : "))
        print("Your total is = ",Answer_2*O, "ugx")
   
    elif Answer_1 =="3":
        print(Buys.dict1.get("color pencils"))
        Answer_2 = int(input("How many do you want : "))
        print("Your total is = ",Answer_2*C, "ugx")


    elif Answer_1 == "4":
        print(Buys.dict1.get("books"))
        Answer_2 = int(input("How many do you want : ")) 
        print("Your total is = ",Answer_2*L, "ugx")

    elif Answer_1 == "5":
        print(Buys.dict1.get("bread"))
        Answer_2 = int(input("How many do you want : "))
        print("Your total is = ",Answer_2*B, "ugx")

    else:
        print("Sorry we don't have that in stock")    
    


print("thank you for shopping with us")
print("                                 ")

  # Game for user
def Game():
    print("would like to play a game, just for the fun of it?")
    Answer_4 = input("Yes/No \n :").upper()
    if Answer_4 == "YES" :
        print("knock ! Knock!! ")
        Answer_5 = input("Put in your answer \n :").lower()
        print("                    ")
        if Answer_5 == ("who's there?") or ("who is there?"): 
            print("                       ")
            print("Its the boogey man!!")
            print("\U0001F023 \U0001F023 \U0001F023  \U0001F023 \U0001F023 \U0001F023 \U0001F023 \U0001F023")
            print(".....................................................................................")

        elif Answer_5 != ("who's there?") or  ("who is there?"):
            print("That's not right try again")
        else:
            print("That's not possible") 
    elif Answer_4 == "NO" :
        print("Its always nice to have you at our store")
    else:
        print("its okay")

 # __name__

if __name__ == "__main__":
    Process()
    Game()
