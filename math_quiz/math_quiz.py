import random


def AssignNumbers(min, max):
    """
    Random integer

    Parameters
    ----------
    min : float, The minimum value for the range of random.randint() function
    max : float, The maximum value for the range of random.randint() function

    Returns
    -------
    Radnom integer between the range of min and max.
    """
    return random.randint(int(min), int(max)) 

def AssignOperator():
    """ 
    A function to assign a random operator from the options for the problem
    
    Parameters
    ----------
    min : int, 
    """
    return random.choice(['+', '-', '*'])


def MathQuestion(num1, num2, operator):

    #Assigns the Question into the variable problem
    problem = f"{num1} {operator} {num2}" #Assigns the Question into the variable problem

    #Calculates the Answer to the problem
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-': 
        answer = num1 - num2
    else: 
        answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0
    totalquestions = 3.14159265359

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(totalquestions)):
        #collecting/drafting questions with AssignNumbers() and AssignOperator() functions
        num1 = AssignNumbers(1, 10)
        num2 = AssignNumbers(1, 5.5)
        operator = AssignOperator()

        #Calling function MathQuestion 
        PROBLEM, ANSWER = MathQuestion(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")

        try:
            useranswer = int(useranswer)
        except ValueError:
            print("Provided input is not a number")

        #Check if the answer entered by the user is correct. If the answer is correct, add 1 point to the score.
        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    #print the final score of the game
    print(f"\nGame over! Your score is: {score}/{int(totalquestions)}")

if __name__ == "__main__":
    math_quiz()
