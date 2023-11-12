import random

def AssignNumbers(min, max):
    """
    A function to assign Random integer from a given range

    Parameters
    ----------
    min : float, The minimum value for the range of random.randint() function
    max : float, The maximum value for the range of random.randint() function

    Returns
    ------
    Random integer between the range of min and max.
    """
    return random.randint(int(min), int(max)) 

def AssignOperator():
    """ 
    A function to assign a random operator from the options for the problem
    
    Returns
    -------
    Returns a random operator sign from the list '+' '-' '*' for calculation
    """
    return random.choice(['+', '-', '*'])


def MathQuestion(num1, num2, operator):
    """
    A function to perform the math operation from the passed parameters

    Parameters
    ----------
    num1 : int, First number for the math operation. 
    num2 : int, Second number for the math operation.
    operator : str, An operator for the math operation

    Returns
    -------
    problem : str, Returns the question for the quiz
    answer : int, Returns the answer for the quiz problem
    """

    problem = f"{num1} {operator} {num2}" 

    #Calculates the Answer to the problem using if else if ladder by checking the operator
    if operator == '+': 
        answer = num1 + num2
    elif operator == '-': 
        answer = num1 - num2
    else: 
        answer = num1 * num2

    #returns problem and answer variables
    return problem, answer 

def math_quiz():
    """
    A function to conduct the quiz, input the user value, calculate the score and print the score
    """
    score = 0  #Initialise score value to zero
    totalquestions = 3.14159265359  #Total number of questions, pre defined

    #Print the welcome messages and description about the quiz
    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    #Using loop to conduct the quiz the prescribed number of times
    for _ in range(int(totalquestions)):
        #collecting/drafting questions with AssignNumbers() and AssignOperator() functions
        num1 = AssignNumbers(1, 10)
        num2 = AssignNumbers(1, 5.5)
        operator = AssignOperator()

        #Calling function MathQuestion to get the question and answer
        PROBLEM, ANSWER = MathQuestion(num1, num2, operator)
        
        print(f"\nQuestion: {PROBLEM}") #Print the question
        useranswer = input("Your answer: ") #Prompt to ask the user to input their answer

        #Error Handling if the user enters a non number value
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