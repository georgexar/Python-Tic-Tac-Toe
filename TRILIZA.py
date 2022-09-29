def tril(lst):
    trilizes = 0
    for i in range(len(lst)):
        for j in range(len(lst[i]) - 2):
            if lst[i][j] + lst[i][j + 1] + lst[i][j + 2] == 3 * lst[i][j]:
                trilizes = trilizes + 1  # τριλιζες στις οριζοντιες γραμμες
    for i in range(len(lst) - 2):
        for j in range(len(lst[i])):
            if lst[i][j] + lst[i + 1][j] + lst[i + 2][j] == 3 * lst[i][j]:
                trilizes = trilizes + 1  # τριλιζες στις καθετες γραμμες
    for i in range(len(lst) - 2):
        for j in range(len(lst[i]) - 2):
            if lst[i][j] + lst[i + 1][j + 1] + lst[i + 2][j + 2] == 3 * lst[i][j]:
                trilizes = trilizes + 1  #τριλιζες διαγωνια αριστερα πανω προς δεξια κατω
    for i in range(len(lst) - 2):
        for j in range(2, len(lst[i])):
            if lst[i][j] + lst[i + 1][j - 1] + lst[i + 2][j - 2] == 3 * lst[i][j]:
                trilizes = trilizes + 1  #τριλιζες διαγωνια αριστερα κατω προς δεξια πανω
    return trilizes


# Για input λιστας ειναι ο παρακατω κωδικας
'''randomlist=[]
n=input('Βαλε αριθμο στοιχειων λιστας:')
k=input('Βαλε αριθμο στοιχειων που θα εχει το καθε στοιχειο της λιστας:')
for i in range(int(n)):
    l=[]
    for j in range(int(k)):
        element=input('βαλε 0 H 1:')
        l.append(element)
    print('στοιχειο',i+1,'της λιστας ειναι:',l)
    randomlist.append(l)
print('η τελικη λιστα ειναι:',randomlist)
tril(randomlist)'''