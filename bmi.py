from tkinter import *
from tkinter import PhotoImage, Tk, ttk

c1 = "#444466"
c2 = "#feffff"
c3 = "purple"

window = Tk()
window.title("bodyMassIndex")
photo = PhotoImage(file = "icon.png")
window.iconphoto(False, photo)
window.geometry("295x175")
window.resizable(width = False , height = False)
window.configure(bg = c2)
# upframe
top = Frame(window , width = 300 , height = 50 , bg = "yellow")
top.grid(row = 0, column = 0)
# downframe
down = Frame(window , width = 300 , height = 180 , bg = c2)
down.grid(row = 1, column = 0)

# appname
appName = Label(top, text = "BMI Calculator", width = 23 , height = 1, padx = 0 ,  anchor="center",bg="yellow",fg =c1,font = ("Ivy 12 bold"))
appName.place(x = 40 , y = 15)

# calculate function 
def calculate():
    weight = float(e_weight.get())
    height = float(e_height.get())**2
    result = weight/height

    if result<18.4:
        l_cal_text['text']= "your BMI is underwight"
    elif result>=18.5 and result<24.9:
        l_cal_text['text']= "your BMI is Normal"
    elif result>=25 and result<29:
        l_cal_text['text']= "your BMI is Overweight"
    elif result>=30:
        l_cal_text['text']= "Obesity"

        l_cal['text']="{:.{}f}".format(result,2)

# weight
l_weight = Label(down,text = "Enter Your Weight", height =1 , padx = 0,anchor = "center",font = ("ivy 10 bold"), bg = c2 , fg = "black")
l_weight.grid(row = 0 , column = 0,columnspan =1,pady = 10 ,padx = 3)
# entry
e_weight =Entry(down , width = 5 , font = ("ivy 10 bold"), justify = "center" , relief = "solid")
e_weight.grid(row = 0 , column = 1,columnspan = 1, pady = 10,padx = 3)
# height
l_height = Label(down,text = "Enter Your Height", height =1 , padx = 0,anchor = "center",font = ("ivy 10 bold"), bg = c2 , fg = "black")
l_height.grid(row = 1 , column = 0,columnspan =1,pady = 10 ,padx = 3)
# entry
e_height =Entry(down , width = 5 , font = ("ivy 10 bold"), justify = "center" , relief = "solid")
e_height.grid(row = 1 , column = 1,columnspan = 1, pady = 10,padx = 3)
# result
l_cal=Label(down , width = 10 , text ="-",height = 3 , padx =  6, pady = 5, anchor = "center", font = ("ivy 12 bold"),bg= c3,fg =c2)
l_cal.place(x=175, y =10)

l_cal_text=Label(down , width = 30 , text ="",height = 1 , padx = 6 , pady = 8 , anchor = "center", font = ("ivy 24 bold"),bg= c2,fg =c2)
l_cal_text.place(x=0, y =85)
b_calculate=Button(down,text = "Calculate" , width = 30 , height = 1 ,bg = c2, fg = c1 , font = ("Ivy 10 bold"), anchor = "center",command =calculate)
b_calculate.grid(row = 4 , column = 0,pady = 0,padx = 5,columnspan=30)
window.mainloop()