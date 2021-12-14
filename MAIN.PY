import random # inporting required module


def gameresults(comp,you): #particular round result
    if(comp==1):
        if(you==2):
            return True
        elif(you==3):
            return False
        elif(you==1):
            return None
    elif(comp==2):
        if(you==3):
            return True
        elif(you==1):
            return False
        elif(you==2):
            return None
    elif(comp==3):
        if(you==1):
            return True
        elif(you==2):
            return False
        elif(you==3):
            return None


choice={1,2,3} # list for rock paper scissor choice so that user do not chose any other input value
print("----------Welcome to the Game designed by Pushpdeep----------")
name = input("Enter your name: ") # taking player name
print(f'''Greetings! {name}, you will compete with computer. 
This game will have 3 rounds score will be as follows
win - 1 points
lose - 0 points
tie - 0 points''')

print("Codes for chosing:\n ROCK(1)\t PAPER(2)\t SCISSOR(3)")
n=int(input("Enter number of rounds: ")) #taking user input for rounds
you_pt =0
comp_pt =0
for i in range(n):
    print(f"ROUND {i+1}")
    b = int(input("Chose: "))
    if(b in choice):
        you=b
    else:
        print("invalid choice you are disqualiied") #if user chose any other choice apart 1,2,3
    if (b==1):
        you_choice='ROCK'
    elif(b==2):
        you_choice='PAPER'
    else:
        you_choice='SCISSOR'
    comp =random.randint(1,3) #random computer choice
    if (b==1):
        comp_choice='ROCK'
    elif(b==2):
        comp_choice='PAPER'
    else:
        comp_choice='SCISSOR'
    pts= gameresults(comp,you)
    if pts:
        you_pt=you_pt+1
        print("you won this round" +" you chose "+you_choice+ " computer chose "+ comp_choice)
    elif pts==None:
        print("you tied this round" +" you chose "+you_choice+ " computer chose "+ comp_choice)       
    else:
        comp_pt=comp_pt+1
        print("you lose this round" +" you chose "+you_choice+ " computer chose "+ comp_choice)
        
#results
if(comp_pt>you_pt):
    print("You lose with "+str(comp_pt-you_pt)+" points")
elif(comp_pt==you_pt):
    print("The game is Tied")
else:
    print("You won with "+str(you_pt-comp_pt)+" points")




