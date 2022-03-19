import random
from tkinter import END, Y

class Deck():
    def __init__(self):
        self.suit=['c','s','d','h']
        self.new_deck=[]
        self.number=['1','2','3','4','5','6','7','8','9','10','10','10','10']
        self.stay=''
        self.again=''
        
    def shuffle(self):
        self.stay='n'
        for suit in self.suit:
            for number in self.number:
                self.new_deck.append(f"{suit}:{number}")
        random.shuffle(self.new_deck)
        # print(self.new_deck)
        # print(len(self.new_deck))
        
        Deck.deal(self)
        # return self.new_deck

    def deal(self):
        self.cardd=[]
        self.cardp=[]         
        play=input("\n\nWould you like to play a game?\n")
        if play.lower()=="y":
            print("here we go!!\n")
        self.cardp.append(self.new_deck.pop())
        self.cardd.append(self.new_deck.pop())
        self.cardp.append(self.new_deck.pop())
        self.cardd.append(self.new_deck.pop())
        # print(self.cardp)
        # print(self.cardd)
        # print(len(self.new_deck))
        # print(self.new_deck)
        Deck.score(self)
       
    def score(self):
        res1=[]
        res2=[]
        # print('self stay',self.stay)
        self.scorep=0
        self.scored=0
        self.again=''
        i=0
        res1=[i[2:] for i in self.cardd]
        # print(type(res1[i]))
        for i in res1[i]:
            # print(res1)
            if int(i) == 1:
                print('Dealer has an Ace which can count as 1 or 11!!\n')
        self.scored=sum(list(map(int,res1)))
        
        i=0
        res2=[i[2:] for i in self.cardp]
        for i in res2[i]:
            # print(res2)
            if int(i) == 1:
                print('You have an Ace which can count as 1 or 11!!\n')
        self.scorep=sum(list(map(int,res2)))
        print("Player score:  ",(self.scorep))
        print("Player's Hand:  ",(self.cardp[0:]))
        print("Dealer is showing:  ",(self.cardd[0]))
        
        if self.scorep > 21:
            print("BUSTED, the casino's owners thank you!!  ")
            self.again=input("Would you like to play again?  ")
            if self.again.lower()=="y":
                Deck.run(play)

        if self.stay=='n':
            self.hit=input("Would you like another card?\n")
            if self.hit.lower()=='y':
                Deck.Hitmep(self)
            else:
                self.stay='y'
                Deck.Hitmed(self)
     
    def Hitmep(self):
        self.cardp.append(self.new_deck.pop())
        # print(self.cardp)
        Deck.score(self)

    def Hitmed(self):
        if self.scored < 17:
            self.cardd.append(self.new_deck.pop())
            print(self.cardd)
            Deck.score(self)

        elif self.scored>21:
            print("Dealer Busts!!")
            print("Players score: \n",self.scorep)
            print("Dealers score: \n",self.scored)
            self.again=input("Would you like to play again?")
            if self.again.lower()=="y":
                Deck.run(play)

        if self.scored > self.scorep and self.scored < 22:
            print("Dealer: ",self.cardp)
            print("Players score: ",self.scorep)
            print("Player: ",self.cardd)
            print("Dealers score: ",self.scored)
            print("Sorry loser!!\n")
            self.again=input("Would you like to play again?")
            if self.again.lower()=="y":
                Deck.run(play)
        else:
            print("Players score: \`n",self.scorep)
            print("Dealers score: \n",self.scored)
            print("You win!!!!\n")
            self.again=input("Would you like to play again?")
            if self.again.lower()=="y":
                Deck.run(play)
        
        self.again=input("Would you like to play again?")
        if self.again.lower()=="y":
            Deck.run(play)

    def run(self):
        Deck.shuffle(self)

play=Deck()
Deck.run(play)
