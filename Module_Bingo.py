from tkinter import *
from tkinter import messagebox
import customtkinter
import random

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "green" (standard), "green", "dark-blue"

box = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

play_status = False
count = 0
num_i = 0
num_v = 1
score_count = 0
click_count = 0
score_i = 0
score_Baoad = [" ","B","I","N","G","O"]
row_1, row_2, row_3, row_5, row_5 = False, False, False, False, False
col_1, col_2, col_3, col_4, col_5 = False, False, False, False, False
dia_1, dia_2 = False, False

class Game_Bingo(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Games", **kwargs):
        super().__init__(*args, **kwargs)

        self.header_name = header_name

        self.frame1 = customtkinter.CTkFrame(master=self)
        self.frame1.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        self.frame1_1 = customtkinter.CTkFrame(master=self.frame1)
        self.frame1_1.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        ## right side

        self.frame_control = customtkinter.CTkFrame(master=self)
        self.frame_control.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        self.label_1 = customtkinter.CTkLabel(master=self.frame_control, text="Game Controls")
        self.label_1.grid(row=0, column=0, pady=12, padx=5)

        self.frame_inside = customtkinter.CTkFrame(master=self.frame_control)
        self.frame_inside.grid(row=2, column=0, padx=10, pady= 10)

        self.score_label= customtkinter.CTkLabel(master=self.frame_inside, text="Score board")
        self.score_label.grid(row=0, column=0, pady=5, padx=15)

        self.score_1= Button(master=self.frame_inside, text=" ", width=3, command=lambda: self.scoreDispManual(self.score_1))
        self.score_2= Button(master=self.frame_inside, text=" ", width=3, command=lambda: self.scoreDispManual(self.score_2))
        self.score_3= Button(master=self.frame_inside, text=" ", width=3, command=lambda: self.scoreDispManual(self.score_3))
        self.score_4= Button(master=self.frame_inside, text=" ", width=3, command=lambda: self.scoreDispManual(self.score_4))
        self.score_5= Button(master=self.frame_inside, text=" ", width=3, command=lambda: self.scoreDispManual(self.score_5))

        self.switch_var = customtkinter.StringVar(value="off")

        self.switch_1 = customtkinter.CTkSwitch(master=self.frame_control, text="Auto Checking Mode", variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch_1.grid(row=3, column=0, padx=20, pady= 20, sticky="w")

        self.autoNumBtn= customtkinter.CTkButton(master=self.frame_control, text="Auto Numbering", bg="SystemButtonFace", command=self.autoNumbering)
        self.autoNumBtn.grid(row=4, column=0, padx=20, pady= 10)

        self.resetbtn= customtkinter.CTkButton(master=self.frame_control, text="Reset", bg="SystemButtonFace", command=self.reset)
        self.resetbtn.grid(row=9, column=0, padx=10, pady= 10)

        self.playbtn= customtkinter.CTkButton(master=self.frame_control, text="Start", state="disabled", bg="SystemButtonFace", command=self.runplay)
        self.playbtn.grid(row=10, column=0, padx=10, pady= 10)

        self.reset()

    # Start the game over!
    def reset(self):
        global b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b12,b13,b14,b15,b16,b17,b18,b19,b20,b21,b22,b23,b24,b25
        global count, num_i, num_v ,play_status, score_count, score_i, click_count
        global score_count, row_1, row_2, row_3, row_5, row_5, col_1, col_2, col_3, col_4, col_5, dia_1, dia_2
        
        if play_status == True:
            print("Rest applied")

        play_status = False
        count = 0
        num_i = 0
        num_v = 1
        score_count = 0
        click_count = 0
        score_i = 0
        row_1, row_2, row_3, row_5, row_5 = False, False, False, False, False
        col_1, col_2, col_3, col_4, col_5 = False, False, False, False, False
        dia_1, dia_2 = False, False

        self.score_1["text"] = " "
        self.score_2["text"] = " "
        self.score_3["text"] = " "
        self.score_4["text"] = " "
        self.score_5["text"] = " "

        self.score_label.grid(row=0, column=0, pady=5, padx=10)

        self.score_1.grid_forget()
        self.score_2.grid_forget()
        self.score_3.grid_forget()
        self.score_4.grid_forget()
        self.score_5.grid_forget()

        self.playbtn.configure(state="disabled")
        self.autoNumBtn.configure(state="normal")

        # label_100 = Label(self.frame1_1, test="test")
        # label_100.grid(row=0, column=0)

        ## Build our buttons
        b1  = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b1))
        b2  = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b2))
        b3  = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b3))
        b4  = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b4))
        b5  = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b5))
        b6  = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b6))
        b7  = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b7))
        b8  = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b8))
        b9  = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b9))
        b10 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b10))
        b11 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b11))
        b12 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b12))
        b13 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b13))
        b14 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b14))
        b15 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b15))
        b16 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b16))
        b17 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b17))
        b18 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b18))
        b19 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b19))
        b20 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b20))
        b21 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b21))
        b22 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b22))
        b23 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b23))
        b24 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b24))
        b25 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=1, width=3, bg="SystemButtonFace", command=lambda: self.b_click(b25))

        # Grid our buttons to the screen
        b1.grid(row=0, column=0)
        b2.grid(row=0, column=1)
        b3.grid(row=0, column=2)
        b4.grid(row=0, column=3)
        b5.grid(row=0, column=4)

        b6.grid(row=1, column=0)
        b7.grid(row=1, column=1)
        b8.grid(row=1, column=2)
        b9.grid(row=1, column=3)
        b10.grid(row=1, column=4)
        
        b11.grid(row=2, column=0)
        b12.grid(row=2, column=1)
        b13.grid(row=2, column=2)
        b14.grid(row=2, column=3)
        b15.grid(row=2, column=4)

        b16.grid(row=3, column=0)
        b17.grid(row=3, column=1)
        b18.grid(row=3, column=2)
        b19.grid(row=3, column=3)
        b20.grid(row=3, column=4)

        b21.grid(row=4, column=0)
        b22.grid(row=4, column=1)
        b23.grid(row=4, column=2)
        b24.grid(row=4, column=3)
        b25.grid(row=4, column=4)

    def autoNumbering(self):
        global box1, click_count

        box1 = box[:]
        random.shuffle(box1)

        b1.configure(text=str(box1[0]))
        b2.configure(text=str(box1[1]))
        b3.configure(text=str(box1[2]))
        b4.configure(text=str(box1[3]))
        b5.configure(text=str(box1[4]))
        b6.configure(text=str(box1[5]))
        b7.configure(text=str(box1[6]))
        b8.configure(text=str(box1[7]))
        b9.configure(text=str(box1[8]))
        b10.configure(text=str(box1[9]))
        b11.configure(text=str(box1[10]))
        b12.configure(text=str(box1[11]))
        b13.configure(text=str(box1[12]))
        b14.configure(text=str(box1[13]))
        b15.configure(text=str(box1[14]))
        b16.configure(text=str(box1[15]))
        b17.configure(text=str(box1[16]))
        b18.configure(text=str(box1[17]))
        b19.configure(text=str(box1[18]))
        b20.configure(text=str(box1[19]))
        b21.configure(text=str(box1[20]))
        b22.configure(text=str(box1[21]))
        b23.configure(text=str(box1[22]))
        b24.configure(text=str(box1[23]))
        b25.configure(text=str(box1[24]))

        self.playbtn.configure(state="normal")

        click_count = 5
        print("random box printed")

    def b_click(self,b):
        global count, num_i, play_status, auto_mode, click_count

        auto_mode = self.switch_var.get()

        if play_status == False:
            if b["text"] == " ":
                b["text"] = str(box[num_i])
                num_i = num_i + 1
                click_count += 1
                # print("index : ",num_i)
                if num_i == 10:
                    self.playbtn.configure(state="normal")
            elif b["text"] != " " and click_count == 25:
                messagebox.showerror("Bingo", "You didn't pressed the start button,\nYou need to press it to start the game" )
            else:
                messagebox.showerror("Bingo", "Hey! That box has already been selected\nPick Another Box..." )
        
        if play_status == True:
            if b["bg"] != "red":
                b.config(bg="red")
                count += 1
                
                if auto_mode == "on": 
                    self.checkifwon()
            else:
                messagebox.showerror("Worng Box","Hey! That box has already been selected\nPick Another Box..." )

    def runplay(self):
        global  play_status,auto_mode, click_count
        play_status = True
        click_count = 0
        print("game Started")
        self.playbtn.configure(state="disabled")
        self.autoNumBtn.configure(state="disabled")
        self.score_label.grid_forget()

        self.score_1.grid(row=0, column=0, padx=5, pady= 10)
        self.score_2.grid(row=0, column=1, padx=5, pady= 10)
        self.score_3.grid(row=0, column=2, padx=5, pady= 10)
        self.score_4.grid(row=0, column=3, padx=5, pady= 10)
        self.score_5.grid(row=0, column=4, padx=5, pady= 10)

        auto_mode = self.switch_var.get()
        
        if auto_mode == "on":
            self.score_1.config(state=DISABLED)
            self.score_2.config(state=DISABLED)
            self.score_3.config(state=DISABLED)
            self.score_4.config(state=DISABLED)
            self.score_5.config(state=DISABLED)
        else:
            self.score_1.config(state=NORMAL)
            self.score_2.config(state=NORMAL)
            self.score_3.config(state=NORMAL)
            self.score_4.config(state=NORMAL)
            self.score_5.config(state=NORMAL)

    def checkifwon(self):
        global score_count, score_i, row_1, row_2, row_3, row_5, row_5, col_1, col_2, col_3, col_4, col_5, dia_1, dia_2
        

        if b1["bg"] == "red" and b2["bg"] == "red" and b3["bg"] == "red" and b4["bg"] == "red" and b5["bg"] == "red" and row_1 == False:
            row_1 = True
            score_count += 1
        if b6["bg"] == "red" and b7["bg"] == "red" and b8["bg"] == "red" and b9["bg"] == "red" and b10["bg"] == "red" and row_2 == False:
            row_2 = True
            score_count += 1
        if b11["bg"] == "red" and b12["bg"] == "red" and b13["bg"] == "red" and b14["bg"] == "red" and b15["bg"] == "red" and row_3 == False:
            row_3 = True
            score_count += 1
        if b16["bg"] == "red" and b17["bg"] == "red" and b18["bg"] == "red" and b19["bg"] == "red" and b20["bg"] == "red" and row_4 == False:
            row_4 = True
            score_count += 1
        if b21["bg"] == "red" and b22["bg"] == "red" and b22["bg"] == "red" and b24["bg"] == "red" and b25["bg"] == "red" and row_5 == False:
            row_5 = True
            score_count += 1
        if b21["bg"] == "red" and b1["bg"] == "red" and b6["bg"] == "red" and b11["bg"] == "red" and b16["bg"] == "red" and col_1 == False:
            col_1 = True
            score_count += 1
        if b22["bg"] == "red" and b2["bg"] == "red" and b7["bg"] == "red" and b12["bg"] == "red" and b17["bg"] == "red" and col_2 == False:
            col_2 = True
            score_count += 1
        if b23["bg"] == "red" and b3["bg"] == "red" and b8["bg"] == "red" and b13["bg"] == "red" and b18["bg"] == "red" and col_3 == False:
            col_3 = True
            score_count += 1
        if b24["bg"] == "red" and b4["bg"] == "red" and b9["bg"] == "red" and b14["bg"] == "red" and b19["bg"] == "red" and col_4 == False:
            col_4 = True
            score_count += 1
        if b25["bg"] == "red" and b5["bg"] == "red" and b10["bg"] == "red" and b15["bg"] == "red" and b20["bg"] == "red" and col_5 == False:
            col_5 = True
            score_count += 1
        if b1["bg"] == "red" and b7["bg"] == "red" and b13["bg"] == "red" and b19["bg"] == "red" and b25["bg"] == "red" and dia_1 == False:
            dia_1 = True
            score_count += 1
        if b5["bg"] == "red" and b9["bg"] == "red" and b13["bg"] == "red" and b17["bg"] == "red" and b21["bg"] == "red" and dia_2 == False:
            dia_2 = True
            score_count += 1

        print("score count : ", score_count)

        if score_count == 1:
            self.score_1["text"] = str(score_Baoad[score_count])
        elif score_count == 2:
            self.score_1["text"] = str(score_Baoad[score_count-1])
            self.score_2["text"] = str(score_Baoad[score_count])
        elif score_count == 3:
            self.score_1["text"] = str(score_Baoad[score_count-2])
            self.score_2["text"] = str(score_Baoad[score_count-1])
            self.score_3["text"] = str(score_Baoad[score_count])
        elif score_count == 4:
            self.score_1["text"] = str(score_Baoad[score_count-3])
            self.score_2["text"] = str(score_Baoad[score_count-2])
            self.score_3["text"] = str(score_Baoad[score_count-1])
            self.score_4["text"] = str(score_Baoad[score_count])
        elif score_count == 5:
            self.score_1["text"] = str(score_Baoad[score_count-4])
            self.score_2["text"] = str(score_Baoad[score_count-3])
            self.score_3["text"] = str(score_Baoad[score_count-2])
            self.score_4["text"] = str(score_Baoad[score_count-1])
            self.score_5["text"] = str(score_Baoad[score_count])

        if score_count >= 5:
            messagebox.showinfo("***BINGO***", "CONGRATULATIONS!")

        # Check if tie
        if count == 25:
            messagebox.showinfo("It's A Tie!\n No One Wins!")

    def scoreDispManual(self,score):
        global score_i, click_count, score_Baoad
        global auto_mode

        auto_mode = self.switch_var.get()

        
        if auto_mode == "off":
            if score["text"] == " ":
                score_i +=1
                print (score_i)
                score["text"] = str(score_Baoad[score_i])
            else:
                messagebox.showerror("Bingo","Unable to set value" )

            if score_i == 5:
                messagebox.showinfo("***BINGO***", "CONGRATULATIONS!")
                self.score_1.config(state=DISABLED)
                self.score_2.config(state=DISABLED)
                self.score_3.config(state=DISABLED)
                self.score_4.config(state=DISABLED)
                self.score_5.config(state=DISABLED)


class App(customtkinter.CTk):

    APP_NAME = "CustomTkinter example_background_image.py"
    WIDTH = 900
    HEIGHT = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        # self.minsize(App.WIDTH, App.HEIGHT)
        # self.maxsize(App.WIDTH, App.HEIGHT)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                width=180,
                                                corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="CustomTkinter", text_font=("Roboto Medium", -16))
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,text="Play",command=lambda: self.show_frame(self.game_1_frame))
        self.button_1.grid(row=2, column=0, pady=10, padx=20)

        self.game_1_frame = Game_Bingo(self.frame_right, header_name="Game 1")

    def show_frame(self,widget,):
        widget.grid(row=0, column=2, padx=20, pady=20)
    
    def on_closing(self, event=0):
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()
