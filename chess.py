
# functions 
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



# small_latter_asci = []
# capital_latter_asci = []

# for i in range(97,123):
#     small_latter_asci.append(i)


# for i in range(65,91):
#     capital_latter_asci.append(i)    

# def small_latter_asci():
#     small_latter_asci = []
#     for i in range(97,123):
#         small_latter_asci.append(i)
#     return small_latter_asci
    

# def capital_latter_asci(latter):
#     capital_latter_asci = []
#     for i in range(65,91):
#         capital_latter_asci.append(i) 
#     return capital_latter_asci






moves = ['h4','e5+','f3','Cd0','Bck4','O-O','o8']

flag = False

for i in moves:
    
    if len(i) >= 2 and len(i) <= 4:

        # lenght two validation 
        if len(i) == 2:
            if checkTwoLength(i) != True:
                flag = True  

        # lenght three validation 
        if len(i) == 3:
            if checkTwoLength(i[0:2]) and i[-1] in ['+','#']:
                pass
            elif ord(i[0]) in range(65,91) and checkTwoLength(i[1:]):
                pass
            elif i == "O-O":
                pass
            else:
                flag = True 

        # lenght four validation
        if len(i) == 4:
            pass
        
    else:
        flag = True



    
if flag:
    print("Invalid")
else:
    print("Valid")
