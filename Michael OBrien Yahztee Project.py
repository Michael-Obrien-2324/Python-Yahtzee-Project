import random
import sys


def inst(): # Gives instructions when called upon
    print('Welcome to the instructions. To leave press ENTER. To play yahtzee, each player gets three turns to roll the dice. After the first roll, the player can choose dice that they wish to save and re-roll the remaining dice. The process is repeated for the second turn, and any saved dice can be rerolled in the third turn. On the scorecard, there are thirteen slots in which a score can be recorded. After the third roll, the player must choose one of these categories in which to record their score for this turn. The amount of points received depends on the rules of the category that the turn was entered into. You may only put your score into the proper category. The dice needed for each category is listed during scoring.')
    n=input('\nPress ENTER to return to game or M to go back to the menu: ')
    if n=='M' or n=='m':
        menu()
        
def alldice():  # Rolls 5 dice at random
    r=random.randint(1,6)
    return r
    
def dice1():
    r=random.randint(1,6)
    dice[0]=r
    
def dice2():
    r=random.randint(1,6)
    dice[1]=r
    
def dice3():
    r=random.randint(1,6)
    dice[2]=r
    
def dice4():
    r=random.randint(1,6)
    dice[3]=r
    
def dice5():
    r=random.randint(1,6)
    dice[4]=r
    
def roll():
    for i in range(6):
        dice.append(alldice())
    print('Here is your first roll {}:'.format(names[j]),'\n',dice[0],dice[1],dice[2],dice[3],dice[4])

def reroll():   # Rerolls selected dice
    ro.append(input("Would you like to reroll dice 1?({})Enter y/n: ".format(dice[0])))
    if ro[0]=='y':
        dice1()
    ro.append(input("Would you like to reroll dice 2?({})Enter y/n: ".format(dice[1])))
    if ro[1]=='y':
        dice2()
    ro.append(input("Would you like to reroll dice 3?({})Enter y/n: ".format(dice[2])))
    if ro[2]=='y':
        dice3()
    ro.append(input("Would you like to reroll dice 4?({})Enter y/n: ".format(dice[3])))
    if ro[3]=='y':
        dice4()
    ro.append(input("Would you like to reroll dice 5?({})Enter y/n: ".format(dice[4])))
    if ro[4]=='y':
        dice5()

def org():  # Places player in rank order from highest points to least
    for j in range(players-1):
        for i in range(players-1):
            if score[i+1]>score[i]:
                big=score[i+1]
                bigname=order[i+1]
                score[i+1]=score[i]
                order[i+1]=order[i]
                score[i]=big
                order[i]=bigname
                
def rank(): # This functon displays current player rankings
    org()
    print('\nRight now...')
    check=len(set(score)) # "Tie" function added after assignment was due so "set" function allowed
    if check == players:
        for p in range(players):
            if p==0:
                print(order[p],'is in {}st place with {} points'.format(p+1,score[p]))
            elif p==1:
                print(order[p],'is in {}nd place with {} points'.format(p+1,score[p]))
            elif p==2:
                print(order[p],'is in {}rd place with {} points'.format(p+1,score[p]))
            else:
                print(order[p],'is in {}th place with {} points'.format(p+1,score[p]))
    else:
        print('There is a tie:')
        for i in range(players):
            print(order[i], " has {} points".format(score[i]))
    n=input('\nPress ENTER to return to game or M to go back to the menu: ')
    if n=='M' or n=='m':
        menu()
        
def end():  # Ends game
    print('Are you sure you want to quit?')
    i = input("Yes or No?: ")
    if i == 'Yes' or i == 'yes':
        sys.exit('You Quit the Game')
        
def menu(): # Opens menu tab
    print('\nYou are currently in the Menu tab. What would you like to access?')
    print('To view instructions, type "I" and press ENTER.')
    print('To see the current scores and rankings, type "R" and press ENTER.')
    print('To quit the game, type "Q" and press ENTER.')
    print('To leave Menu and continue game, press ENTER.')
    command=input('Enter command here: ')
    print(command)
    if command=='I' or command=='i':
        inst()
    elif command=='R' or command=='r':
        rank()
    elif command=='Q' or command=='q':
        end()
	
def combine(x): # Adds up total score with bonus
    n=x*13
    total=0
    for i in range(13):
        total+=points[n+i]
    total+=bonus[x]
    return total

def ace(x): # Scores aces section if able
    n=x*13
    if points[n]!=0:
        p=print('\nSorry you already used your aces space, try a different spot.')
        return -1
    else:
        for i in range(5):
            if dice[i]==1:
                points[n]+=1
        return points[n]
        
def two(x):# Scores twos section if able
    n=(x*13)+1
    if points[n]!=0:
        p=print('\nSorry you already used your twos space, try a different spot.')
        return -1
    else:
        for i in range(5):
            if dice[i]==2:
                points[n]+=2
        return points[n]
        
