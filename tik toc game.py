a, b, c, d, e, f, g, h, i = " ", " ", " ", " ", " ", " ", " ", " ", " "
from os import system,name
from time import sleep

def clear():
    if name == 'nt':
        _ = system('cls')
        sleep(0.5)
        print(" \n"*20)


def start_game():
    print("     |     |    ")
    print("  {}  |  {}  |  {}  ".format(g,h,i))
    print("     |     |    ")
    print("-"*18)
    print("     |     |    ")
    print("  {}  |  {}  |  {}  ".format(d,e,f))
    print("     |     |    ")
    print("-"*18)
    print("     |     |    ")
    print("  {}  |  {}  |  {}  ".format(a,b,c))
    print("     |     |    ")

def place_valuefx(arg):
    global a,b,c,d,e,f,g,h,i
    if arg==1:
        if a!="X" and a!="O":
            a="X"
            clear()
            start_game()
        else:
            return False
            
    elif arg==2:
        if b!="X" and b!="O":
            b="X"
            clear()
            start_game()
        else:
            return False
            
    elif arg==3: 
        if c!="X" and c!="O":
            c="X"
            clear()
            start_game()
        else:
            return False
    
    elif arg==4:
        if d!="X" and d!="O":
            d="X"
            clear()
            start_game()
        else:
            return False
            
    elif arg==5: 
        if e!="X" and e!="O":
            e="X"
            clear()
            start_game()
        else:
            return False
            
    elif arg==6:
        if f!="X" and f!="O":
            f="X"
            clear()
            start_game()
        else:
            return False
            
    elif arg==7:
        if g!="X" and g!="O":
            g="X"
            clear()
            start_game()
        else:
            return False
            
    elif arg==8:
        if h!="X" and h!="O":
            h="X"
            clear()
            start_game()
        else:
            return False
            
    elif arg==9:
        if i!="X" and i!="O":
            i="X"
            clear()
            start_game()    
        else:
            return False
           
    else:
        print("Enter valid number")  
        
def place_valuefo(arg):
    global a,b,c,d,e,f,g,h,i
    if arg==1:
        if a!="X" and a!="O":
            a="O"
            clear()
            start_game()
        else:
            return False
                    
    elif arg==2:
        if b!="X" and b!="O":
            b="O"
            clear()
            start_game()
        else:
            return False
                   
    elif arg==3: 
        if c!="X" and c!="O":
            c="O"
            clear()
            start_game()
        else:
            return False
                   
    elif arg==4:
        if d!="X" and d!="O":
            d="O"
            clear()
            start_game()
        else:
            return False
                   
    elif arg==5: 
        if a!="X" and e!="O":
            e="O"
            clear()
            start_game()
        else:
            return False
                   
    elif arg==6:
        if f!="X" and f!="O":
            f="O"
            clear()
            start_game()
        else:
            return False
                   
    elif arg==7:
        if g!="X" and g!="O":
            g="O"
            clear()
            start_game()
        else:
            return False
                   
    elif arg==8:
        if h!="X" and h!="O":
            h="O"
            clear()
            start_game()
        else:
            return False
                   
    elif arg==9:
        if i!="X" and i!="O":
            i="O"
            clear()
            start_game()
        else:
            return False
                   
    else:
        print("Enter valid number")            
        
def c_win():
    global a,b,c,d,e,f,g,h,i,win
    if a==b==c:
        if a.strip() != "":
            print("Player with symbol {} wins.".format(a))
            return True 
    elif d==e==f:
        if d.strip() != "":
            print("Player with symbol {} wins.".format(d))
            return True
    elif g==h==i:
        if g.strip() != "":
            print("Player with symbol {} wins.".format(g))
            return True
    elif a==d==g:
        if a.strip() != "":
            print("Player with symbol {} wins.".format(a))
            return True
    elif c==f==i:
        if c.strip() != "":
            print("Player with symbol {} wins.".format(c))
            return True
    elif c==e==g:
        if c.strip() != "":
            print("Player with symbol {} wins.".format(c))
            return True
    elif b==e==h:
        if b.strip() != "":
            print("Player with symbol {} wins.".format(b)) 
            return True
    elif  a==e==i:
        if a.strip() != "":
            print("Player with symbol {} wins.".format(a))
            return True
    else:
        return False


def play_game():    
    print("Do you want to start game type 1 for 'Yes' or 2 for 'No':")
    play = int(input())
    chanceoff = True
    def get_input():
        global a,b,c,d,e,f,g,h,i
        print("Put capslock on")
        symbol = input("What do you want to be firt player symbol X or O:")
        if symbol == "X":
            chanceoff = True
            chanceofs = False
        elif symbol == "O" :
            chanceoff = False
            chanceofs = True
        else:
             print("Enter valid symbol")
             play_game() 

        while True:
            while chanceoff:
                place = int(input("Enter place :"))
                print("\n")
                if place_valuefx(place)== False:
                    print("Dont overwrite:")
                    continue
                chanceofs = True
                chanceoff = False
                if c_win() == True:
                    return
                break

            while chanceofs:
                place = int(input("Enter place :"))
                print("\n")
                if place_valuefo(place) == False:
                    print("Dont overwrite:")
                    continue
                chanceoff = True
                chanceofs = False    
                if c_win() == True:
                    return
                break
    if play == 1:
        get_input()
    else: 
        print("Hope to see you next time")

play_game()




