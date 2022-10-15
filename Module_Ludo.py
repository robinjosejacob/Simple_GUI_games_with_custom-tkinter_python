from tkinter import *
from tkinter import messagebox
from webbrowser import BackgroundBrowser
import customtkinter
from PIL import Image, ImageTk
import os

PATH = os.path.dirname(os.path.realpath(__file__))


customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "green" (standard), "green", "dark-blue"

class Home(customtkinter.CTkFrame):
	def __init__(self, *args, header_name="Games",shade_color,main_color,**kwargs):
		super().__init__(*args, **kwargs)

		self.main_color = main_color
		self.fg_color_ = shade_color

		# self.homeframe = customtkinter.CTkFrame(master=self)
		# self.homeframe.grid(row=0, column=0, sticky="nswe", padx=20, pady=20)

		self.tocken_1 = customtkinter.CTkButton(master=self, text="1", width=32, height=32, corner_radius=10, fg_color=self.main_color)
		self.tocken_1.grid(row=0, column=0, pady=18, padx=18)
		self.tocken_2 = customtkinter.CTkButton(master=self, text="2", width=32, height=32, corner_radius=10, fg_color=self.main_color)
		self.tocken_2.grid(row=0, column=1, pady=18, padx=18)
		self.tocken_3 = customtkinter.CTkButton(master=self, text="3", width=32, height=32, corner_radius=10, fg_color=self.main_color)
		self.tocken_3.grid(row=1, column=0, pady=18, padx=18)
		self.tocken_4 = customtkinter.CTkButton(master=self, text="4", width=32, height=32, corner_radius=10, fg_color=self.main_color)
		self.tocken_4.grid(row=1, column=1, pady=18, padx=18)

		self.configure(fg_color=self.fg_color_ ,border_color=self.main_color, border_width=3)


