for row in range(6):  #heart making.
    for col in range(7):
        if (row==0 and col!=0 and col!=3 and col!=6) or (row==1 and col!=1 and col!=2 and col!=4 and col!=5) or (row==2 and col!=1 and col!=2 and col!=3 and col!=4 and col!=5) or (row==3 and col!=0 and col!=2 and col!=3 and col!=4 and col!=6) or (row==4 and col!=0 and col!=1 and col!=3 and col!=5 and col!=6) or (row==5 and col!=0 and col!=1 and col!=2 and col!=4 and col!=5 and col!=6):
            print("*",end=" ")
        else:
            print(end="  ")
    print()
