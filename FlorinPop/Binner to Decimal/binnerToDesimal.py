print ('###################################')
print ('This is convert Binner to Decimal \n')
inputBinner = input('Fill binary digit :')
lenght = len(inputBinner)
temp = 0
wrong = False
for i in range (lenght) :
    a = int (inputBinner[i])
    if a != 0 and a !=1 :
        print ('Please, input 0 or 1')
        wrong = True    
    else :
        temp += 2**((lenght-1)-i)*a
if wrong == False :
    print(f'The decimal of {inputBinner} is {temp}')