class LudoMain(customtkinter.CTkFrame):
	def __init__(self, *args, header_name="Games", **kwargs):
		super().__init__(*args, **kwargs)

		redmain = "#E32227"
		redshade = "#FF8A8A"
		greenmain = "#00D100"
		greenshade = "#8AFF8A"
		bluemain = "#0476D0"
		blueshade = "#62B8FC"
		yellowmain = "#D1D100"
		yellowshade = "#FFFF8A"
		offwhite = "#F5F5F5"

		self.settings_image = self.load_image("/test_images/settings.png", 20)
		self.bell_image = self.load_image("/test_images/bell.png", 20)
		self.home_image = self.load_image("/test_images/home.png", 20)

		self.header_name = header_name

		self.label_1 = customtkinter.CTkLabel(master=self, text=self.header_name)
		self.label_1.grid(row=0, column=1,pady=10, padx=10)

		# self.label_2 = customtkinter.CTkLabel(master=self, text="Module under development")
		# self.label_2.grid(row=0, column=1,pady=10, padx=10)

		self.rootframe_left = customtkinter.CTkFrame(master=self)
		self.rootframe_left.grid(row=1, column=0, padx=5, pady=5)

		self.rootframe = customtkinter.CTkFrame(master=self)
		self.rootframe.grid(row=1, column=1, padx=1, pady=1)

		self.rootframe_right = customtkinter.CTkFrame(master=self)
		self.rootframe_right.grid(row=1, column=2, padx=5, pady=5)

		self.red_homeclass = Home(self.rootframe, header_name="Red Home",shade_color=redshade,main_color=redmain)
		self.red_homeclass.grid(row=0, column=0, pady=5, padx=5)
		self.green_homeclass = Home(self.rootframe, header_name="Grenn Home",shade_color=greenshade,main_color=greenmain)
		self.green_homeclass.grid(row=0, column=2, pady=5, padx=5)
		self.blue_homeclass = Home(self.rootframe, header_name="Blue Home",shade_color=blueshade,main_color=bluemain)
		self.blue_homeclass.grid(row=2, column=0, pady=5, padx=5)
		self.yellow_homeclass = Home(self.rootframe, header_name="Yellow Home",shade_color=yellowshade,main_color=yellowmain)
		self.yellow_homeclass.grid(row=2, column=2, pady=5, padx=5)

		self.finishingframe = customtkinter.CTkFrame(master=self.rootframe,corner_radius=1)
		self.finishingframe.grid(row=1, column=1, sticky="nswe", padx=5, pady=5)

		self.redfinished=customtkinter.CTkLabel(master=self.finishingframe,text=" ",width=33,height=33,corner_radius=2,fg_color=redshade).grid(row=0,column=0,padx=1,pady=1)
		self.grefinished=customtkinter.CTkLabel(master=self.finishingframe,text=" ",width=33,height=33,corner_radius=2,fg_color=greenshade).grid(row=0,column=1,padx=1,pady=1)
		self.blufinished=customtkinter.CTkLabel(master=self.finishingframe,text=" ",width=33,height=33,corner_radius=2,fg_color=blueshade).grid(row=1,column=0,padx=1,pady=1)
		self.yelfinished=customtkinter.CTkLabel(master=self.finishingframe,text=" ",width=33,height=33,corner_radius=2,fg_color=yellowshade).grid(row=1,column=1,padx=1,pady=1)
		
		self.redtrackframe = customtkinter.CTkFrame(master=self.rootframe,corner_radius=1)
		self.redtrackframe.grid(row=1, column=0, sticky="nswe", padx=5, pady=5)
		self.greentrackframe = customtkinter.CTkFrame(master=self.rootframe,corner_radius=1)
		self.greentrackframe.grid(row=0, column=1, sticky="nswe", padx=5, pady=5)
		self.bluetrackframe = customtkinter.CTkFrame(master=self.rootframe,corner_radius=1)
		self.bluetrackframe.grid(row=1, column=2, sticky="nswe", padx=5, pady=5)
		self.yellowtrackframe = customtkinter.CTkFrame(master=self.rootframe,corner_radius=1)
		self.yellowtrackframe.grid(row=2, column=1, sticky="nswe", padx=5, pady=5)

		############## red track #########
		self.b52=customtkinter.CTkLabel(master=self.redtrackframe,text="52",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=1,padx=1,pady=1)
		self.b1	=customtkinter.CTkLabel(master=self.redtrackframe,text="1 ",width=21,height=21,corner_radius=2,fg_color=redshade).grid(row=0,column=2,padx=1,pady=1)
		self.b2	=customtkinter.CTkLabel(master=self.redtrackframe,text="2 ",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=3,padx=1,pady=1)
		self.b3	=customtkinter.CTkLabel(master=self.redtrackframe,text="3 ",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=4,padx=1,pady=1)
		self.b4	=customtkinter.CTkLabel(master=self.redtrackframe,text="4 ",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=5,padx=1,pady=1)
		self.b5	=customtkinter.CTkLabel(master=self.redtrackframe,text="5 ",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=6,padx=1,pady=1)
		
		self.b51=customtkinter.CTkLabel(master=self.redtrackframe,text="52",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=1,column=1,padx=1,pady=1)
		self.R1 =customtkinter.CTkLabel(master=self.redtrackframe,text="R1",width=21,height=21,corner_radius=2,fg_color=redshade).grid(row=1,column=2,padx=1,pady=1)
		self.R2 =customtkinter.CTkLabel(master=self.redtrackframe,text="R2",width=21,height=21,corner_radius=2,fg_color=redshade).grid(row=1,column=3,padx=1,pady=1)
		self.R3 =customtkinter.CTkLabel(master=self.redtrackframe,text="R3",width=21,height=21,corner_radius=2,fg_color=redshade).grid(row=1,column=4,padx=1,pady=1)
		self.R4 =customtkinter.CTkLabel(master=self.redtrackframe,text="R4",width=21,height=21,corner_radius=2,fg_color=redshade).grid(row=1,column=5,padx=1,pady=1)
		self.R5 =customtkinter.CTkLabel(master=self.redtrackframe,text="R5",width=21,height=21,corner_radius=2,fg_color=redshade).grid(row=1,column=6,padx=1,pady=1)

		self.b50=customtkinter.CTkLabel(master=self.redtrackframe,text="50",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=1,padx=1,pady=1)
		self.b49=customtkinter.CTkLabel(master=self.redtrackframe,text="49",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=2,padx=1,pady=1)
		self.b48=customtkinter.CTkLabel(master=self.redtrackframe,text="48",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=3,padx=1,pady=1)
		self.b47=customtkinter.CTkLabel(master=self.redtrackframe,text="47",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=4,padx=1,pady=1)
		self.b46=customtkinter.CTkLabel(master=self.redtrackframe,text="46",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=5,padx=1,pady=1)
		self.b45=customtkinter.CTkLabel(master=self.redtrackframe,text="45",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=6,padx=1,pady=1)
		
		############## green track #########
		self.b6 =customtkinter.CTkLabel(master=self.greentrackframe,text="6 ",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=1,column=0,padx=1,pady=1)
		self.b7 =customtkinter.CTkLabel(master=self.greentrackframe,text="7 ",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=0,padx=1,pady=1)
		self.b8 =customtkinter.CTkLabel(master=self.greentrackframe,text="8 ",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=3,column=0,padx=1,pady=1)
		self.b9 =customtkinter.CTkLabel(master=self.greentrackframe,text="9 ",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=4,column=0,padx=1,pady=1)
		self.b10=customtkinter.CTkLabel(master=self.greentrackframe,text="10",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=5,column=0,padx=1,pady=1)
		self.b11=customtkinter.CTkLabel(master=self.greentrackframe,text="11",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=6,column=0,padx=1,pady=1)
		
		self.b12=customtkinter.CTkLabel(master=self.greentrackframe,text="12",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=1,column=1,padx=1,pady=1)
		self.G1 =customtkinter.CTkLabel(master=self.greentrackframe,text="G1",width=21,height=21,corner_radius=2,fg_color=greenshade).grid(row=2,column=1,padx=1,pady=1)
		self.G2 =customtkinter.CTkLabel(master=self.greentrackframe,text="G2",width=21,height=21,corner_radius=2,fg_color=greenshade).grid(row=3,column=1,padx=1,pady=1)
		self.G3 =customtkinter.CTkLabel(master=self.greentrackframe,text="G3",width=21,height=21,corner_radius=2,fg_color=greenshade).grid(row=4,column=1,padx=1,pady=1)
		self.G4 =customtkinter.CTkLabel(master=self.greentrackframe,text="G4",width=21,height=21,corner_radius=2,fg_color=greenshade).grid(row=5,column=1,padx=1,pady=1)
		self.G5 =customtkinter.CTkLabel(master=self.greentrackframe,text="G5",width=21,height=21,corner_radius=2,fg_color=greenshade).grid(row=6,column=1,padx=1,pady=1)
		
		self.b13=customtkinter.CTkLabel(master=self.greentrackframe,text="13",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=1,column=2,padx=1,pady=1)
		self.b14=customtkinter.CTkLabel(master=self.greentrackframe,text="14",width=21,height=21,corner_radius=2,fg_color=greenshade).grid(row=2,column=2,padx=1,pady=1)
		self.b15=customtkinter.CTkLabel(master=self.greentrackframe,text="15",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=3,column=2,padx=1,pady=1)
		self.b16=customtkinter.CTkLabel(master=self.greentrackframe,text="16",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=4,column=2,padx=1,pady=1)
		self.b17=customtkinter.CTkLabel(master=self.greentrackframe,text="17",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=5,column=2,padx=1,pady=1)
		self.b18=customtkinter.CTkLabel(master=self.greentrackframe,text="18",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=6,column=2,padx=1,pady=1)
		
		############## blue track #########
		self.b19=customtkinter.CTkLabel(master=self.bluetrackframe,text="19",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=1,padx=1,pady=1)
		self.b20=customtkinter.CTkLabel(master=self.bluetrackframe,text="20",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=2,padx=1,pady=1)
		self.b21=customtkinter.CTkLabel(master=self.bluetrackframe,text="21",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=3,padx=1,pady=1)
		self.b22=customtkinter.CTkLabel(master=self.bluetrackframe,text="22",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=4,padx=1,pady=1)
		self.b23=customtkinter.CTkLabel(master=self.bluetrackframe,text="23",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=5,padx=1,pady=1)
		self.b24=customtkinter.CTkLabel(master=self.bluetrackframe,text="24",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=0,column=6,padx=1,pady=1)
		
		self.b25=customtkinter.CTkLabel(master=self.bluetrackframe,text="Y5",width=21,height=21,corner_radius=2,fg_color=yellowshade).grid(row=1,column=1,padx=1,pady=1)
		self.Y1 =customtkinter.CTkLabel(master=self.bluetrackframe,text="Y4",width=21,height=21,corner_radius=2,fg_color=yellowshade).grid(row=1,column=2,padx=1,pady=1)
		self.Y2 =customtkinter.CTkLabel(master=self.bluetrackframe,text="Y3",width=21,height=21,corner_radius=2,fg_color=yellowshade).grid(row=1,column=3,padx=1,pady=1)
		self.Y3 =customtkinter.CTkLabel(master=self.bluetrackframe,text="Y2",width=21,height=21,corner_radius=2,fg_color=yellowshade).grid(row=1,column=4,padx=1,pady=1)
		self.Y4 =customtkinter.CTkLabel(master=self.bluetrackframe,text="Y1",width=21,height=21,corner_radius=2,fg_color=yellowshade).grid(row=1,column=5,padx=1,pady=1)
		self.Y5 =customtkinter.CTkLabel(master=self.bluetrackframe,text="25",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=1,column=6,padx=1,pady=1)
		
		self.b26=customtkinter.CTkLabel(master=self.bluetrackframe,text="26",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=1,padx=1,pady=1)
		self.b27=customtkinter.CTkLabel(master=self.bluetrackframe,text="27",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=2,padx=1,pady=1)
		self.b28=customtkinter.CTkLabel(master=self.bluetrackframe,text="28",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=3,padx=1,pady=1)
		self.b29=customtkinter.CTkLabel(master=self.bluetrackframe,text="29",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=4,padx=1,pady=1)
		self.b30=customtkinter.CTkLabel(master=self.bluetrackframe,text="30",width=21,height=21,corner_radius=2,fg_color=yellowshade).grid(row=2,column=5,padx=1,pady=1)
		self.b31=customtkinter.CTkLabel(master=self.bluetrackframe,text="31",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=6,padx=1,pady=1)
		
		############## yellow track #########
		self.b32=customtkinter.CTkLabel(master=self.yellowtrackframe,text="32",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=1,column=0,padx=1,pady=1)
		self.b33=customtkinter.CTkLabel(master=self.yellowtrackframe,text="33",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=0,padx=1,pady=1)
		self.b34=customtkinter.CTkLabel(master=self.yellowtrackframe,text="34",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=3,column=0,padx=1,pady=1)
		self.b35=customtkinter.CTkLabel(master=self.yellowtrackframe,text="35",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=4,column=0,padx=1,pady=1)
		self.b36=customtkinter.CTkLabel(master=self.yellowtrackframe,text="36",width=21,height=21,corner_radius=2,fg_color=blueshade).grid(row=5,column=0,padx=1,pady=1)
		self.b37=customtkinter.CTkLabel(master=self.yellowtrackframe,text="37",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=6,column=0,padx=1,pady=1)

		self.b38=customtkinter.CTkLabel(master=self.yellowtrackframe,text="B5",width=21,height=21,corner_radius=2,fg_color=blueshade).grid(row=1,column=1,padx=1,pady=1)
		self.B1 =customtkinter.CTkLabel(master=self.yellowtrackframe,text="B4",width=21,height=21,corner_radius=2,fg_color=blueshade).grid(row=2,column=1,padx=1,pady=1)
		self.B2 =customtkinter.CTkLabel(master=self.yellowtrackframe,text="B3",width=21,height=21,corner_radius=2,fg_color=blueshade).grid(row=3,column=1,padx=1,pady=1)
		self.B3 =customtkinter.CTkLabel(master=self.yellowtrackframe,text="B2",width=21,height=21,corner_radius=2,fg_color=blueshade).grid(row=4,column=1,padx=1,pady=1)
		self.B4 =customtkinter.CTkLabel(master=self.yellowtrackframe,text="B1",width=21,height=21,corner_radius=2,fg_color=blueshade).grid(row=5,column=1,padx=1,pady=1)
		self.B5 =customtkinter.CTkLabel(master=self.yellowtrackframe,text="38",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=6,column=1,padx=1,pady=1)

		self.b39=customtkinter.CTkLabel(master=self.yellowtrackframe,text="32",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=1,column=2,padx=1,pady=1)
		self.b40=customtkinter.CTkLabel(master=self.yellowtrackframe,text="34",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=2,column=2,padx=1,pady=1)
		self.b41=customtkinter.CTkLabel(master=self.yellowtrackframe,text="35",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=3,column=2,padx=1,pady=1)
		self.b42=customtkinter.CTkLabel(master=self.yellowtrackframe,text="36",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=4,column=2,padx=1,pady=1)
		self.b43=customtkinter.CTkLabel(master=self.yellowtrackframe,text="37",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=5,column=2,padx=1,pady=1)
		self.b44=customtkinter.CTkLabel(master=self.yellowtrackframe,text="38",width=21,height=21,corner_radius=2,fg_color=offwhite).grid(row=6,column=2,padx=1,pady=1)

		self.redplayer_dice = customtkinter.CTkButton(master=self.rootframe_left,text="Player 1",command=lambda: self.rollDice(self.redplayer_dice),fg_color=redmain, hover_color=redshade, image=self.home_image)
		self.redplayer_dice.grid(row=0, column=0, pady=50, padx=5)

		self.greenplayer_dice = customtkinter.CTkButton(master=self.rootframe_right,text="Player 2",command=lambda: self.rollDice(self.greenplayer_dice),fg_color=greenmain, hover_color=greenshade)
		self.greenplayer_dice.grid(row=0, column=0, pady=50, padx=5)

		self.blueplayer_dice = customtkinter.CTkButton(master=self.rootframe_left,text="Player 3",command=lambda: self.rollDice(self.blueplayer_dice),fg_color=bluemain,hover_color=blueshade)
		self.blueplayer_dice.grid(row=1, column=0, pady=50, padx=5)

		self.yellowplayer_dice = customtkinter.CTkButton(master=self.rootframe_right,text="Player 4",command=lambda: self.rollDice(self.yellowplayer_dice),fg_color=yellowmain, hover_color=yellowshade)
		self.yellowplayer_dice.grid(row=1, column=0, pady=50, padx=5, sticky="s")
	
	def load_image(self, path, image_size):
		""" load rectangular image with path relative to PATH """
		return ImageTk.PhotoImage(Image.open(PATH + path).resize((image_size, image_size)))

	def rollDice(self,color):
		pass


