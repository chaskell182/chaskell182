'''
Christopher Haskell
Date: Thu Mar 7 11:45:06 2024
ISCS 210 Python Program
Filename: CP04_MathQuiz_Haskell_C
Description of the program:
Write a program that administers simple math quizzes. 
The program should display two random numbers that are to be added, such as:

247 + 129

The program should allow the student to enter the answer to the quiz. 
Your program should compare the numbers added to the student’s answer.
If the answer is correct, a message of congratulations should be displayed.
If the answer is incorrect, a message showing the correct answer should be 
displayed.

Algorithm:
Input: Prompt the user to input the answer to the question 

Processing: Generate two random numbers (rand.int) and find the sum
determine if the inputted answer is correct 


Output: Display congratulations for a correct answer, display incorrect
and the correct answer if the the answer is wrong 
'''
print('\nThis program will display 10 addition questions with numbers between 1 and 1000')
print('\nPlease solve the following 10 addition problems')

#import random to generate random integer 

import random
'''
#set variables    
total_wrong = 0
total_right = 0

#Set the number of questions with a for loop
for question in range (10):
        
      
#Generate random integers    
    num1 = random.randint(1, 1000)
    num2 = random.randint(1,1000)
#Get right answer     
    answer = num1 + num2
#Input user answer
    guess = int(input(f'\nWhat is {num1} + {num2}? '))
        
        
#------------------------------------------------------------------------------


#If correct
    if guess == answer:
        print('\nCongratulations! Thats correct')
        total_right += 1
        
#If incorrect     
    if guess != answer:
        print(f'\nSorry, thats incorrect. The correct answer is {answer}')
        total_wrong += 1
#Display the results
print(f'\nYou got {total_right} questions right, and {total_wrong} questions wrong')


#Calc final grade 
grade = (total_right / 10) * 100


#Steal code from CP03
if grade >= 90:
    score1 = 'A'
    
elif grade >= 80 and grade <= 89:
    score1 = 'B'
    
elif grade >= 70 and grade <= 79:
    score1 = 'C'
    
elif grade >= 60 and grade <= 69:
    score1 = 'D'

elif grade < 60:
    score1 = 'F'

#Display the grade 
print(f'\nYour grade is an {grade} percent, which is letter grade {score1}')
'''    


#if you want to ask a non-specific amount of questions:

    
def main():  
    
     again = ''
     
     while again == '':
         
         total_right = 0
         num1 = random.randint(1, 1000)
         num2 = random.randint(1,1000)
         
         answer = num1 + num2
     
         guess = int(input(f'\nWhat is {num1} + {num2}? '))
             
             
         is_right(answer, guess)
        
         again = input('\nPress Enter for the next question:') 
         

             
def is_right(answer, guess):
    
    if guess == answer:
        print('\nCongratulations! Thats correct')
        
        
    if guess != answer:
        print(f'\nSorry, the correct answer is {answer}')


main()  

    

        

    

        
    
    

            
       
         
