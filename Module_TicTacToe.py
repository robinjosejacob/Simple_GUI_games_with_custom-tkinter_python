from tkinter import *
from tkinter import messagebox
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "green" (standard), "green", "dark-blue"

class Game_TicTacToe(customtkinter.CTkFrame):
	# X starts so true
	clicked = True
	count = 0

	def __init__(self, *args, header_name="Games", **kwargs):
		super().__init__(*args, **kwargs)

		self.header_name = header_name

		self.header_name = header_name

		self.frame0 = customtkinter.CTkFrame(master=self)
		self.frame0.grid(row=0, column=0, sticky="nswe", padx=10, pady=10)

		self.label_heading = customtkinter.CTkLabel(master=self.frame0, text=self.header_name)
		self.label_heading.pack(pady=12, padx=10)

		self.frame1 = customtkinter.CTkFrame(master=self)
		self.frame1.grid(row=1, column=0, sticky="nswe", padx=10, pady=5)

		self.frame1_1 = customtkinter.CTkFrame(master=self.frame1)
		self.frame1_1.pack(padx=20, pady=20)

		self.frame2 = customtkinter.CTkFrame(master=self)
		self.frame2.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)

		self.resetbtn= customtkinter.CTkButton(master=self.frame2, text="Reset", command=self.reset)
		self.resetbtn.pack(pady=10, padx=10)

		self.reset()

	def reset(self):

		global b1, b2, b3, b4, b5, b6, b7, b8, b9
		global clicked, count
		clicked = True
		count = 0

		# Build our buttons
		self.b1 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b1))
		self.b2 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b2))
		self.b3 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b3))

		self.b4 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b4))
		self.b5 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b5))
		self.b6 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b6))

		self.b7 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b7))
		self.b8 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b8))
		self.b9 = Button(self.frame1_1, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.b_click(self.b9))

		# Grid our buttons to the screen
		self.b1.grid(row=0, column=0)
		self.b2.grid(row=0, column=1)
		self.b3.grid(row=0, column=2)

		self.b4.grid(row=1, column=0)
		self.b5.grid(row=1, column=1)
		self.b6.grid(row=1, column=2)

		self.b7.grid(row=2, column=0)
		self.b8.grid(row=2, column=1)
		self.b9.grid(row=2, column=2)

	def b_click(self,b):
		global clicked, count

		if b["text"] == " " and clicked == True:
			b["text"] = "X"
			clicked = False
			count += 1
			self.checkifwon()
		elif b["text"] == " " and clicked == False:
			b["text"] = "O"
			clicked = True
			count += 1
			self.checkifwon()
		else:
			messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected\nPick Another Box..." )


	# disable all the buttons
	def disable_all_buttons(self):
		self.b1.config(state=DISABLED)
		self.b2.config(state=DISABLED)
		self.b3.config(state=DISABLED)
		self.b4.config(state=DISABLED)
		self.b5.config(state=DISABLED)
		self.b6.config(state=DISABLED)
		self.b7.config(state=DISABLED)
		self.b8.config(state=DISABLED)
		self.b9.config(state=DISABLED)

	# Check to see if someone won
	def checkifwon(self):
		global winner
		winner = False

		if self.b1["text"] == "X" and self.b2["text"] == "X" and self.b3["text"]  == "X":
			self.b1.config(bg="#ff8080")
			self.b2.config(bg="#ff8080")
			self.b3.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
			self.disable_all_buttons()
		elif self.b4["text"] == "X" and self.b5["text"] == "X" and self.b6["text"]  == "X":
			self.b4.config(bg="#ff8080")
			self.b5.config(bg="#ff8080")
			self.b6.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
			self.disable_all_buttons()

		elif self.b7["text"] == "X" and self.b8["text"] == "X" and self.b9["text"]  == "X":
			self.b7.config(bg="#ff8080")
			self.b8.config(bg="#ff8080")
			self.b9.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
			self.disable_all_buttons()

		elif self.b1["text"] == "X" and self.b4["text"] == "X" and self.b7["text"]  == "X":
			self.b1.config(bg="#ff8080")
			self.b4.config(bg="#ff8080")
			self.b7.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
			self.disable_all_buttons()

		elif self.b2["text"] == "X" and self.b5["text"] == "X" and self.b8["text"]  == "X":
			self.b2.config(bg="#ff8080")
			self.b5.config(bg="#ff8080")
			self.b8.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
			self.disable_all_buttons()

		elif self.b3["text"] == "X" and self.b6["text"] == "X" and self.b9["text"]  == "X":
			self.b3.config(bg="#ff8080")
			self.b6.config(bg="#ff8080")
			self.b9.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
			self.disable_all_buttons()

		elif self.b1["text"] == "X" and self.b5["text"] == "X" and self.b9["text"]  == "X":
			self.b1.config(bg="#ff8080")
			self.b5.config(bg="#ff8080")
			self.b9.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
			self.disable_all_buttons()

		elif self.b3["text"] == "X" and self.b5["text"] == "X" and self.b7["text"]  == "X":
			self.b3.config(bg="#ff8080")
			self.b5.config(bg="#ff8080")
			self.b7.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
			self.disable_all_buttons()

		#### CHECK FOR O's Win
		elif self.b1["text"] == "O" and self.b2["text"] == "O" and self.b3["text"]  == "O":
			self.b1.config(bg="#ff8080")
			self.b2.config(bg="#ff8080")
			self.b3.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
			self.disable_all_buttons()
		elif self.b4["text"] == "O" and self.b5["text"] == "O" and self.b6["text"]  == "O":
			self.b4.config(bg="#ff8080")
			self.b5.config(bg="#ff8080")
			self.b6.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
			self.disable_all_buttons()

		elif self.b7["text"] == "O" and self.b8["text"] == "O" and self.b9["text"]  == "O":
			self.b7.config(bg="#ff8080")
			self.b8.config(bg="#ff8080")
			self.b9.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
			self.disable_all_buttons()

		elif self.b1["text"] == "O" and self.b4["text"] == "O" and self.b7["text"]  == "O":
			self.b1.config(bg="#ff8080")
			self.b4.config(bg="#ff8080")
			self.b7.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
			self.disable_all_buttons()

		elif self.b2["text"] == "O" and self.b5["text"] == "O" and self.b8["text"]  == "O":
			self.b2.config(bg="#ff8080")
			self.b5.config(bg="#ff8080")
			self.b8.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
			self.disable_all_buttons()

		elif self.b3["text"] == "O" and self.b6["text"] == "O" and self.b9["text"]  == "O":
			self.b3.config(bg="#ff8080")
			self.b6.config(bg="#ff8080")
			self.b9.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
			self.disable_all_buttons()

		elif self.b1["text"] == "O" and self.b5["text"] == "O" and self.b9["text"]  == "O":
			self.b1.config(bg="#ff8080")
			self.b5.config(bg="#ff8080")
			self.b9.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
			self.disable_all_buttons()

		elif self.b3["text"] == "O" and self.b5["text"] == "O" and self.b7["text"]  == "O":
			self.b3.config(bg="#ff8080")
			self.b5.config(bg="#ff8080")
			self.b7.config(bg="#ff8080")
			winner = True
			messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
			self.disable_all_buttons()

		# Check if tie
		if count == 9 and winner == False:
			messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
			self.disable_all_buttons()	


class App(customtkinter.CTk):

	APP_NAME = "CustomTkinter example_background_image.py"
	WIDTH = 900
	HEIGHT = 600

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.title(App.APP_NAME)
		self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
		self.minsize(App.WIDTH, App.HEIGHT)
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

		self.button_1 = customtkinter.CTkButton(master=self.frame_left,text="Play",command=lambda: show_frame(self.game_1_frame))
		self.button_1.grid(row=2, column=0, pady=10, padx=20)

		self.game_1_frame = Game_TicTacToe(self.frame_right, header_name="Game 1")

		def show_frame(widget,):
			widget.grid(row=0, column=2, padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
