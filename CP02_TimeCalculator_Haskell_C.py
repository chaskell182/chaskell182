'''
Christopher Haskell
Feb 13, 2024
ISCS 210 Python Program
Filename: CP02_TimeCalculator_Haskell_C.py
Description of the program:
Write a program that asks the user to enter a number
of seconds and works as follows:

There are 60 seconds in a minute.
If the number of seconds entered by the user is greater than or equal to 60,
the program should convert the number of seconds to minutes and seconds.

There are 3,600 seconds in an hour.
If the number of seconds entered by the user is greater than or equal to 3,600,
the program should convert the number of seconds to hours, minutes, and seconds.

There are 86,400 seconds in a day.
If the number of seconds entered by the user is greater than or equal to 86,400,
the program should convert the number of seconds to days, hours, minutes,
and seconds

Algorithm:
Input: What am I inputting and how
Prompt the user to input a number of seconds


Processing:
Calculate the number of minutes, hours or days the inputted
number of seconds equals 


Output:
Display the seconds, minutes if the input is greater than 60,
hours if the input it greater than 3600 or days if the input
is greater than 86400
'''


MINUTE = 60
HOUR = 3600
DAY = 86400

minutes = 0   #seconds divided by 60
rem_sec = 0   #Remaning seconds
hour = 0      #Number of hours
rem_min = 0   #Remaining minutes
day = 0       #Number of days
rem_hour = 0  #Remaining hours



     
import math

#math.floor will round number down to print the whole minute/hour/day


print('\nThis program converts the number of seconds you enter to minutes,'
      '\nhours and days')
#Prompt the user for the number of seconds

seconds = float(input('\nPlease enter the number of seconds: '))

minutes = int(math.floor((seconds / MINUTE)))

rem_sec = seconds % 60

#f the input is less than 60 seconds, no coversion is necessary

if(seconds < MINUTE):
    print(f'\nYou entered {seconds} seconds')

#if the input is is 60, print one minute 

if(seconds == 60):
    print('The number of seconds you entered is equal to one minute.')

#if the input is greater than 60 and less than 3600, convert seconds to minutes

if(seconds > MINUTE and seconds < 3600):
    
    print(f'\nThe number of seconds you entered equals {minutes:.2f} minutes' , 
          f'\nand {rem_sec} seconds')

#----------------------------------------------------------------------------

#if input equals 3600, print one hour
    
if(seconds == 3600):
    
    print('\nThe number of seconds you entered equals one hour')

#calculate seconds to hours and minutes 
  
hours = int(math.floor((seconds / HOUR)))

rem_min = int((seconds / 60) % 60)

rem_sec2 = seconds % 60


if(seconds > HOUR) and (seconds < DAY):
    print(f'\nThe number of seconds you entered equals {hours:.2f} hours' , 
          f'\n{rem_min:.2f} minutes and {rem_sec2:.2f} seconds.')


#--------------------------------------------------------------------------

#if input equals 86400, print one day

if seconds == DAY:
    print('\nThe seconds you entered equals 24 hours, or one day')

#If the input is greater than 86400 convert seconds to days, hours, minutes

days = int(math.floor((seconds / DAY)))

rem_hour = int((seconds / 3600) % 24)

rem_min2 = int((seconds / 60) % 60)

rem_sec3 = int(seconds % 60)

if seconds > DAY:
    print(f'\nThe seconds you entered is equal to {days} days, {rem_hour} hours,')
    print(f'\n{rem_min2} minutes and {rem_sec3} seconds.')



#just checking the results, minutes and seconds are correct but hours are not 


    






















