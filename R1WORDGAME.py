option=1
print ("\nWelcome player..!..This is a small model of the game HANGMAN.\nYou have to predict the name of your classmate with utmost 10 guesses..\nYou can quit the game by inputting QUIT anytime.\nHere you go!!")
while (option==1):
    import random
    chanceno=0
    flag=1
    k=0
    wordlist=['AARATHI','ADVAITH','AFNAN','AJAYJEEVAN','AJAYPHILIP','AKSHAY','AMITHA','AMJAD','ANIRUDH','ANIT','ANNA','ANUJA','ARJUNMS','ARJUNRS','ARSHA','ARUN','ASHIESH','ATHILA','ATHIRA','ATOZ','AUSTIN','AYSHA','AZHAR','BABITHA','BASIMA','BRIAN','DILBER','FARHAN','FIDEL','GOURI','GRACE','HANIN','HARI','HISHAM','JUBIN','KARTHIKA','KENNEDY','KIRAN','LIA','MARIYA','MILAN','MUHAMMED','NAFI','NEELIMA','PRAVEEN','REENU','RISAL','RIZAN','SAHIL','SAHLA','SARANYA','SARATH','SHAHIL','SHRUTHI','SOORAJ','SOURAV','SREECHANDANA','SREEJITH','SUHAIL','SUJITH','SWATHI','TAPAN','THARIKH','THAYYIB','TINUMOL','UTHARA','VENI','VISHNU','ZEN']
    right=random.choice(wordlist)
    l=len(right)
    a=["-"]*l
    print ("\nThe skeleton of the name is : ", "- "*l)
    for chanceno in range (10):
        pp=0
        res=""
        sample=input("\nEnter a letter or the name as such : ")
        sample=sample.upper()
        if (sample=="QUIT"):
            print ("You chose to quit...The right answer was ",right)
            exit()
        if (sample==right):
            flag=0
            break
        chanceno+=1
        for i in range (l):
            if(right[i]==sample):
                a[i]=sample
                k=k+1
                pp=1
        if (pp==1):
            print ("Correct Guess!")
        if (pp==0):
            print ("Wrong Guess..")
        for j in a:
            res=res+j+" "
        print ("The new skeleton is : ",res)
        if (k==l):
                flag=0
                break
        else :
            print ("You have",(10-chanceno),"tries left")
    if (flag==0):
        print ("Wow..You have guessed it right")
    else:
        print ("\nSorry..game over")
        print ("The right answer was ",right)
    option=int(input("Do you want to continue?? If yes, enter 1 :"))
    if (option!=1):
        print ("Thank you for playing") 
