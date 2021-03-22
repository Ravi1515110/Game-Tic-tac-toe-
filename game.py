from tkinter import *
win=Tk()
win.configure(bg="green")
win.geometry("350x400")
win.title("Tic-Tac-Toe(Game)")
win.resizable(0,0)

c=1
def show(b):
    global c
    c=c+1
    if(c%2==0):
        if (b["text"]==""):
            b["text"]="O"

    else:
        if (b["text"] == ""):
            b["text"]="X"
    if(B1["text"]=="O" and B2["text"]=="O" and B3["text"]=="O"):
        print("1st player winner!!")
    elif(B1["text"]=="X" and B2["text"]=="X" and B3["text"]=="X"):
        print("2nd player winner!!!")

    elif (B4["text"] == "O" and B5["text"] == "O" and B6["text"] == "O"):
        print("1st player winner!!!")
    elif (B4["text"] == "X" and B5["text"] == "X" and B6["text"] == "X"):
        print("2nd player winner!!!")
    elif(B7["text"]=="O" and B8["text"]=="O" and B9["text"]=="O"):
        print("1st player winner!!")
    elif(B1["text"]=="O" and B4["text"]=="O" and B7["text"]=="O"):
        print("1st player winner!!")
    elif (B1["text"] == "X" and B4["text"] == "X" and B7["text"] == "X"):
        print("2nd player winner!!!")
    elif(B2["text"]=="O" and B5["text"]=="O" and B8["text"]=="O"):
        print("1st player winner!!")
    elif (B2["text"] == "X" and B5["text"] == "X" and B8["text"] == "X"):
        print("2nd player winner!!!")
    elif(B3["text"]=="O" and B6["text"]=="O" and B9["text"]=="O"):
        print("1st player winner!!")
    elif (B3["text"] == "X" and B6["text"] == "X" and B9["text"] == "X"):
        print("2nd player winner!!!")
    elif(B1["text"]=="O" and B5["text"]=="O" and B9["text"]=="O"):
        print("1st player winner!!")
    elif (B1["text"] == "X" and B5["text"] == "X" and B9["text"] == "X"):
        print("2nd player winner!!!")
    elif((B1["text"]=="O" or B1["text"]=="X") and (B2["text"]=="O" or B2["text"]=="X") and (B3["text"]=="O" or B3["text"]=="X") and (B4["text"]=="O" or B4["text"]=="X") and (B5["text"]=="O" or B5["text"]=="X") and (B6["text"]=="O" or B6["text"]=="X") and (B7["text"]=="O" or B7["text"]=="X") and (B8["text"]=="O" or B8["text"]=="X") and (B9["text"]=="O" or B9["text"]=="X")):
        print("Tie")

B1=Button(win,text="",width=10,height=4,font=("Arial",15),command=lambda:show(B1))
B1.place(x=0,y=0)
B2=Button(win,text="",width=10,height=4,font=("Arial",15),command=lambda:show(B2))
B2.place(x=120,y=0)
B3=Button(win,text="",width=10,height=4,font=("Arial",15),command=lambda:show(B3))
B3.place(x=240,y=0)
B4=Button(win,text="",width=10,height=4,font=("Arial",15),command=lambda:show(B4))
B4.place(x=0,y=109)
B5=Button(win,text="",width=10,height=4,font=("Arial",15),command=lambda:show(B5))
B5.place(x=120,y=109)
B6=Button(win,text="",width=10,height=4,font=("Arial",15),command=lambda:show(B6))
B6.place(x=240,y=109)
B7=Button(win,text="",width=10,height=4,font=("Arial",15),command=lambda:show(B7))
B7.place(x=0,y=218)
B8=Button(win,text="",width=10,height=4,font=("Arial",15),command=lambda:show(B8))
B8.place(x=120,y=218)
B9=Button(win,text="",width=10,height=4,font=("Arial",15),command=lambda:show(B9))
B9.place(x=240,y=218)
win.mainloop()





















