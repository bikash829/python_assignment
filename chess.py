
# --------------start custom functions ---------------------

# single digit checker function 
def checkSignleDigit(data):
    if data.isnumeric():
        convert = int(data)
        if convert in range(10):
            return True
        else:
            return False    
    else:
        return False


#Two length checker 
def checkTwoLength(data):
    if ord(data[0]) in range(97,123):
        if data[1].isnumeric():
            convert = int(data[1])
            if convert in range(10):
                return True
            else:
                return False    
        else:
            return False
    else:
        return False


# type two condition check of length moves
def lenThreeTypTwo(data):
    if ord(data[0]) in range(65,91) and checkTwoLength(data[1:3]):
        return True
    else: 
        return False


# function for two to four length's move chess 

def chessValidation(data):
    flag = False
    checkMate = []
    for i in data:
        
        if len(i) >= 2 and len(i) <= 4:
            # check mate validation 
            if '#' in i:
                checkMate.append(i)
            # -------------------lenght two validation---------------------
            if len(i) == 2:
                if checkTwoLength(i) != True:
                    flag = True  
                    break

            # -----------------lenght three validation---------------------
            if len(i) == 3:
                # Type 1 - A length 2 move + '#/+' - e4#,c3#,f1+,c3+ 
                if checkTwoLength(i[0:2]) and i[-1] in ['+','#']:
                    pass

                # Type 2 - A capital letter + a length 2 move - Nf3, Rb1
                elif lenThreeTypTwo(i):
                    pass

                # Type 3 - O-O 
                elif i == "O-O":
                    pass

                else:
                    flag = True 
                    break

            # ----------------lenght four validation-------------------
            if len(i) == 4:
                # Type 1 - A Type 2 Length 3 move + '#/+' - Nf3# , Qc7# , Rc8+, Ke2+
                if lenThreeTypTwo(i[0:3]) and i[-1] in ['+','#']:
                    pass

                # Type 2 - A small letter + 'x' + a length 2 move - exb4 , cxd7 
                elif ord(i[0]) in range(97,123) and i[1] == 'x' and checkTwoLength(i[2:]): 
                    pass

                #  Type 3 - A capital letter + a small letter/ a digit +  a length 2 move - Nbd7 , R1d8 
                elif ord(i[0]) in range(65,91) and (checkSignleDigit(i[1]) or ord(i[1]) in range(97,123)) and checkTwoLength(i[2:]):
                    pass
                else:
                    flag = True
                    break
        else:
            flag = True
            break



    # validation for checkmate
    if len(checkMate) == 1:
        if checkMate[0] == data[-1]:
            pass
        else:
            flag = True
    else:
        flag = True


    # final output
    if flag:
        return "Invalid"
    else:
        return "Valid"
        
# -----------------end custom functons------------------- 



moves = input("Please enter your moves and each moves must be separated by comma/space: ").strip()


if ',' in moves:
    filter = moves.split(',')
    filterMoves = []
    for i in filter:
        filterMoves.append(i.strip())
else:
    filterMoves = moves.split()
    

print(chessValidation(filterMoves).center(50,"="))
