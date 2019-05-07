import time as t
import random as r
endGame=False
square1=int(0)
square2=int(0)
square3=int(0)
square4=int(0)
square5=int(0)
square6=int(0)
square7=int(0)
square8=int(0)
square9=int(0)
noughtsWin=False
crossesWin=False
def calculateWin():
    global square1
    global square2
    global square3
    global square4
    global square5
    global square6
    global square7
    global square8
    global square9
    global endGame
    global noughtsWin
    global crossesWin
    print("Thats the end of the game!")
    print("And the winner is...")
    t.sleep(r.randint(5,10))
    if square1==1:
        if square2==1:
            if square3==1:
                crossesWin=True
        if square4==1:
            if square7==1:
                crossesWin=True
        if square5==1:
            if square9==1:
                crossesWin=True
    if square2==1:
        if square5==1:
            if square8==1:
                crossesWin=True
    if square3==1:
        if square6==1:
            if square9==1:
                crossesWin=True
        if square5==1:
            if square7==1:
                crossesWin=True
    if square4==1:
        if square5==1:
            if square6==1:
                crossesWin=True
    if square7==1:
        if square8==1:
            if square9==1:
                crossesWin=True
    if square1==2:
        if square2==2:
            if square3==2:
                noughtsWin=True
        if square4==2:
            if square7==2:
                noughtsWin=True
        if square5==2:
            if square9==2:
                noughtsWin=True
    if square2==2:
        if square5==2:
            if square8==2:
                noughtsWin=True
    if square3==2:
        if square6==2:
            if square9==2:
                noughtsWin=True
        if square5==2:
            if square7==2:
                noughtsWin=True
    if square4==2:
        if square5==2:
            if square6==2:
                noughtsWin=True
    if square7==2:
        if square8==2:
            if square9==2:
                noughtsWin=True
    if noughtsWin==True and crossesWin==True:
        print("It's a draw!")
        endGame=True
    if noughtsWin!=True and crossesWin==True:
        print("Crosses!")
        endGame=True
    if noughtsWin==True and crossesWin!=True:
        print("Noughts!")
        endGame=True
    

    
