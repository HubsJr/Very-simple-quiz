ghj=input("enter your first name:")
print("Welcome to my Quiz:\nIf you go wrong once you lose but if you give all the answers correct then you win but no CHEATING.")
print("Q1:-Who is the president of India?")
winlist=("ramnath govind","multiple choice question","multiple choice questions","mumbai")
enter=input("enter your answer here:")
seat=enter.lower()
x=0
if seat in winlist:
    print("woah you surely are smart you are correct!!!!")
    x=x+1
else:
    print("you went wrong at the first question")
    x=x-1
print("Q2:-What is the full form of MCQ?")
enter2=input("enter your answer here:")
seat2=enter2.lower()
if seat2 in winlist:
    print("you are right!!!!!!")
    x=x+1
else:
    print("I told you this is a hard quiz, ur answer is wrong")
    x=x-1
print("Q3:-which city is the india's largest city by population")
enter3=input("enter ur answer here:")
seat3=enter3.lower()
if seat3 in winlist:
    print("you are right!!!")
    x=x+1
else:
    print("you were wrong you lose 1 mark")
    x=x-1
print("well " +str(ghj)+ " you have completed the quiz and scored: "+str(x)+" marks")



































