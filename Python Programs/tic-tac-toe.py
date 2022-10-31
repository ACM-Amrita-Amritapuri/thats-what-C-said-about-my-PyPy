from tkinter import *
from tkinter.messagebox import showinfo

y=""
x=0
player_1=[]
player_2=[]


def define_sign(number):

    global x,y
    global player_1,player_2
    from itertools import permutations

    set1=permutations([1,2,3])
    set2=permutations([4,5,6])
    set3=permutations([7,8,9])
    set4=permutations([1,4,7])
    set5=permutations([2,5,8])
    set6=permutations([3,6,9])
    set7=permutations([1,5,9])
    set8=permutations([3,5,7])

    for i in set1,set2,set3,set4,set5,set6,set7,set8:
        for j in list(i):
            plyr_1=all(elem in player_1 for elem in j)
            plyr_2=all(elem in player_2 for elem in j)
            if plyr_1 == True:
                print(player_1)
                showinfo("Game Result","Player 1 has WON!!!")
                break
            elif plyr_2 == True:
                print(player_1)
                showinfo("Game Result","Player 2 has WON!!!")
            else:
                pass

    if number==1:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b1.config(text=y)
        x=x+1



    if number==2:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b2.config(text=y)
        x=x+1



    if number==1:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b1.config(text=y)
        x=x+1



    if number==3:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b3.config(text=y)
        x=x+1



    if number==4:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b4.config(text=y)
        x=x+1



    if number==5:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b5.config(text=y)
        x=x+1



    if number==6:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b6.config(text=y)
        x=x+1



    if number==7:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b7.config(text=y)
        x=x+1



    if number==8:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b8.config(text=y)
        x=x+1



    if number==9:
        if x%2 == 1:
            y = 'X'
            player_1.append(number)
            print(player_1)

        elif x%2 != 1:
            y = 'O'
            player_2.append(number)
            print(player_2)

        b9.config(text=y)
        x=x+1



app=Tk()
app.title("TIC-TAC-TOE")

l1=Label(app,text="player 1 : X",font = "times 25")
l1.grid(row=0,column=1)

l2=Label(app,text="player 2 : O",font = "times 25")
l2.grid(row=0,column=3)

b1=Button(app,width=20,height=10,command=lambda: define_sign(1))
b1.grid(row=1,column=1)

b2=Button(app,width=20,height=10,command=lambda: define_sign(2))
b2.grid(row=1,column=2)

b3=Button(app,width=20,height=10,command=lambda: define_sign(3))
b3.grid(row=1,column=3)

b4=Button(app,width=20,height=10,command=lambda: define_sign(4))
b4.grid(row=4,column=1)

b5=Button(app,width=20,height=10,command=lambda: define_sign(5))
b5.grid(row=4,column=2)

b6=Button(app,width=20,height=10,command=lambda: define_sign(6))
b6.grid(row=4,column=3)

b7=Button(app,width=20,height=10,command=lambda: define_sign(7))
b7.grid(row=8,column=1)

b8=Button(app,width=20,height=10,command=lambda: define_sign(8))
b8.grid(row=8,column=2)

b9=Button(app,width=20,height=10,command=lambda: define_sign(9))
b9.grid(row=8,column=3)

app.mainloop()
