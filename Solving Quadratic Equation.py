import math
from tkinter import *

root =Tk()
root.title("Solving Quadratic Equation")

#img=PhotoImage(file='image.png')
#img1=Label(root, image= img)
#img1.grid(row = 0, column = 0, columnspan = 2,pady = 2)


A_in = Label(root, text="input A")
A_in.grid(row = 1, column = 0, pady = 2)

inputA = Entry(root, width=50)
inputA.grid(row = 1, column = 1, pady = 2)
inputA.get()

B_in = Label(root, text="input B")
B_in.grid(row = 2, column = 0, pady = 2)

inputB = Entry(root, width=50)
inputB.grid(row = 2, column = 1, pady = 2)
inputB.get()

C_in = Label(root, text="input C")
C_in.grid(row = 3, column = 0, pady = 2)

inputC = Entry(root, width=50)
inputC.grid(row = 3, column = 1, pady = 2)
inputC.get()

ans_out = Label(root, text="Answer")
ans_out.grid(row = 5, column = 0, pady = 2)

output1 = Entry(root, width=50)
output1.grid(row = 5, column = 1, pady = 2)

ans = ("") 

def solve():
    a = float(inputA.get())
    b = float(inputB.get())
    c = float(inputC.get())
    
    d = (b**2)-4*a*c # discriminant
  
    
    if d < 0:
        ans =("This equation has no real solution")
    elif d == 0:
        x = (-b+math.sqrt(b**2-4*a*c))/2*a
        ans = ("This equation has one solutions: "), x
    else:
        x1 = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
        x2 = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
        ans = ("This equation has two solutions: ", x1, " or", x2)
    output1.insert(0, ans )

def clear():
    inputA.delete(0, END)
    inputB.delete(0, END)
    inputC.delete(0, END)
    output1.delete(0, END)
    
button1 =Button(root, text = "clear", command=clear, bg='red')
button1.grid(row = 4, column = 0, pady = 2)
    
button =Button(root, text = "Calculate", command=solve, bg='lime')
button.grid(row = 4, column = 1, pady = 2)
    
root.mainloop()
#by lstefanlombard