def three(x):# Scores threes section if able
    n=(x*13)+2
    if points[n]!=0:
        p=print('\nSorry you already used your threes space, try a different spot.')
        return -1
    else:
        for i in range(5):
            if dice[i]==3:
                points[n]+=3
        return points[n]
        
def four(x):# Scores fours section if able
    n=(x*13)+3
    if points[n]!=0:
        p=print('\nSorry you already used your fours space, try a different spot.')
        return -1
    else:
        for i in range(5):
            if dice[i]==4:
                points[n]+=4
        return points[n]
        
def five(x):# Scores fives section if able
    n=(x*13)+4
    if points[n]!=0:
        p=print('\nSorry you already used your fives space, try a different spot.')
        return -1
    else:
        for i in range(5):
            if dice[i]==5:
                points[n]+=5
        return points[n]
        
def six(x):# Scores sixes section if able
    n=(x*13)+5
    if points[n]!=0:
        p=print('\nSorry you already used your sixes space, try a different spot.')
        return -1
    else:
        for i in range(5):
            if dice[i]==6:
                points[n]+=6
        return points[n]
        
def tok(x):  # Scores Three of a Kind section if able
    n=(x*13)+6
    if points[n]!=0:
        p=print('\nSorry you already used your three of a kind space, try a different spot.')
        return -1
    else:
        for i in range(5):
            for j in range(4):
                if dice[j]<dice[j+1]:
                    b=dice[j+1]
                    dice[j+1]=dice[j]
                    dice[j]=b
        if dice[2]==dice[1]==dice[0] or dice[2]==dice[1]==dice[3]or dice[2]==dice[3]==dice[4]:
            k=dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
            points[n]=k
        else:
            h=input('You did not roll a three of a kind. Would you like to mark 0?("y") or pick a different spot("n")?: ')
            if h=='y':
                points[n]=0
            else:
                return -1
        return points[n]
        
def fok(x):     # Scores Four of a Kind section if able
    n=(x*13)+7
    if points[n]!=0:
        p=print('\nSorry you already used your four of a kind space, try a different spot.')
        return -1
    else:
        for i in range(5):
            for j in range(4):
                if dice[j]<dice[j+1]:
                    b=dice[j+1]
                    dice[j+1]=dice[j]
                    dice[j]=b
        if dice[0]==dice[1]==dice[2]==dice[3]or dice[1]==dice[2]==dice[3]==dice[4]:
            k=dice[0]+dice[1]+dice[2]+dice[3]+dice[4]
            points[n]=k
        else:
            h=input('You did not roll a four of a kind. Would you like to mark 0?("y") or pick a different spot("n")?: ')
            if h=='y':
                points[n]=0
            else:
                return -1
        return points[n]
        
def fullh(x):   # Scores Full House section if unused
    n=(x*13)+8
    if points[n]!=0:
        p=print('\nSorry you already used your full house space, try a different spot.')
        return -1
    else:
        for i in range(5):
            for j in range(4):
                if dice[j+1]>dice[j]:
                    b=dice[j+1]
                    l=dice[j]
                    dice[j+1]=l
                    dice[j]=b
        if dice[0]==dice[1]==dice[2] and dice[3]==dice[4]:
            points[n]=25
        elif dice[2]==dice[3]==dice[4] and dice[0]==dice[1]:
            points[n]=25
        else:
            h=input('You did not roll a full house. Would you like to mark 0?("y") or pick a different spot("n")?: ')
            if h=='y':
                points[n]=0
            else:
                return -1
        return points[n]
        
def smst(x):	# Scores Small straight section if able
    n=(x*13)+9
    if points[n]!=0:
        p=print('\nSorry you already used your small straight space, try a different spot.')
        return -1
    else:
        for i in range(5):
            for j in range(4):
                if dice[j]<dice[j+1]:
                    b=dice[j+1]
                    dice[j+1]=dice[j]
                    dice[j]=b
        if dice[0]==dice[1]+1==dice[2]+2==dice[3]+3 or dice[1]==dice[2]+1==dice[3]+2==dice[4]+3 or dice[0]==dice[1]+1==dice[2]+2==dice[3]+2==dice[4]+3 or dice[0]==dice[1]+1==dice[2]+1==dice[3]+2==dice[4]+3:
            points[n]=30
        else:
            h=input('You did not roll a small straight. Would you like to mark 0?("y") or pick a different spot("n")?: ')
            if h=='y':
                points[n]=0
            else:
                return -1
        return points[n]
        
