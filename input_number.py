total_input = 0
num1_to_10 = 0
num11_to_20 = 0
num21_to_30 = 0
num31_to_40 = 0
num41_to_50 = 0

#Loop: asks user to input numbers from 1 to 50
while True: 
    try:
        number = int(input("Input a number from 1 to 50: "))

        if 1 <= number <= 50:
            #Countes number of input between 1 to 50
            if 1 <= number <= 50:
                total_input += 1
            #Counts number of input between 1 to 10
            elif 1 <= number <= 10:
                num1_to_10 += 1
            #Counts number of input between 11 to 20
            elif 11 <= number <= 20:
                num11_to_20 += 1
            #Counts number of input between 21 to 30
            elif 21 <= number <= 30:
                num21_to_30 += 1
            #Counts number of input between 31 to 40
            elif 31 <= number <= 40:
                num31_to_40 += 1
            #Counts number of input between 41 to 50
            elif 41 <= number <= 50:
                num41_to_50 += 1
        else:
            break

    #Stop the loop if input is invalid
    except:
        break