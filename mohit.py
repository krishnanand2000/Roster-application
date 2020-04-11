import tkinter
from tkinter import *
from tkinter import messagebox

def main_window():
    wdw = tkinter.Tk()
    wdw.title("Roster Application")
    frame  = Frame(wdw, bd= 10 , height = 1080 , width = 720)
    frame.pack()

    black_label = Label(frame, text = "Welcome to Roster Application" , justify = CENTER , bg = 'CYAN' , borderwidth = 5)
    black_label.grid(row = 0 , column = 3)

    label_name = Label(frame, text = "Enter Name" , justify = LEFT )
    label_name.grid(row = 1, column = 1)
    global name_enty 
    name_enty =  Entry(frame , justify = LEFT)
    name_enty.grid(row = 1, column = 2)

    label_desg = Label(frame , text = "Enter designation", justify = LEFT)
    label_desg.grid(row = 1 , column = 3)
    global desg_enty 
    desg_enty = Entry(frame , justify = LEFT)
    desg_enty.grid(row = 1 , column = 4 )

    label_time = Label(frame , text = "Time:", justify = LEFT)
    label_time.grid(row = 3 , column = 1)

    label_8 = Label(frame , text = "08:00", justify = LEFT)
    label_8.grid(row = 3 , column = 2)

    label_9 = Label(frame , text = "09:00", justify = LEFT)
    label_9.grid(row = 3 , column = 3)

    label_10 = Label(frame , text = "10:00", justify = LEFT)
    label_10.grid(row = 3 , column = 4)

    label_11 = Label(frame , text = "11:00", justify = LEFT)
    label_11.grid(row = 3 , column = 5)

    label_day1 = Label(frame , text = "Monday", justify = LEFT)
    label_day1.grid(row = 4 , column = 1)

    label_day2 = Label(frame , text = "Tuesday", justify = LEFT)
    label_day2.grid(row = 5 , column = 1)

    label_day3 = Label(frame , text = "Wednesday", justify = LEFT)
    label_day3.grid(row = 6 , column = 1)

    label_day4 = Label(frame , text = "Thrusday", justify = LEFT)
    label_day4.grid(row = 7 , column = 1)

    label_day4 = Label(frame , text = "Friday", justify = LEFT)
    label_day4.grid(row = 8 , column = 1)

    global entry11 
    entry11 = Entry(frame , justify = LEFT)
    entry11.grid(row = 4 , column = 2) 

    global entry12 
    entry12 = Entry(frame , justify = LEFT)
    entry12.grid(row = 4 , column = 3) 

    global entry13 
    entry13 = Entry(frame , justify = LEFT)
    entry13.grid(row = 4 , column = 4) 
    
    global entry14
    entry14 = Entry(frame , justify = LEFT)
    entry14.grid(row = 4 , column = 5) 

    global entry21
    entry21 = Entry(frame , justify = LEFT)
    entry21.grid(row = 5 , column = 2) 

    global entry22
    entry22 = Entry(frame , justify = LEFT)
    entry22.grid(row = 5 , column = 3)

    global entry23
    entry23 = Entry(frame , justify = LEFT)
    entry23.grid(row = 5 , column = 4)

    global entry24
    entry24 = Entry(frame , justify = LEFT)
    entry24.grid(row = 5 , column = 5)

    global entry31
    entry31 = Entry(frame , justify = LEFT)
    entry31.grid(row = 6 , column = 2)

    global entry32
    entry32 = Entry(frame , justify = LEFT)
    entry32.grid(row = 6 , column = 3)

    global entry33
    entry33 = Entry(frame , justify = LEFT)
    entry33.grid(row = 6 , column = 4)

    global entry34
    entry34 = Entry(frame , justify = LEFT)
    entry34.grid(row = 6 , column = 5)

    global entry41
    entry41 = Entry(frame , justify = LEFT)
    entry41.grid(row = 7 , column = 2)
    
    global entry42
    entry42 = Entry(frame , justify = LEFT)
    entry42.grid(row = 7 , column = 3)

    global entry43
    entry43 = Entry(frame , justify = LEFT)
    entry43.grid(row = 7 , column = 4)

    global entry44
    entry44 = Entry(frame , justify = LEFT)
    entry44.grid(row = 7 , column = 5)

    global entry51
    entry51 = Entry(frame , justify = LEFT)
    entry51.grid(row = 8 , column = 2)

    global entry52
    entry52 = Entry(frame , justify = LEFT)
    entry52.grid(row = 8 , column = 3)

    global entry53
    entry53 = Entry(frame , justify = LEFT)
    entry53.grid(row = 8 , column = 4)

    global entry54
    entry54 = Entry(frame , justify = LEFT)
    entry54.grid(row = 8 , column = 5)

    button=Button(frame,text="Submit",justify=CENTER,borderwidth=10,cursor="arrow",)
    button.grid(row=9,column = 3)
    wdw.mainloop()


main_window()
