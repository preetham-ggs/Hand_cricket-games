# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 18:35:21 2021

@author: user
"""
import random

print('''Hello guys ! Let's know the rules !
      First u will input your balls for each team.
      This is to set the length of ur game.
      Wickets will be balls//6 + 1.
      Eg: 25 balls -> 25//6+ 1 -> 4+1 ->5
      Second u will input your opponent's and your team name.
      Read whether you will be batting or bowling first.
      Bowling:
          U will type a number from 0 to 6 as input.
          If your symbol matches with the computer's symbol,
          you will get a wicket. If u get all of them, computer will be all out.
          If they don't match, the symbol computer enters will add up in its' runs tally.
          If you are bowling second, restrict the computer from reaching your runs scored in the 1st innings, to win.
      Batting:
          U will type a number from 0 to 6 as input.
          If your symbol matches with computer's symbol, you will lose a wicket.
          Remember you have only 5 of them.
          If they don't match, the symbol you enter will be assed in your runs tally.
          If batting second, score more than what the computer scored in the first innings, to win'
      If your score and the computer's scores are level at the end of the game, it is a TIE.
      Alert: Do not enter number less than 0 or greater than 6. Else it  will show Invalid Input.
      HAVE A NICE TIME !!! 🤗'         
      ''')
r=int(input("Enter your balls per innings limit:"))
q=r//6 + 1
print("you have {} balls per innings".format(r))
print("each side has {} wickets".format(q))
toss=['H','T']
a_n=input('Name of your opponent team/player:')
b_n=input('Name of your team/player:')
print("Time for toss.")
x=random.choice(toss)
y=input('H or T ?')
if(x==y):
    print(" You won the toss. Choose even number to bowl and odd number to bat.")
    m=int(input("Your number"))
if(x!=y):
    m=random.randint(1,3)
    print("You lost the toss")
g=m%2
#GGS_Preetham_Karthikeyan_:_Reg._No._:21BCE5719
if(g==0):
    print('''Welcome to handcricket game. 
          {} bats first and {} bowls first.
          Computer is {} & you are {}. 
          Let's Play !!!'''.format(a_n,b_n,a_n,b_n))
    m=0
    i=0
    j=0
    aw=0
    ar=0
    bw=0
    br=0
    while(m==0):
        if(aw<q):
            if(i==r):
                m=m+1
                print("{} has scored {} runs. {} needs to score {} off {} balls ".format(ar,a_n,b_n,ar+1,r,))
                break
            elif(i<r):
                a=random.randint(0,6)
                b=int(input("the type of ball"))
                if(a==b):
                    aw=aw+1
                    i=i+1
                    print("You bowled {} and {} hit {}".format(b,a_n,a))
                    print("The score of {} is {}-{} in {} balls".format(a_n,ar,aw,i))
                if(a!=b):
                    if(b>6):
                        print("Invalid Input bro - your input was {}".format(b))                   
                        print("The score of {} is {}-{} in {} balls".format(a_n,ar,aw,i))                
                    else:
                        ar=ar+a
                        i=i+1
                        print("You bowled {} and {} hit {}.".format(b,a_n,a))
                        print("The score of {} is {}-{} in {} balls".format(a_n,ar,aw,i))               
        elif(aw==q):
            m=m+1
            print("{} has scored {} runs. {} needs to score {} runs off {} balls".format(a_n,ar,b_n,ar+1,r))
            break
    while(m==1):
        if(bw==q):
            if(ar>br):
                print("{} beat {} by {} runs".format(a_n,b_n,ar-br))
                break
            if(ar==br):
                 print("It's a tie")
                 break
        elif(bw<q):
            if(j==r):
                if(ar>br):
                    print("{} beat {} by {} runs".format(a_n,b_n,ar-br))
                    break
                if(ar==br):
                    print("It's a tie")
                    break
                if(ar<br):
                    print("{} beats {} by {} wickets".format(b_n,a_n,q-bw))
                    break
            elif(j<r and ar>br):
                    a=random.randint(0,6)
                    b=int(input("the type of shot"))            
                    if(a==b):
                        bw=bw+1
                        j=j+1
                        print("{} bowled {} and {} hit {}".format(a_n,a,b_n,b))
                        print("The score of {} is {}-{} in {} balls".format(b_n,br,bw,j))
                    if(a!=b):
                        if(b>6):                        
                            print("Invalid Input bro - your input was {}".format(b))                        
                            print("The score of {} is {}-{} in {} balls".format(b_n,br,bw,j))
                        else:
                            br=br+b
                            j=j+1
                            print("{} bowled {} and {} hit {}".format(a_n,a,b_n,b))
                            print("The score of {} is {}-{} in {} balls".format(b_n,br,bw,j))                
            elif(j<r and ar<br):
                print("{} beats {} by {} wickets".format(b_n,a_n,q-bw))
                break
        
if(g==1):
    print('''Welcome to handcricket game. 
          {} bats first and {} bowls first.
          Computer is {} & you are {}. 
          Let's Play !!!'''.format(b_n,a_n,a_n,b_n))
    m=0
    i=0
    j=0
    aw=0
    ar=0
    bw=0
    br=0
    while(m==0):
        if(bw<q):
            if(i==r):
                m=m+1
                print("{} has scored {} runs. {} needs to score {} runs off {} balls ".format(b_n,br,br+1,a_n,r))
                break
            elif(i<r):
                a=random.randint(0,6)
                b=int(input("the type of shot"))
                if(a==b):
                    bw=bw+1
                    i=i+1
                    print("{} bowled {} and you hit {}".format(a_n,a,b))
                    print("The score of {} is {}-{} in {} balls".format(b_n,br,bw,i))
                if(a!=b):
                    if(b>6):
                        print("Invalid Input bro - your input was {}".format(b))                   
                        print("The score of {} is {}-{} in {} balls".format(b_n,br,bw,i))                
                    else:
                        br=br+b
                        i=i+1
                        print("{} bowled {} and you hit {}.".format(a_n,a,b))
                        print("The score of {} is {}-{} in {} balls".format(b_n,br,bw,i))               
        elif(bw==q):
            m=m+1
            print("{} has scored {} runs. {} needs to score {} runs off {} balls ".format(b_n,br,a_n,br+1,r))
            break
    while(m==1):
        if(aw==q):
            if(br>ar):
                print("{} beat {} by {} runs".format(b_n,a_n,br-ar))
                break
            if(br==ar):
                 print("It's a tie")
                 break
        elif(aw<5):
            if(j==r):
                if(br>ar):
                    print("{} beat {} by {} runs".format(b_n,a_n,br-ar))
                    break
                if(ar==br):
                    print("It's a tie")
                    break
                if(br<ar):
                    print("{} beats {} by {} wickets".format(a_n,b_n,q-aw))
                    break
            elif(j<r and br>ar and aw<5):
                    a=random.randint(0,6)
                    b=int(input("the type of ball"))            
                    if(a==b):
                        aw=aw+1
                        j=j+1
                        print("you bowled {} and {} hit {}".format(b,a_n,a))
                        print("The score of {} is {}-{} in {} balls".format(a_n,ar,aw,j))
                    if(a!=b):
                        if(b>6):                        
                            print("Invalid Input bro - your input was {}".format(b))                        
                            print("The score of {} is {}-{} in {} balls".format(b_n,br,bw,j))
                        else:
                            ar=ar+a
                            j=j+1
                            print("you bowled {} and {} hit {}".format(b,a_n,a))
                            print("The score of {} is {}-{} in {} balls".format(a_n,ar,aw,j))                
            elif(j<r and br<ar):
                print("{} beats {} by {} wickets".format(a_n,b_n,q-aw))
                break
        
    
            
            
                
        
    
        