def lst(x): 	# Scores Large straight section if able
    n=(x*13)+10
    if points[n]!=0:
        p=print('\nSorry you already used your large straight space, try a different spot.')
        return -1
    else:
        for i in range(5):
            for j in range(4):
                if dice[j]<dice[j+1]:
                    b=dice[j+1]
                    dice[j+1]=dice[j]
                    dice[j]=b
        if dice[0]==dice[1]+1==dice[2]+2==dice[3]+3==dice[4]+4:
            points[n]=40
        else:
            h=input('You did not roll a large straight. Would you like to mark 0?("y") or pick a different spot("n")?: ')
            if h=='y':
                points[n]=0
            else:
                return -1
        return points[n]
        
def yaht(x):	#Scores Yahtzee section
    n=(x*13)+11
    if dice[0]==dice[1]==dice[2]==dice[3]==dice[4]:
        if points[n]>=50:
            points[n]=points[n]+100
            return 100
        elif points[n]==0:
            points[n]+=50
            return 50
    else:
        h=input('You did not roll a yahtzee. Would you like to mark 0?("y") or pick a different spot("n")?: ')
        if h=='y':
            points[n]+=0
            return 0
        else:
            return -1

def chance(x):
    n=(x*13)+12
    if points[n]!=0:
        p=print('\nSorry you already used your chance space, try a different spot.')
        return -1
    else:
        k=0
        for i in range(5):
            k+=dice[i]
        points[n]+=k
        return points[n]
        
def place(j,c):
    while True:
        if c==1:
            k=ace(j)
            categ_name="Aces"
        elif c==2:
            k=two(j)
            categ_name="Twos"
        elif c==3:
            k=three(j)
            categ_name="Threes"
        elif c==4:
            k=four(j)
            categ_name="Fours"
        elif c==5:
            k=five(j)
            categ_name="Fives"
        elif c==6:
            k=six(j)
            categ_name="Sixes"
        elif c==7:
            k=tok(j)
            categ_name="Three of a Kind"
        elif c==8:
            k=fok(j)
            categ_name="Four of a Kind"
        elif c==9:
            k=fullh(j)
            categ_name="Full House"
        elif c==10:
            k=smst(j)
            categ_name="Small Straight"
        elif c==11:
            k=lst(j)
            categ_name="Large Straight"
        elif c==12:
            k=yaht(j)
            categ_name="Yahtzee"
        elif c==13:
            k=chance(j)
            categ_name="Chance"
        if k!=-1:
            break
        elif k==-1:
            num=c
            while True:
                c = int(input('Choose again: '))
                if c>0 and c<14 and c!=num:
                    break
    return k, categ_name

#Start of the game is below
print('Welcome to Yahtzee')
players=int(input('How many players will be playing?: '))
names=[]
score=[]
points=[]
order=[]
bonus=[]
ro=[]
for j in range(players):
    n=j+1
    name=input('Enter name of player {} here: '.format(n))
    names.append(name)
    order.append(name)
    score.append(0)
    bonus.append(0)
    for i in range(13):
        points.append(0)

n=input('To access Menu and more, type "M". To begin the game press ENTER: ')
if n=="M" or n=='m':
    menu()


