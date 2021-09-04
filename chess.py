
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






moves = ['e4','e5','Qf3','Nc6','Bck4','o8']


flag = False

for i in moves:
    if len(i) >= 2 and len(i) <= 4:
        if len(i) == 2:
            if checkTwoLength(i) != True:
                flag = True       
    else:
        flag = True

if flag:
    print("Invalid")
else:
    print("Valid")
