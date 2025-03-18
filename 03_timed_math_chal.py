#timed how long it takes to complete a set of math questions
#random generate questions
#https://youtu.be/21FnnGKSRZo?t=2385
import random
import time

OPERATORS=['+','-','*']
MIN_OPERAND=3
MAX_OPERAND=12
TOTAL_PROBLEMS=10


def generate_problem():
    left= random.randint(MIN_OPERAND, MAX_OPERAND)
    right=random.randint(MIN_OPERAND, MAX_OPERAND)
    operator=random.choice(OPERATORS)

    #generating the question
    expr= str(left)+" "+ operator+" "+str(right)
    #obtaining the answer using eval based on the expression
    answer=eval(expr)
    #print (expr)
    return expr, answer



#generate_problem()

wrong =0
input('Press enter to start!')
print("----------------------------------")
start_time=time.time()
for i in range(TOTAL_PROBLEMS):
    expr, answer= generate_problem()
    while True:
        guess= input('Problem # '+ str(i+1)+ ": "+ expr + "=")
        if guess==str(answer):
            break
        wrong+=1

end_time=time.time()
total_time= round(end_time - start_time,2 )
pri
nt("----------------------------------")
print ('Nice work! You finished in ', total_time, " seconds!")