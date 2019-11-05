from tkinter import *
import msvcrt

expression=""
ans=0

def num(n):
 global expression
 g=str(n)
 expression=expression+g
 exp=expression
 i=Entry(frame1,justify=RIGHT)
 i.insert(0,exp)
 i.grid(row=0,column=0,sticky=N)
def nu(s):
 global expression
 expression=expression+s
 k=Entry(frame1,justify=RIGHT)
 k.insert(0,expression)
 k.grid(row=0,column=0,sticky=N)
def cl(frame1):
	global expression
	expression=" "
	o=Entry(frame1,justify=RIGHT)
	o.insert(0,expression)
	o.grid(row=0,column=0,sticky=N)
    
def back(frame1) :
	global expression
	expression=expression[:-1]
	k=Entry(frame1,justify=RIGHT)
	k.insert(0,expression)
	k.grid(row=0,column=0,sticky=N)

def equal(frame1):
 global expression
 global ans
 ans=eval(expression)
 expression=str(ans)
 l=Entry(frame1,justify=RIGHT)
 l.insert(0,str(ans))
 l.grid(row=0,column=0,sticky=N)

root=Tk()
root.title('CALCULATOR')
frame1=Frame(root,width=400,height=70)
frame1.grid()
p=Entry(frame1)
p.insert(0,"")
p.grid(row=0,column=0,sticky=N)
while msvcrt.kbhit():
    msvcrt.getwch()
    char = msvcrt.getwch()
    if char == '\b':
    	back(root)
    elif char=='':
    	equal(root)
    else :
    	num(char)
button1=Button(root,text=' 1 ',command=lambda : num(1))
button1.grid(row=2,column=0)
button2=Button(root,text=' 2 ',command=lambda : num(2))
button2.grid(row=2,column=1)
button3=Button(root,text=' 3 ',command=lambda : num(3))
button3.grid(row=2,column=2)
button4=Button(root,text=' 4 ',command=lambda : num(4))
button4.grid(row=3,column=0)
button5=Button(root,text=' 5 ',command=lambda : num(5))
button5.grid(row=3,column=1)
button6=Button(root,text=' 6 ',command=lambda : num(6))
button6.grid(row=3,column=2)
button7=Button(root,text=' 7 ',command=lambda : num(7))
button7.grid(row=4,column=0)
button8=Button(root,text=' 8 ',command=lambda : num(8))
button8.grid(row=4,column=1)
button9=Button(root,text=' 9 ',command=lambda : num(9))
button9.grid(row=4,column=2)
button10=Button(root,text=' <-- ',command=lambda : back(root))
button10.grid(row=1,column=0)
button11=Button(root,text=' C ',command=lambda :cl(root))
button11.grid(row=1,column=1)
button12=Button(root,text=' = ',command=lambda :equal(root))
button12.grid(row=1,column=2)
button13=Button(root,text=' + ',command=lambda :nu("+"))
button13.grid(row=1,column=4)
button14=Button(root,text=' - ',command=lambda :nu("-"))
button14.grid(row=2,column=4)
button15=Button(root,text=' * ',command=lambda :nu("*"))
button15.grid(row=3,column=4)
button16=Button(root,text=' / ',command=lambda :nu("/"))
button16.grid(row=4,column=4)
root.mainloop()

