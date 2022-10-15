import customtkinter
# from PIL import Image, ImageTk
import os
import Module_TicTacToe as g1
import Module_Bingo as g2

PATH = os.path.dirname(os.path.realpath(__file__))

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class Game_template(customtkinter.CTkFrame):
    def __init__(self, *args, header_name="Games", **kwargs):
        super().__init__(*args, **kwargs)
        
        self.header_name = header_name

        self.frame0 = customtkinter.CTkFrame(master=self)
        self.frame0.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

        self.label_1 = customtkinter.CTkLabel(master=self.frame0, text=self.header_name)
        self.label_1.pack(pady=12, padx=10)

        self.label_1 = customtkinter.CTkLabel(master=self.frame0, text="Game under development")
        self.label_1.pack(pady=12, padx=10)

class App(customtkinter.CTk):

    APP_NAME = "CustomTkinter example_background_image.py"
    WIDTH = 900
    HEIGHT = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title(App.APP_NAME)
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)
        # self.maxsize(App.WIDTH, App.HEIGHT)

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,width=180,corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(7, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        ####### adding widget to left frame ###
        self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="CustomTkinter", text_font=("Roboto Medium", -16))
        self.label_1.grid(row=1, column=0, pady=10, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left, text="Tic Tac Toe", height=32, compound="right", command=lambda: self.select_game(self.game_1_frame,0,1))
        self.button_1.grid(row=2, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="ew")

        self.button_2 = customtkinter.CTkButton(master=self.frame_left, text="Bingo", height=32, compound="right", command=lambda: self.select_game(self.game_2_frame,0,1))
        self.button_2.grid(row=3, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        self.button_3 = customtkinter.CTkButton(master=self.frame_left, text="Dots and Boxes", height=32, compound="right", command=lambda: self.select_game(self.game_3_frame,0,1))
        self.button_3.grid(row=4, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        self.button_4 = customtkinter.CTkButton(master=self.frame_left, text="Sudoku", height=32, compound="right", command=lambda: self.select_game(self.game_4_frame,0,1))
        self.button_4.grid(row=5, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        self.button_4 = customtkinter.CTkButton(master=self.frame_left, text="Ludo", height=32, compound="right", command=lambda: self.select_game(self.game_5_frame,0,1))
        self.button_4.grid(row=6, column=0, columnspan=2, padx=20, pady=10, sticky="ew")

        self.optionmenu_theme = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Light", "Dark", "System"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_theme.grid(row=20, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        self.game_1_frame = g1.Game_TicTacToe(self.frame_right, header_name="Tic Tac Toe")
        self.game_2_frame = g2.Game_Bingo(self.frame_right, header_name="Bingo")
        self.game_3_frame = Game_template(self.frame_right, header_name="Dots And Boxes")
        self.game_4_frame = Game_template(self.frame_right, header_name="Sudoku")
        self.game_5_frame = Game_template(self.frame_right, header_name="Ludo")

    def button_function(self):
        print("button pressed")

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def select_game(self, widget,row_num, col_num):
        if widget == self.game_1_frame:
            self.game_1_frame.pack(padx=20, pady=20)
            self.game_2_frame.pack_forget()
            self.game_3_frame.pack_forget()
            self.game_4_frame.pack_forget()
            self.game_5_frame.pack_forget()
        elif widget == self.game_2_frame:
            self.game_2_frame.pack(padx=20, pady=20)
            self.game_1_frame.pack_forget()
            self.game_3_frame.pack_forget()
            self.game_4_frame.pack_forget()
            self.game_5_frame.pack_forget()
        elif widget == self.game_3_frame:
            self.game_3_frame.pack( padx=20, pady=20)
            self.game_1_frame.pack_forget()
            self.game_2_frame.pack_forget()
            self.game_4_frame.pack_forget()
            self.game_5_frame.pack_forget()
        elif widget == self.game_4_frame:
            self.game_4_frame.pack(padx=20, pady=20)
            self.game_1_frame.pack_forget()
            self.game_2_frame.pack_forget()
            self.game_3_frame.pack_forget()
            self.game_5_frame.pack_forget()
        elif widget == self.game_5_frame:
            self.game_5_frame.pack(padx=20, pady=20)
            self.game_1_frame.pack_forget()
            self.game_2_frame.pack_forget()
            self.game_3_frame.pack_forget()
            self.game_4_frame.pack_forget()

if __name__ == "__main__":
    app = App()
    app.mainloop()
