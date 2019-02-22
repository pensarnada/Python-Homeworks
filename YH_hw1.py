"""
Expectation for the homework :

Take two positive numbers from the player: begin and end.
Generate a random number, target in [begin, end].
The game starts with a score, S = 100 and consists of different rounds.
In each round,

- Display “The target is in [begin, end]. You have N guesses...” on console.
- Get N guesses from player, where N is 20% of the range size (end-begin). This means that more
guesses are allowed for larger ranges and vice versa.
- For each wrong guess, take 5 points off from score S and display “Wrong guess!” on console.
- If any of the N guesses is equal to target value, display “Right guess! Score: S” and finish the
game.
- Otherwise, reduce the range to half which contains the target.
Repeat the steps above until either the player doesn't have any guesses (N < 1) or run out of score
(S ? 0). In any of these cases, display “You lost! The target was target.” and finish the game.

IMPORTANT NOTE:
Be careful about invalid inputs: All inputs must be numeric, end must be greater than begin, and each
guess must be in the specified range. Ask each question over and over again until a valid input is
entered, but do not decrease the score or N for invalid inputs.
"""

#Yusuf HAYIRLI
import random
begin=input("Begin? ") #input begin
while True: #We check begin value if it is numeric or not.
    if begin.isnumeric() == True:
        begin=int(begin)
        break
    else:
        begin=input("Enter a numeric value for begin: ") #if begin is not numeric, ask again.
        if begin.isnumeric() != True:
            continue 
        else:
            begin=int(begin)
            break
end=input("End? ") #input end
while True: #We check end value if it is numeric or greater than begin value.
    if end.isnumeric() == True:
        end=int(end)
        if begin>=end: 
            end=input("Enter a value greater than begin: ") #if begin<end, ask again.
            continue
            if end.isnumeric() != True:
                continue
            else:
                end=int(end)
        break #if end is numeric and greater than
    else:
        end=input("Enter a numeric value for end: ") #if end is not numeric, ask again.
        if end.isnumeric() != True:
            continue
        else:
            end=int(end)
            if begin>=end:
                end=input("Enter a value greater than begin: ") #if begin<end, ask again.
                continue
            else:
                end=int(end)
                break
x=random.randint(begin,end) #random number generate a number to x
S=100 #Starting score.
N=((end-begin)*(0.2)) #Our guesses here.
newN=N #Checks if N<0 or not.
Count_N=0 #Counts how many guesses used per round to pass it or end it if its newN=0.
print("The Target is in [",begin,",",end,"]") #display Range
print("You have",int(N),"guesses...") #Display guesses
while N>=1 and S>=0: #Starts the loop for get guesses...
    guess=input("Enter your guess: ")
    if guess.isnumeric() != True:
        print("Enter a numeric value for guess: ")
        continue
    else:
        guess=int(guess)
        if guess<begin or guess>end:
            print("Enter a value in specified range:\n")
            continue
    therange=(end-begin)/2 #Calculating the range
    Count_N+=1 #Counting the used guesses
    if(Count_N==20):
        print("You Lost! The Target was ",x)
        break #if we used 20 guesses, Score point will be over and it will be end.
    else:
        if (guess!=x and Count_N<20): #or it will count the guesses
            N-=1
            print("Wrong Guess!")
            S-=5
            if(N==0 and newN//2 >= 1): #if N is over, we check if our guesses >=1 or not.
                N= newN//2 #we assign newN to N if newN>=1 
                newN//=2 #we divide newN to find new guesses if >=1 or not.
                if(x+therange >= end ): #if x+our range is bigger than end, x is in between end and mid.
                    begin+=therange
                    print("The Target is in [",int(begin),",",int(end),"]") #Displays range
                    print("You have",int(N),"guesses...") #Displays left guesses
                else: #else x is in between begin and mid.
                    end-=therange 
                    print("The Target is in [",int(begin),",",int(end),"]") #Displays range
                    print("You have",int(N),"guesses...") #Displays left guesses
            elif(N==0 and newN//2<1): #if N=0 and our newN is lower than 1, we're out of guesses.
                print("You lost! The target was ",x) #and we lost because N<1
        else:
            print("Right Guess! Your Score: ",S) #If we answer right, it will give our score and congrats.
            break #If we answer right, we will be out of while and stop the program.
