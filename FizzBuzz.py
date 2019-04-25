
for i in range(1,101):

    x=''                      #creates empty string for output
    
    if i%3==0:                #adds 'Fizz' to output if multiple of 3
        x=x+'Fizz'
        
    if i%5==0:                #adds 'Buzz' to output if multiple of 5
        x=x+'Buzz'
    
    if x=='':                 #assigns i to output if string still empty and therefore not multiple of 3 or 5
        x=i
        
    print(x)