class App(customtkinter.CTk):

	APP_NAME = "class template.py"
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

		self.frame_left = customtkinter.CTkFrame(master=self,
													width=180,
													corner_radius=0)
		self.frame_left.grid(row=0, column=0, sticky="nswe")

		self.frame_right = customtkinter.CTkFrame(master=self)
		self.frame_right.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

		# ============ frame_left ============

		# configure grid layout (1x11)
		self.frame_left.grid_rowconfigure(0, minsize=10)   # empty row with minsize as spacing
		self.frame_left.grid_rowconfigure(5, weight=1)  # empty row as spacing
		self.frame_left.grid_rowconfigure(8, minsize=20)    # empty row with minsize as spacing
		self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

		self.label_1 = customtkinter.CTkLabel(master=self.frame_left, text="Dashboard", text_font=("Roboto Medium", -16))
		self.label_1.grid(row=1, column=0, pady=10, padx=10)

		self.optionmenu_theme = customtkinter.CTkOptionMenu(master=self.frame_left,
														values=["Light", "Dark", "System"],
														command=self.change_appearance_mode)
		self.optionmenu_theme.grid(row=10, column=0, pady=10, padx=20, sticky="w")

		self.button_1 = customtkinter.CTkButton(master=self.frame_left,text="Play",command=lambda: self.show_frame(self.module_1_frame))
		self.button_1.grid(row=2, column=0, pady=10, padx=20)

		self.module_1_frame = Template(self.frame_right, header_name="Ludo")

		self.optionmenu_theme.set("Light")

	def change_appearance_mode(self, new_appearance_mode):
		customtkinter.set_appearance_mode(new_appearance_mode)

	def show_frame(self,widget,):
		widget.pack(padx=20, pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
