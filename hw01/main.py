for i in range(1,10):
    for k in range(1,i):
        print(end='       ')
    for j in range(i,10):
        formula='{0:1}*{1:1}={2:<3}'.format(i,j,i*j)
        print(formula,end='')
    print('')




