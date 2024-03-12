'''
Christopher Haskell
Feb 22, 2024
ISCS 210 Python Program
Filename: CP03_Test_Score_average_haskell_c.py

Description of the program: 
Write a program that asks the user to enter five test scores.
The program should display a letter grade for each score
and the average test score.
Write the following functions in the program:
calc_average. This function should accept five test scores as arguments and
return the average of the scores.
determine_grade. This function should accept a test score as an argument and
return a letter grade for the score based on the following grading scale:


Score:         Letter Grade:
90–100               A
80–89                B
70–79                C
60–69                D
Below 60             F


Algorithm:
----------

Input: 
Prompt the user to input 5 test scores


Processing:
-----------

The 'calc_average' function will add the scores
and divide by the number of tests entered
The 'determine_grade' function will assign a letter grade
to each inputted test score using if-elif statements

Output:
-------

Display the averages of the scores, and display the letter scores
assigned to each test

'''
#Display the purpose of the program

print('\nThis program will calculate the average of the inputted test scores'
      '\nand assign a letter grade based on the provided grading scale')


#prompt the user for the test scores
def main():

    test1 = int(input('\nPlease enter the first test score: '))
    test2 = int(input('Please enter the second test score: '))
    test3 = int(input('Please enter the third test score: '))
    test4 = int(input('Please enter the fourth test score: '))
    test5 = int(input('Please enter the fifth test score: '))

#call functions in main

    avg = calc_average(test1, test2, test3, test4, test5)
    
    print(f'\nThe average of the test scores is {avg}')
    
    determine_grade(test1, test2, test3, test4, test5)
    
    
    
#Define calc_average function

def calc_average(test1, test2, test3, test4, test5):


    avg = int((test1 +  test2 + test3 + test4 + test5) / 5)
    
    return avg





#-------------------------------------------------------------------

#define determine_grade function

def determine_grade(test1, test2, test3, test4, test5):
    
#Test number 1


    if test1 >= 90:
        score1 = 'A'
        
    elif test1 >= 80 and test1 <= 89:
        score1 = 'B'
        
    elif test1 >= 70 and test1 <= 79:
        score1 = 'C'
        
    elif test1 >= 60 and test1 <= 69:
        score1 = 'D'

    elif test1 < 60:
        score1 = 'F'

              
#----------------------------------------------------------------------

 #Test number 2
     
    if test2 >= 90:
        score2 = 'A'
        
    elif test2 >= 80 and test2 <= 89:
        score2 = 'B'
        
    elif test2 >= 70 and test2 <= 79:
        score2 = 'C'
        
    elif test2 >= 60 and test2 <= 69:
        score2 = 'D'

    elif test2 < 60:
        score2 = 'F'

        
#---------------------------------------------------------------------

 #Test number 3
      
    if test3 >= 90:
        score3 = 'A'
        
    elif test3 >= 80 and test3 <= 89:
        score3 = 'B'
        
    elif test3 >= 70 and test3 <= 79:
        score3 = 'C'
        
    elif test3 >= 60 and test3 <= 69:
        score3 = 'D'

    elif test3 < 60:
        score3 = 'F'

    
#=-----------------------------------------------------------------------

#Test number 4
       
    if test4 >= 90:
        score4 = 'A'
        
    elif test4 >= 80 and test4 <= 89:
        score4 = 'B'
        
    elif test4 >= 70 and test4 <= 79:
        score4 = 'C'
        
    elif test4 >= 60 and test4 <= 69:
        score4 = 'D'

    elif test4 < 60:
        score4 = 'F'

   
#---------------------------------------------------------------------------

#Test number 5
     
    if test5 >= 90:
        score5 = 'A'
        
    elif test5 >= 80 and test5 <= 89:
        score5 = 'B'
        
    elif test5 >= 70 and test5 <= 79:
        score5 = 'C'
        
    elif test5 >= 60 and test5 <= 69:
        score5 = 'D'

    elif test5 < 60:
        score5 = 'F'
        

#--------------------------------------------------------------------------   

    print('\n=============================')

    print('\nTest Score','\tLetter Grade')
    print('--------------------------')

    print(f'\n{test1:^8}', f'\t{score1:^12}')
    print(f'\n{test2:^8}', f'\t{score2:^12}')
    print(f'\n{test3:^8}', f'\t{score3:^12}')
    print(f'\n{test4:^8}', f'\t{score4:^12}')
    print(f'\n{test5:^8}', f'\t{score5:^12}')

#Call main function

main()



