for i in range(13): #There are 13 rounds in yahtzee
    for j in range(players): #This will give each player a turn in each round
        n=input("\nIt is now {}'s turn. To access Menu, type 'M', press ENTER to roll: ".format(names[j]))
        if n=='M' or n=='m':
            menu()
        n=j*13
        print("{}'s Scoreboard:".format(names[j]))
        print('    Aces      | - {} points'.format(points[n]))
        print('    Twos      | - {} points'.format(points[n+1]))
        print('    Threes    | - {} points'.format(points[n+2]))
        print('    Fours     | - {} points'.format(points[n+3]))
        print('    Fives     | - {} points'.format(points[n+4]))
        print('    Sixes     | - {} points'.format(points[n+5]))
        print('--------------------------')
        print('    Bonus     | - {} points'.format(bonus[j]))
        print('--------------------------')
        print(' 3 of a Kind  | - {} points'.format(points[n+6]))
        print(' 4 of a Kind  | - {} points'.format(points[n+7]))
        print('  Full House  | - {} points'.format(points[n+8]))
        print('Small Straight| - {} points'.format(points[n+9]))
        print('Large Straight| - {} points'.format(points[n+10]))
        print('   Yahtzee    | - {} points'.format(points[n+11]))
        print('    Chance    | - {} points'.format(points[n+12]))
        dice=[]
        roll()
        ro=[]
        reroll()
        if ro[0]=='y' or ro[1]=='y' or ro[2]=='y' or ro[3]=='y' or ro[4]=='y':
            print('Here is your second roll {}:\n'.format(names[j]),dice[0],dice[1],dice[2],dice[3],dice[4])
            ro=[]
            reroll()
            if ro[0]=='y' or ro[1]=='y' or ro[2]=='y' or ro[3]=='y' or ro[4]=='y':
            	print('Here is your third roll:\n',dice[0],dice[1],dice[2],dice[3],dice[4])
                #print('Where would you like to score this roll {}?'.format(names[j]))
        print('\nWhere would you like to score this roll {}?\n\nYour roll was '.format(names[j]),dice[0],dice[1],dice[2],dice[3],dice[4])
        #c=int(input('Here are your options:\n\nUpper Section:\nAces-Score is the sum of all dice with number "1"-type "1"\nTwos-Score is the sum of all dice with number "2"-type "2"\nThrees-Score is the sum of all dice with number "3"-type "3"\nFours-Score is the sum of all dice with number "4"-type "4"\nFives-Score is the sum of all dice with number "5"-type "5"\nSixes-Score is the sum of all dice with number "6"-type "6"\n\nLower Section:\n3 of a Kind-Sums up all dice when there are 3 of one type-type "7"\n4 of a Kind-Sums up all dice when there are 4 of a type-type "8"\nFull House-Scores 25 if there are 3 of one kind and two of another-type "9"\nSmall Straight-At least four consecutive dice, scores 30-type "10"\nLarge Straight-ALl five dice consecutive, scores 40-type "11"\nYahtzee-All Five dice the same number, scores 50-type "12"\nChance-Sum of all dice-type "13"\nEnter here: '))
        #pick(j)
        n=j*13
        a1='\nAces(type "1")-Score is the sum of all dice with number "1"               | - {} points'.format(points[n])
        b1='\nTwos(type "2")-Score is the sum of all dice with number "2"               | - {} points'.format(points[n+1])
        c1='\nThrees(type "3")-Score is the sum of all dice with number "3"             | - {} points'.format(points[n+2])
        d1='\nFours(type "4")-Score is the sum of all dice with number "4"              | - {} points'.format(points[n+3])
        e1='\nFives(type "5")-Score is the sum of all dice with number "5"              | - {} points'.format(points[n+4])
        f1='\nSixes(type "6")-Score is the sum of all dice with number "6"              | - {} points'.format(points[n+5])
        g1='\n3 of a Kind(type "7")-Sums up all dice when there are 3 of one type       | - {} points'.format(points[n+6])
        h1='\n4 of a Kind(type "8")-Sums up all dice when there are 4 of a type         | - {} points'.format(points[n+7])
        i1='\nFull House(type "9")-Scores 25 if there are 3 of one kind and 2 of another| - {} points'.format(points[n+8])
        j1='\nSmall Straight(type "10")-At least four consecutive dice, scores 30       | - {} points'.format(points[n+9])
        k1='\nLarge Straight(type "11")-ALl five dice consecutive, scores 40            | - {} points'.format(points[n+10])
        l1='\nYahtzee(type "12")-All Five dice the same number, scores 50               | - {} points'.format(points[n+11])
        m1='\nChance(type "13")-Sum of all dice                                         | - {} points'.format(points[n+12])
        comb=points[n]+points[n+1]+points[n+2]+points[n+3]+points[n+4]+points[n+5]
        if comb>=63:
            bonus[j]=35
        c=int(input('Here are your options:\n\nUpper Section:{}{}{}{}{}{}\n\nCombined Upper Score:{} points\nUpper Section Bonus-35 points:If combined upper score is at least 63 points-{} points\n\nLower Section:{}{}{}{}{}{}{}\nEnter here: '.format(a1,b1,c1,d1,e1,f1,comb,bonus[j],g1,h1,i1,j1,k1,l1,m1)))
        while True:
            if c>0 and c<14:
                break
            else:
                c = int(input('{} is not a valid option. Choose again: '.format(c)))
        ThisRound,categ_name = place(j,c)
        score[j]=combine(j)
        print('You scored {} points in the {} section'.format(ThisRound,categ_name))
        n=input("Your turn has ended. To access Menu, type 'M', press ENTER to continue: ")
        if n=='M':
            menu()
    	
    	
org()
print('\nFinal Results are...')
check=len(set(score)) #"Tie" function added after assignment was due so "set" function allowed
if check == players:
    for i in range(players):
        if i==0:
            print(order[i],'won the game with {} points. Congrats {}!'.format(score[i],order[i]))
        elif i==1:
            print(order[i],'was in {}nd place with {} points'.format(i+1,score[i]))
        elif i==2:
            print(order[i],'was in {}rd place with {} points'.format(i+1,score[i]))
        else:
            print(order[i],'was in {}th place with {} points'.format(i+1,score[i]))
else:
    if score[0]==score[1]:
        print('There was a tie!')
    print('\nFinal scores:\n')
    for i in range(players):
        print(order[i], "- {} points".format(score[i]))
print('Thanks for playing!')
#print(score, bonus,points)