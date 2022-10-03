import os
from tkinter import *
from PIL import Image , ImageTk
from main import main_level_one



def levels_menu():
    root = Tk()

    root.title("Harry Potter Game")
    root.geometry("1000x600+175+53")
    root.resizable(False,False)

    class MainSettings:
        def __init__(self) : pass



        def LevelButtons():

            def ButtonLevelOne():
                main_level_one()
            


                

            btn_level_one = Button(master=root,text="1",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00",command=ButtonLevelOne)
            btn_level_two = Button(master=root,text="2",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00")
            btn_level_three = Button(master=root,text="3",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00")
            btn_level_four = Button(master=root,text="4",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00")
            btn_level_five = Button(master=root,text="5",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00")


            btn_level_six = Button(master=root,text="6",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00")
            btn_level_seven = Button(master=root,text="7",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00")
            btn_level_eight = Button(master=root,text="8",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00")
            btn_level_nine = Button(master=root,text="9",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00")
            btn_level_ten = Button(master=root,text="10",font=("bold",15),width=7,height=3,bg="#3333CC",fg="#FFCC00")

            def place_buttons():
                btn_level_one.place(x=75,y=85)
                btn_level_two.place(x=220,y=85)
                btn_level_three.place(x=420,y=85)
                btn_level_four.place(x=620,y=85)
                btn_level_five.place(x=830,y=85)

                btn_level_six.place(x=75,y=375)
                btn_level_seven.place(x=220,y=375)
                btn_level_eight.place(x=420,y=375)
                btn_level_nine.place(x=620,y=375)
                btn_level_ten.place(x=820,y=375)

            place_buttons()

    load_bg = ImageTk.PhotoImage(Image.open("img/hogwarts-castle.jpg"))

    bg_label = Label(master=root,image=load_bg)
    bg_label.place(x=-3,y=0)

    MainSettings.LevelButtons()

    root.mainloop()