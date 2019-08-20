import random

def generateString(typeOfString):
    generatedstr = ""
    flag=0
    sindex=1
    for i in range(noc):
        if(ws == 1):
            
            if(flag==0):
                flag=1
                sindex=random.randint(1,10)+len(generatedstr)
                
            if(len(generatedstr) == sindex):
                generatedstr = generatedstr + ' '
                flag=0
            else:
                index = random.randint(0,(len(typeOfString)-1))
                generatedstr = generatedstr + typeOfString[index]
        else:
            index = random.randint(0,(len(typeOfString)-1))
            generatedstr = generatedstr + typeOfString[index]
                
    return generatedstr


while True:
    noc = int(input("\nEnter number of characters you want to generate: "))
    tos = int(input("1.Numeric, 2.Alphanumeric, 3.Alphabets only\n"))
    cs=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    ns=['0','1','2','3','4','5','6','7','8','9']
    ans=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
    ws = int(input("1.String with space, 2.String with no space\n"))
    
    if(tos == 1):
       generatedstr = generateString(ns)
    elif(tos == 2):
        ifgeneratedstr = generateString(ns+cs)
    elif(tos == 3):
        generatedstr = generateString(cs)
        
    print(generatedstr)
