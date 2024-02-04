from tkinter import *



# ===== Definations =====
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
    
    win2 = Tk()
    win2.config(bg="yellow")
    win2.geometry(f"{ww}x{wh}+{wx}+{wy}")
    
    
    lbl_score = Label(win2,text="Score : ",font="Arial 10",bg="yellow")
    lbl_score.place(x=10,y=10)
    
    
    lbl_time = Label(win2,text="Time : ",font="Arial 10",bg="yellow")
    lbl_time.place(x=410,y=10)
    
    
    lbl_question = Label(win2,text="question",font="Arial 20 bold",bg="yellow")
    lbl_question.place(x=180,y=50)
    
    
    btn1 = Button(win2,text="1",font="Arial 10 bold",height=1,width=5)
    btn1.place(x=215,y=120)
    
    
    btn2 = Button(win2,text="2",font="Arial 10 bold",height=1,width=5)
    btn2.place(x=215,y=160)
    
    
    btn3 = Button(win2,text="3",font="Arial 10 bold",height=1,width=5)
    btn3.place(x=215,y=200)
    
    
    win2.mainloop()
    
    
    
def help():
    guid_window = Toplevel(root)
    guid_window.title("guide page")
    lbl_guid = Label(guid_window,
                     text="This a guide for game and other buttons...\n"\
                        "you should read the questions and you have time\n"\
                        "to answer the questions with above buttons if you choose\n"\
                        "you will achive a score if you aswer all of theme correct \n"\
                        "you will be winner Good Luck",
                     font="Arial 20 bold").pack()



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