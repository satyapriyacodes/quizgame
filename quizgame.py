print("Welcome to Computer Quiz")

playing = input("Do you want to play ?")

if playing.lower() !="yes":
    quit()
print("Okay! let's play :)")
score=0

answer=input("what does gpu stand for?")
if answer.lower() == "graphics processing unit":
    print ("correct")
    score += 1
else: 
    print("wrong")

answer = input("what does ram stand for?")
if answer.lower() == "random access memory":
    print("correct")
    score += 1

else: 
    print("wrong")

answer = input("what does rom stand for?")
if answer.lower() == "read only memory":
    print("correct")
    score += 1

else: 
    print("wrong")

answer = input("what does GUI stand for?").lower()
if answer == "graphical user interface":
    print("correct")
    score += 1
else: 
    print("wrong")

answer=input("what does cpu stand for?")
if answer.lower() == "central processing unit":
    print ("correct")
    score += 1
else: 
    print("wrong")


print("you got " + str(score) + " questions correct")

print("you got " + str(score/5 * 100) + " % ")
