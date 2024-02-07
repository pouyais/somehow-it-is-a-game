from tkinter import *
from tkinter import messagebox
import random


# ===== variables =====
time = 0
b = 0
s = 0



# ===== Definitions =====
def color():
    
    
    # ===== Defination =====
    def changecolor():
        selected_color = v.get()
        
        if selected_color == 1:
            win.config(bg="red")
        elif selected_color == 2:
            win.config(bg="blue")
        elif selected_color == 3:
            win.config(bg="yellow")
        elif selected_color == 4:
            win.config(bg="green")
        else:
            pass
        
        for btn in radio_buttons:
            btn.configure(bg=colors[selected_color])
    
    # ===== UI Design =====
    win = Tk()
    win.config(bg="#1EECB1")
    win.geometry(f"{ww}x{wh}+{wx}+{wy}")
    
    
    v = IntVar(win,value=0)
    
    colors = {1 : "red" , 2 : "blue" , 3 : "yellow" , 4 : "green"}
  
    radio_buttons = []
    Options = {"Red" : 1 ,"Blue" : 2 ,"Yellow" : 3 ,"Green" : 4}
    for txt,val in Options.items():
        rdbtn = Radiobutton(win,text=txt,value=val,variable=v,bg="#1EECB1",font="tahoma 15 bold")
        rdbtn.pack(side=TOP)
        radio_buttons.append(rdbtn)
       
        
    btn_change_color = Button(win,text="Change",font="Arial 15 bold",bg="grey",command=changecolor)
    btn_change_color.pack(side=TOP)
    
    win.mainloop()
    

def game():
    
    
    # ===== Definition =====
    def start():
        global time
        time = 60
        countdown()
        begin()
        
      
    def countdown():
        global time
        global s    
        if time > 0:
            btn_start.config(state=DISABLED)
            btn1.config(state=NORMAL)
            btn2.config(state=NORMAL)
            btn3.config(state=NORMAL)
            lbl_counter.config(text=time,bg="yellow",fg="red",font="Arial 14 bold")
            time -= 1
            lbl_counter.after(1000,countdown)
            if time == 0:
                lbl_counter.config(text="0")
                lbl_score_number.config(text="0")
                btn_start.config(state=NORMAL)
                btn1.config(state=DISABLED)
                btn2.config(state=DISABLED)
                btn3.config(state=DISABLED)
                messagebox.showinfo(win2,message=f"Your score is {s}!")
                s  = 0   
             
              
                
    def begin():
        global b
        global s
        qs = ["1+2", "3-1", "1+1", "3-2", "2-1", "2+1"]
        Eq = random.choice(qs)
        b = eval(Eq)
        lbl_question.config(text=Eq)
                        
            
    def btn11():
        global b
        global s
        qs = ["1+2","3-1","1+1","3-2","2-1","2+1"]
        Eq = random.choice(qs)
        lbl_question.config(text=Eq)
        a = 1
        
        if a == b:
            s += 1
            lbl_score_number.config(text=s,bg="yellow",fg="green",font="Arial 14 bold")
        else:
            pass
        
        b = eval(Eq)
        
        
    def btn22():
        global b
        global s
        qs = ["1+2","3-1","1+1","3-2","2-1","2+1"]
        Eq = random.choice(qs)
        lbl_question.config(text=Eq)
        a = 2

        if a == b:
            s += 1
            lbl_score_number.config(text=s,bg="yellow",fg="green",font="Arial 14 bold")
        else:
            pass
        
        b = eval(Eq)
        
        
    def btn33():
        global b
        global s
        qs = ["1+2","3-1","1+1","3-2","2-1","2+1"]
        Eq = random.choice(qs)
        lbl_question.config(text=Eq)
        a = 3 

        if a == b:
            s += 1
            lbl_score_number.config(text=s,bg="yellow",fg="green",font="Arial 14 bold")
        else:
            pass
            
        b = eval(Eq)
        
    
    # ===== UI Design =====
    win2 = Tk()
    win2.config(bg="yellow")
    win2.geometry(f"{ww}x{wh}+{wx}+{wy}")
    
    
    # ===== Labels =====
    lbl_score = Label(win2,text="Score : ",font="Arial 10",bg="yellow")
    lbl_score.place(x=10,y=14)
    
    
    lbl_score_number = Label(win2,text="0",font="Arial 14",bg="yellow")
    lbl_score_number.place(x=60,y=12)
    
    
    lbl_time = Label(win2,text="Time : ",font="Arial 10",bg="yellow")
    lbl_time.place(x=410,y=14)
    
    
    lbl_question = Label(win2,text="  Q",font="Arial 22 bold",bg="yellow")
    lbl_question.place(x=210,y=50)
    
    
    lbl_counter = Label(win2,height=1,width=3,text="60",font="Arial 14",bg="yellow")
    lbl_counter.place(x=450,y=10)
    
    
    # ===== Buttons =====    
    btn1 = Button(win2,text="1",font="Arial 10 bold",height=1,width=5,command=btn11,state=DISABLED)
    btn1.place(x=215,y=120)
    
    
    btn2 = Button(win2,text="2",font="Arial 10 bold",height=1,width=5,command=btn22,state=DISABLED)
    btn2.place(x=215,y=160)
    
    
    btn3 = Button(win2,text="3",font="Arial 10 bold",height=1,width=5,command=btn33,state=DISABLED)
    btn3.place(x=215,y=200)
    
    
    btn_start = Button(win2,text="start",font="Arial 10 bold",height=1,width=5,command=start)
    btn_start.place(x=90,y=250)
    
    win2.mainloop()
    
     
def help():
    guid_window = Toplevel(root)
    guid_window.title("guide page")
    lbl_guid = Label(guid_window,
                     text="This is a guide to using the app\n"\
                        "In the game you have to answer some specific\n"\
                        " questions with the buttons below the questions\n"\
                        "And if you answer the questions correctly\n"\
                        "you will get a point in the upper left corner with green color,\n"\
                        " and if your answer is wrong,\n"\
                        "you still have time, of course, until your time runs out,\n"\
                        "you have 60 seconds to answer the questions.\n"\
                        "I hope you win the game Good Luck...!",
                     font="Arial 20 bold",bg="lightblue").pack()


def exit():
    root.destroy()



root = Tk()
screen_w = root.winfo_screenwidth()
screen_h = root.winfo_screenheight()
cx = screen_w / 2
cy = screen_h / 2
ww = 500
wh = 300
wx = int(cx - ww / 2)
wy = int(cy - wh / 2)
root.config(bg="#807C7B")
root.geometry(f"{ww}x{wh}+{wx}+{wy}")

# ===== Labels =====
lbl_show = Label(text="!This a game by XKstudio!",font="Arial 15 bold",bg="#807C7B")
lbl_show.place(x=115,y=50)


# ===== Buttons =====
btn_colors = Button(root,text="Color",bg="#69EF06",font="tahoma 15 bold",height=1,width=5,command=color)
btn_colors.place(x=125,y=120)


btn_game = Button(root,text="Game",bg="#69EF06",font="tahoma 15 bold",height=1,width=5,command=game)
btn_game.place(x=280,y=120)


btn_help = Button(root,text="Help",bg="#69EF06",font="tahoma 15 bold",height=1,width=5,command=help)
btn_help.place(x=125,y=200)


btn_exit = Button(root,text="Exit",bg="#69EF06",font="tahoma 15 bold",height=1,width=5,command=exit)
btn_exit.place(x=280,y=200)


root.mainloop()