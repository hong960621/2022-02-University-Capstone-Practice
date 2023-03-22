import numpy as np

#QUIZ 1) Code a program that geneates passwords for each site.
site = input("Enter the address of the Website: ") #input address
tmpsite = site[7:]                                 #slice 'http://' out
a = tmpsite.rfind('.')                             #Find len of string til hits '.'
new_str = tmpsite[:a]                              #slice '.com' out

cpnt1 = new_str[:3]                                #Component 1, first 3 digits of remaining characters
cpnt2 = len(new_str)                               #Component 2, the number of characters
str_cpnt2 = str(cpnt2)                             #Change int to str  
cpnt3 = new_str.count('e')                         #Component 3, the number of character 'e' in the String 
str_cpnt3 = str(cpnt3)                             #Change int to str
cpnt4 = cpnt1[2:]                                  #Component 4, last character of the first 3 digits 
upper = cpnt4.upper()                              #Capitalize compnent 4
pw = upper + cpnt1 + str_cpnt2 + str_cpnt3 + '!'   #Generate password via concatenating all 5 components

print('')                                          #new line
print('The password for "%s" is generated as "%s".' %(site, pw))








