import random

#Quiz 3) Kakao Taxi
passlist = range(1, 51)                                              # Create a passengers list range betwen 1 to 50
cnt = 0                                                              # Declare counter to display total passengers
for i in passlist:                                                   # Run, until finish reading passengers list
    time = random.randint(5, 50)                                     # Give out a random travel time between 5 to 50

    if time <= 15:                                                   # If a given travel time is less than, or equal to 15
        a = 'O'                                                      # a = 'O'
        cnt = cnt + 1                                                # Increase counter by 1
    else:                                                            # If a given travel time is not less than, or equal to 15 
        a = ' '                                                      # a = ' '
    print('[%c] passenger %d (travel time: %d minutes)'%(a,i,time))  # Print out each passenger with given number and travel time
print('Total passengers : %d '%(cnt))                                # Print out total passengers

   