
# coding: utf-8

# In[4]:


import random
name = ""
dict = {"a":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"A":11}
seq = ["a",'2','3','4','5','6','7','8','9','10',"J","Q","K"]
class PCard():
    global seq
    global dict
    global name
        
    def __init__(self):
        self.pcsum = 0
        self.pcard1 = 0
        self.pcard2 = 0
        
    def checkcard(self):
        if self.pcard1 == "a" and self.pcard2 != "a":  
            pcsum = dict[self.pcard2] + 11
            if pcsum < 22:
                self.pcard1 = "A"
        elif self.pcard1 != "a" and self.pcard2 == "a":    
            pcsum = dict[self.pcard1] + 11
            if pcsum < 22:
                self.pcard2 = "A"
        else:
              pass    
        
        
    def playercard(self):       
        pcard1 = random.choice(seq)
        self.pcard1 = pcard1
        pcard2 = random.choice(seq)
        self.pcard2 = pcard2
        self.checkcard()
        self.pcsum = dict[self.pcard1] + dict[self.pcard2]
        if self.pcsum == 21:
            print(f"your cards are {self.pcard1} and {self.pcard2}")
            print("your sum is 21")
            print(f"!!BlackJack!! {name} YOU WON")
            return
        elif self.pcsum > 21:
            print(f"your cards are {self.pcard1} and {self.pcard2}")
            print(f"your sum is {self.pcsum}")
            print("!!!You are Busted!!!")
            return
        else:   
            print(f"Your 2 cards are {pcard1} & {pcard2} and sum is {self.pcsum}")
            
            
    def phit(self):
        ecard = random.choice(seq)
        self.pcsum = self.pcsum + dict[ecard]  
        if self.pcsum == 21:
            print(f"your new card sum is {self.pcsum}")
            print(f"!!BlackJack!! {name} YOU WON")
            return
        elif self.pcsum > 21:
            print(f"your new card sum is {self.pcsum}")
            print("!!!You are Busted!!!")
            return
        else:
            print(f"New card is {ecard} and sum is {self.pcsum}")
            
 
    def pstand(self):
        print(f"plyer selected no New card so the sum is {self.pcsum}")


class DCard():
    global seq
    global dict
    
    def __init__(self):
        self.dcsum = 0
        self.dcard1 = 0
        self.dcard2 = 0   
        
    def checkdcard(self):
        dcsum=0
        if self.dcard1 == "a" and self.dcard2 != "a":   
            dcsum = dict[self.dcard2] + 11
            if dcsum < 22:
                self.dcard1 = "A"
            elif self.dcard1 != "a" and self.dcard2 == "a":  
                dcsum = dict[self.dcard1] + 11
                if dcsum < 22:
                    self.dcard2 = "A"
            else:
                pass            
    
    def dealercard(self): 
        dcard1 = random.choice(seq)
        self.dcard1 = dcard1
        dcard2 = random.choice(seq)
        self.dcard2 = dcard2
        self.checkdcard()
        self.dcsum = dict[self.dcard1] + dict[self.dcard2]
        print(f"Dealers first card is {dcard1}")      
 
        
    def showcard(self):
        self.checkdcard()
        print(f"Dealer 1st card was {self.dcard1} and 2nd card is {self.dcard2} and sum is {self.dcsum}")
        
    
    def dhit(self):
        ecard = random.choice(seq)
        if ecard == "a" and self.dcsum < 13:
            ecard = "A"
            self.dcsum = self.dcsum + dict[ecard]
        else:
            self.dcsum = self.dcsum + dict[ecard]
            print(f"New card is {ecard} and sum is {self.dcsum}")
        
        
    def dstand(self):
        print(f"no New card selected so the sum is {self.dcsum}")    
        
    
        


# In[5]:


def startgame():
    name = input("Enter name:")
    dccard = DCard()
    dccard.dealercard()
    print("\n")
    pccard = PCard()
    pccard.playercard()
    while pccard.pcsum < 21:
        print("What do want to do")
        choice = input("Enter 1 for hit,2 for stand")
        if choice == "1":
            pccard.phit()
            
        elif choice == "2":
            pccard.pstand()
            dccard.showcard()
            if dccard.dcsum == 21 and pccard.pcsum<22:
                print("!!Dealer WON")
                return
            elif dccard.dcsum > 21:
                print("!!!Dealer Busted you won!!!")
                return
            else:
                while dccard.dcsum < 17:
                    dccard.dhit()  
                dccard.dstand()
                if dccard.dcsum == 21 and pccard.pcsum!=21:
                    print("!!Dealer WON")
                    return
                elif dccard.dcsum > 21:
                    print("!!!Dealer Busted you won!!!")
                    return
                else:
                    if dccard.dcsum > pccard.pcsum:
                        print("!!Dealer WON")
                        return
                    elif dccard.dcsum == pccard.pcsum:    
                        print("!!its a tie")
                        return
                    else:
                        print("!!You WON")
                        return
                        
        
              


# In[ ]:


startgame()

