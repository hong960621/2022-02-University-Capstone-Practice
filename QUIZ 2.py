import numpy as np
import random 

# Quiz 2) Code a lottery program
ids = list(range(1,21))                     #Create a list of IDs in range between 1 to 20
random.shuffle(ids)                         #Shuffle the order of the list
winner_list = random.sample(ids, k=4)       #Extract 4 numbers from the list, and create a new list that is made of 4 numbers
chicken_winner = winner_list[3]             #Set the last number from the list as a winner number of chicken
coffee_winner = winner_list[0:3]            #Set the first 3 numbers from the list as winner numbers of coffee

print('')                                   #Set a new line
print('=== Winner Announcement ===')        
print('chicken winner :', chicken_winner)   #Output chicken_winner without manipulation of datatype since it is just an integer
print('coffee winners : ',end='')           #Add end function to avoid the separator to print out comma in the beginning of the output
print(*coffee_winner,sep=',')               #USE asterik to print out data without square brakets and separate each numbers with comma using separator
print('=== Congratulations ===')