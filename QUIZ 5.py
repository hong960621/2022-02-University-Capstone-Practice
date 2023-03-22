#Quiz 5 Code a program that read and write data to a text file.
x = 0                                                          #Delcare counter for While loop
y = 0                                                          #Delcare counter for for loop

with open('C:/Users/홍윤기/Desktop/score.txt', 'w') as f:      #Open 'Score.txt' and write scores of Math and English
    f.write('Math      : 100\n')
    f.write('English   : 90')

with open('C:/Users/홍윤기/Desktop/score.txt', 'a') as f:      #Add additional data in 'Score.txt'
    f.write('\nChem    : 95')
    f.write('\nPhysics : 90')
    f.write('\nCoding  : 100')

with open('C:/Users/홍윤기/Desktop/score.txt', 'r') as f:      #Read 'Score.txt' and print out data of each lines using readlines() and for loop

        lines = f.readlines()                                  #Store data of each lines in variable 'lines' from 'score.txt'
        lines = [line.rstrip('\n') for line in lines]          #Strip out data of each lines until it hits new line
        
        for y in lines:                                        
            print(y)

with open('C:/Users/홍윤기/Desktop/score.txt', 'r') as f:       #Read 'score.txt' and print ot data of each lines using while loop

    while x < 5:
        
        print(lines[x])
        x = x + 1



   
    

