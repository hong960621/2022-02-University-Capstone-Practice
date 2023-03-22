
#Quiz 4) Code a program to find the standard weight
height = 0                                      # Declare height
gender = 0                                      # Declare gender
Male = 0                                        # Declare Male

height = float(input("키를 입력하세요: "))       # Input height in float
gender = input("성별을 입력 하세요: ")           # Input gender in string
height = height * 0.01                          # Convert cm to M

def std_weight(height, gender):                 # Define function to calculate standard weight 

    if len(gender) <= 4:                        # If length of the string is less than, or equal to 4
        stdweight = height * height * 22        # Define gender as Male and calculate 
    else:
        stdweight = height * height * 21        # Define gender as Female and calculate


    return stdweight                            # Return standard weight
    

stdweight = std_weight(height, gender)          # 오늘의 뽀인트 - 함수를 변수에 지정하여 사용 해야 된당!!
stdweight = round(stdweight,2)                  # round decimal places up to second digits
height = height * 100                           # Convert height M to cm
print('The standard weight for a %d cm tall %s is %.2f kg' %(height,gender,stdweight)) 