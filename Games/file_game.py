import random 

def game ():
    print("you are playing the game ")
    score= random.randint(1,50)
    with open ( "Games/highscore.txt", "r") as f :
        highscore=f. read ()
        if highscore!="":
            highscore=int ( highscore)
        else :
            highscore=0
        print ( f"your score is {score}")
    if score>highscore:
        with open ( "Games/highscore.txt","w") as f :
            f . write(str (score))
            return score
        
a=game()
print (a)