while True:    
    if endGame==False:
        if square1==0:
            if square2==0:
                if square3==0:
                    print("1        |2        |3        ")
                    print("         |         |         ")
                    print("         |         |         ")
                    print("         |         |         ")
                    print("         |         |         ")
                    print("-----------------------------")
        if square4==0:
            if square5==0:
                if square6==0:
                    print("4        |5        |6        ")
                    print("         |         |         ")
                    print("         |         |         ")
                    print("         |         |         ")
                    print("         |         |         ")
                    print("-----------------------------")
        if square7==0:
            if square8==0:
                if square9==0:
                    print("7        |8        |9        ")
                    print("         |         |         ")
                    print("         |         |         ")
                    print("         |         |         ")
                    print("         |         |         ")
        crossesChoise=input("Crosses, which square do you choose?")
        crossesChoise=int(crossesChoise)
        playGame()
        noughtsChoise=input("Noughts, which square do you choose?")
        noughtsChoise=int(noughtsChoise)
        playGame()


    def playGame():
        global square1
        global square2
        global square3
        global square4
        global square5
        global square6
        global square7
        global square8
        global square9
        global endGame
        global noughtsWin
        global crossesWin
        if crossesChoise==1:
            square1=int(1)
        if crossesChoise==2:
            square2=int(1)
        if crossesChoise==3:
            square3=int(1)
        if crossesChoise==4:
            square4=int(1)
        if crossesChoise==5:
            square5=int(1)
        if crossesChoise==6:
            square6=int(1)
        if crossesChoise==7:
            square7=int(1)
        if crossesChoise==8:
            square8=int(1)
        if crossesChoise==9:
            square9=int(1)
        if noughtsChoise==1:
            square1=int(2)
        if noughtsChoise==2:
            square2=int(2)
        if noughtsChoise==3:
            square3=int(2)
        if noughtsChoise==4:
            square4=int(2)
        if noughtsChoise==5:
            square5=int(2)
        if noughtsChoise==6:
            square6=int(2)
        if noughtsChoise==7:
            square7=int(2)
        if noughtsChoise==8:
            square8=int(2)
        if noughtsChoise==9:
            square9=int(2)

        if square1!=0:
            if square2!=0:
                if square3!=0:
                    if square4!=0:
                        if square5!=0:
                            if square6!=0:
                                if square7!=0:
                                    if square8!=0:
                                        if square9!=0:
                                            calculateWin()

        if square1==1:
            if square2==1:
                if square3==1:
                    print("1        |2        |3        ")
                    print("  o   o  |  o   o  |  o   o  ")
                    print("    o    |    o    |    o    ")
                    print("  o   o  |  o   o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==0:
                    print("1        |2        |3        ")
                    print("  o   o  |  o   o  |         ")
                    print("    o    |    o    |         ")
                    print("  o   o  |  o   o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3 == 2:
                    print("1        |2        |3        ")
                    print("  o   o  |  o   o  |  o o o  ")
                    print("    o    |    o    |  o   o  ")
                    print("  o   o  |  o   o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square2==0:
                if square3==1:
                    print("1        |2        |3        ")
                    print("  o   o  |         |  o   o  ")
                    print("    o    |         |    o    ")
                    print("  o   o  |         |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==0:
                    print("1        |2        |3        ")
                    print("  o   o  |         |         ")
                    print("    o    |         |         ")
                    print("  o   o  |         |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==2:
                    print("1        |2        |3        ")
                    print("  o   o  |         |  o o o  ")
                    print("    o    |         |  o   o  ")
                    print("  o   o  |         |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square2==2:
                if square3==0:
                    print("1        |2        |3        ")
                    print("  o   o  |  o o o  |         ")
                    print("    o    |  o   o  |         ")
                    print("  o   o  |  o o o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==1:
                    print("1        |2        |3        ")
                    print("  o   o  |  o o o  |  o   o  ")
                    print("    o    |  o   o  |    o    ")
                    print("  o   o  |  o o o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==2:
                    print("1        |2        |3        ")
                    print("  o   o  |  o o o  |  o o o  ")
                    print("    o    |  o   o  |  o   o  ")
                    print("  o   o  |  o o o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")                        
        if square1==2:
            if square2==2:
                if square3==2:
                    print("1        |2        |3        ")
                    print("  o o o  |  o o o  |  o o o  ")
                    print("  o   o  |  o   o  |  o   o  ")
                    print("  o o o  |  o o o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==0:
                    print("1        |2        |3        ")
                    print("  o o o  |  o o o  |         ")
                    print("  o   o  |  o   o  |         ")
                    print("  o o o  |  o o o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==1:
                    print("1        |2        |3        ")
                    print("  o o o  |  o o o  |  o   o  ")
                    print("  o   o  |  o   o  |    o    ")
                    print("  o o o  |  o o o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square2==0:
                if square3==2:
                    print("1        |2        |3        ")
                    print("  o o o  |         |  o o o  ")
                    print("  o   o  |         |  o   o  ")
                    print("  o o o  |         |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==0:
                    print("1        |2        |3        ")
                    print("  o o o  |         |         ")
                    print("  o   o  |         |         ")
                    print("  o o o  |         |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==1:
                    print("1        |2        |3        ")
                    print("  o o o  |         |  o   o  ")
                    print("  o   o  |         |    o    ")
                    print("  o o o  |         |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square2==1:
                if square3==2:
                    print("1        |2        |3        ")
                    print("  o o o  |  o   o  |  o o o  ")
                    print("  o   o  |    o    |  o   o  ")
                    print("  o o o  |  o   o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==0:
                    print("1        |2        |3        ")
                    print("  o o o  |  o   o  |         ")
                    print("  o   o  |    o    |         ")
                    print("  o o o  |  o   o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3==1:
                    print("1        |2        |3        ")
                    print("  o o o  |  o   o  |  o   o  ")
                    print("  o   o  |    o    |    o    ")
                    print("  o o o  |  o   o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")                            
        if square1 == 0:
            if square2 == 0:
                if square3 == 1:
                    print("1        |2        |3        ")
                    print("         |         |  o   o  ")
                    print("         |         |    o    ")
                    print("         |         |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3 == 2:
                    print("1        |2        |3        ")
                    print("         |         |  o o o  ")
                    print("         |         |  o   o  ")
                    print("         |         |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square2 == 1:
                if square3 == 1:
                    print("1        |2        |3        ")
                    print("         |  o   o  |  o   o  ")
                    print("         |    o    |    o    ")
                    print("         |  o   o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3 == 2:
                    print("1        |2        |3        ")
                    print("         |  o   o  |  o o o  ")
                    print("         |    o    |  o   o  ")
                    print("         |  o   o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3 == 0:
                    print("1        |2        |3        ")
                    print("         |  o   o  |         ")
                    print("         |    o    |         ")
                    print("         |  o   o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square2 == 2:
                if square3 == 1:
                    print("1        |2        |3        ")
                    print("         |  o o o  |  o   o  ")
                    print("         |  o   o  |    o    ")
                    print("         |  o o o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3 == 2:
                    print("1        |2        |3        ")
                    print("         |  o o o  |  o o o  ")
                    print("         |  o   o  |  o   o  ")
                    print("         |  o o o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square3 == 0:
                    print("1        |2        |3        ")
                    print("         |  o o o  |         ")
                    print("         |  o   o  |         ")
                    print("         |  o o o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")

        if square4==1:
            if square5==1:
                if square6==1:
                    print("4        |5        |6        ")
                    print("  o   o  |  o   o  |  o   o  ")
                    print("    o    |    o    |    o    ")
                    print("  o   o  |  o   o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==0:
                    print("4        |5        |6        ")
                    print("  o   o  |  o   o  |         ")
                    print("    o    |    o    |         ")
                    print("  o   o  |  o   o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==2:
                    print("4        |5        |6        ")
                    print("  o   o  |  o   o  |  o o o  ")
                    print("    o    |    o    |  o   o  ")
                    print("  o   o  |  o   o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square5==0:
                if square6==1:
                    print("4        |5        |6        ")
                    print("  o   o  |         |  o   o  ")
                    print("    o    |         |    o    ")
                    print("  o   o  |         |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==0:
                    print("4        |5        |6        ")
                    print("  o   o  |         |         ")
                    print("    o    |         |         ")
                    print("  o   o  |         |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==2:
                    print("4        |5        |6        ")
                    print("  o   o  |         |  o o o  ")
                    print("    o    |         |  o   o  ")
                    print("  o   o  |         |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square5==2:
                if square6==0:
                    print("4        |5        |6        ")
                    print("  o   o  |  o o o  |         ")
                    print("    o    |  o   o  |         ")
                    print("  o   o  |  o o o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==1:
                    print("4        |5        |6        ")
                    print("  o   o  |  o o o  |  o   o  ")
                    print("    o    |  o   o  |    o    ")
                    print("  o   o  |  o o o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==2:
                    print("4        |5        |6        ")
                    print("  o   o  |  o o o  |  o o o  ")
                    print("    o    |  o   o  |  o   o  ")
                    print("  o   o  |  o o o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")                        
        if square4==2:
            if square5==2:
                if square6==2:
                    print("4        |5        |6        ")
                    print("  o o o  |  o o o  |  o o o  ")
                    print("  o   o  |  o   o  |  o   o  ")
                    print("  o o o  |  o o o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==0:
                    print("4        |5        |6        ")
                    print("  o o o  |  o o o  |         ")
                    print("  o   o  |  o   o  |         ")
                    print("  o o o  |  o o o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==1:
                    print("4        |5        |6        ")
                    print("  o o o  |  o o o  |  o   o  ")
                    print("  o   o  |  o   o  |    o    ")
                    print("  o o o  |  o o o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square5==0:
                if square6==2:
                    print("4        |5        |6        ")
                    print("  o o o  |         |  o o o  ")
                    print("  o   o  |         |  o   o  ")
                    print("  o o o  |         |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==0:
                    print("4        |5        |6        ")
                    print("  o o o  |         |         ")
                    print("  o   o  |         |         ")
                    print("  o o o  |         |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==1:
                    print("4        |5        |6        ")
                    print("  o o o  |         |  o   o  ")
                    print("  o   o  |         |    o    ")
                    print("  o o o  |         |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square5==1:
                if square6==2:
                    print("4        |5        |6        ")
                    print("  o o o  |  o   o  |  o o o  ")
                    print("  o   o  |    o    |  o   o  ")
                    print("  o o o  |  o   o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==0:
                    print("4        |5        |6        ")
                    print("  o o o  |  o   o  |         ")
                    print("  o   o  |    o    |         ")
                    print("  o o o  |  o   o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==1:
                    print("4        |5        |6        ")
                    print("  o o o  |  o   o  |  o   o  ")
                    print("  o   o  |    o    |    o    ")
                    print("  o o o  |  o   o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")                            
        if square4==0:
            if square5==0:
                if square6==1:
                    print("4        |5        |6        ")
                    print("         |         |  o   o  ")
                    print("         |         |    o    ")
                    print("         |         |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==2:
                    print("4        |5        |6        ")
                    print("         |         |  o o o  ")
                    print("         |         |  o   o  ")
                    print("         |         |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square5==1:
                if square6 == 1:
                    print("4        |5        |6        ")
                    print("         |  o   o  |  o   o  ")
                    print("         |    o    |    o    ")
                    print("         |  o   o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==2:
                    print("4        |5        |6        ")
                    print("         |  o   o  |  o o o  ")
                    print("         |    o    |  o   o  ")
                    print("         |  o   o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==0:
                    print("4        |5        |6        ")
                    print("         |  o   o  |         ")
                    print("         |    o    |         ")
                    print("         |  o   o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")
            if square5==2:
                if square6==1:
                    print("4        |5        |6        ")
                    print("         |  o o o  |  o   o  ")
                    print("         |  o   o  |    o    ")
                    print("         |  o o o  |  o   o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==2:
                    print("4        |5        |6        ")
                    print("         |  o o o  |  o o o  ")
                    print("         |  o   o  |  o   o  ")
                    print("         |  o o o  |  o o o  ")
                    print("         |         |         ")
                    print("-----------------------------")
                if square6==0:
                    print("4        |5        |6        ")
                    print("         |  o o o  |         ")
                    print("         |  o   o  |         ")
                    print("         |  o o o  |         ")
                    print("         |         |         ")
                    print("-----------------------------")

        if square7==1:
            if square8==1:
                if square9==1:
                    print("7        |8        |9        ")
                    print("  o   o  |  o   o  |  o   o  ")
                    print("    o    |    o    |    o    ")
                    print("  o   o  |  o   o  |  o   o  ")
                    print("         |         |         ")
                if square9==0:
                    print("7        |8        |9        ")
                    print("  o   o  |  o   o  |         ")
                    print("    o    |    o    |         ")
                    print("  o   o  |  o   o  |         ")
                    print("         |         |         ")
                if square9==2:
                    print("7        |8        |9        ")
                    print("  o   o  |  o   o  |  o o o  ")
                    print("    o    |    o    |  o   o  ")
                    print("  o   o  |  o   o  |  o o o  ")
                    print("         |         |         ")
            if square8==0:
                if square9==1:
                    print("7        |8        |9        ")
                    print("  o   o  |         |  o   o  ")
                    print("    o    |         |    o    ")
                    print("  o   o  |         |  o   o  ")
                    print("         |         |         ")
                if square9==0:
                    print("7        |8        |9        ")
                    print("  o   o  |         |         ")
                    print("    o    |         |         ")
                    print("  o   o  |         |         ")
                    print("         |         |         ")
                if square9==2:
                    print("7        |8        |9        ")
                    print("  o   o  |         |  o o o  ")
                    print("    o    |         |  o   o  ")
                    print("  o   o  |         |  o o o  ")
                    print("         |         |         ")
            if square8==2:
                if square9==0:
                    print("7        |8        |9        ")
                    print("  o   o  |  o o o  |         ")
                    print("    o    |  o   o  |         ")
                    print("  o   o  |  o o o  |         ")
                    print("         |         |         ")
                if square9==1:
                    print("7        |8        |9        ")
                    print("  o   o  |  o o o  |  o   o  ")
                    print("    o    |  o   o  |    o    ")
                    print("  o   o  |  o o o  |  o   o  ")
                    print("         |         |         ")
                if square9==2:
                    print("7        |8        |9        ")
                    print("  o   o  |  o o o  |  o o o  ")
                    print("    o    |  o   o  |  o   o  ")
                    print("  o   o  |  o o o  |  o o o  ")
                    print("         |         |         ")                       
        if square7==2:
            if square8==2:
                if square9==2:
                    print("7        |8        |9        ")
                    print("  o o o  |  o o o  |  o o o  ")
                    print("  o   o  |  o   o  |  o   o  ")
                    print("  o o o  |  o o o  |  o o o  ")
                    print("         |         |         ")
                if square9==0:
                    print("7        |8        |9        ")
                    print("  o o o  |  o o o  |         ")
                    print("  o   o  |  o   o  |         ")
                    print("  o o o  |  o o o  |         ")
                    print("         |         |         ")
                if square9==1:
                    print("7        |8        |9        ")
                    print("  o o o  |  o o o  |  o   o  ")
                    print("  o   o  |  o   o  |    o    ")
                    print("  o o o  |  o o o  |  o   o  ")
                    print("         |         |         ")
            if square8==0:
                if square9==2:
                    print("7        |8        |9        ")
                    print("  o o o  |         |  o o o  ")
                    print("  o   o  |         |  o   o  ")
                    print("  o o o  |         |  o o o  ")
                    print("         |         |         ")
                if square9==0:
                    print("7        |8        |9        ")
                    print("  o o o  |         |         ")
                    print("  o   o  |         |         ")
                    print("  o o o  |         |         ")
                    print("         |         |         ")
                if square9==1:
                    print("7        |8        |9        ")
                    print("  o o o  |         |  o   o  ")
                    print("  o   o  |         |    o    ")
                    print("  o o o  |         |  o   o  ")
                    print("         |         |         ")
            if square8==1:
                if square9==2:
                    print("7        |8        |9        ")
                    print("  o o o  |  o   o  |  o o o  ")
                    print("  o   o  |    o    |  o   o  ")
                    print("  o o o  |  o   o  |  o o o  ")
                    print("         |         |         ")
                if square9==0:
                    print("7        |8        |9        ")
                    print("  o o o  |  o   o  |         ")
                    print("  o   o  |    o    |         ")
                    print("  o o o  |  o   o  |         ")
                    print("         |         |         ")
                if square9==1:
                    print("7        |8        |9        ")
                    print("  o o o  |  o   o  |  o   o  ")
                    print("  o   o  |    o    |    o    ")
                    print("  o o o  |  o   o  |  o   o  ")
                    print("         |         |         ")                           
        if square7==0:
            if square8==0:
                if square9==1:
                    print("7        |8        |9        ")
                    print("         |         |  o   o  ")
                    print("         |         |    o    ")
                    print("         |         |  o   o  ")
                    print("         |         |         ")
                if square9==2:
                    print("7        |8        |9        ")
                    print("         |         |  o o o  ")
                    print("         |         |  o   o  ")
                    print("         |         |  o o o  ")
                    print("         |         |         ")
            if square8==1:
                if square9==1:
                    print("7        |8        |9        ")
                    print("         |  o   o  |  o   o  ")
                    print("         |    o    |    o    ")
                    print("         |  o   o  |  o   o  ")
                    print("         |         |         ")
                if square9==2:
                    print("7        |8        |9        ")
                    print("         |  o   o  |  o o o  ")
                    print("         |    o    |  o   o  ")
                    print("         |  o   o  |  o o o  ")
                    print("         |         |         ")
                if square9==0:
                    print("7        |8        |9        ")
                    print("         |  o   o  |         ")
                    print("         |    o    |         ")
                    print("         |  o   o  |         ")
                    print("         |         |         ")
            if square8==2:
                if square9==1:
                    print("7        |8        |9        ")
                    print("         |  o o o  |  o   o  ")
                    print("         |  o   o  |    o    ")
                    print("         |  o o o  |  o   o  ")
                    print("         |         |         ")
                if square9==2:
                    print("7        |8        |9        ")
                    print("         |  o o o  |  o o o  ")
                    print("         |  o   o  |  o   o  ")
                    print("         |  o o o  |  o o o  ")
                    print("         |         |         ")
                if square9==0:
                    print("7        |8        |9        ")
                    print("         |  o o o  |         ")
                    print("         |  o   o  |         ")
                    print("         |  o o o  |         ")
                    print("         |         |         ")

               
            
                

    
                
                
                

    
    
        
    
    
    
