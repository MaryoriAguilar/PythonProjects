import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 2
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problems():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)
    
    problem = str(left) + " " + operator + " " + str(right)
    answer = eval(problem)
    return problem, answer

wrong = 0
input("Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    problem, answer = generate_problems()
    while True:
     guess = input("Problem #" + str(i + 1) + ": " + problem + " = ")
     if int(guess) == answer :
         break
     wrong += 1

end_time = time.time()
total_time = end_time - start_time
print("---------------------")
print("Nice work! you end in", round(total_time,2), "seconds")
print("You fail:", wrong, "times")
    
generate_problems()