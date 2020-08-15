import tkinter as tk
import os
import threading as th
from time import sleep

def get_dynos():
	apps = ("ultimatespelltome", "ustbackup")
	for i in apps:
		try:
			os.system(f"heroku ps -a {i} > {i}_Dynos.txt")
		except:
			os.system(f"echo Erro De Conexão > {i}_Dynos.txt")

	label3["text"] = "\t" + read_dynos()[0]
	label4["text"] = "\t" + read_dynos()[1]

def read_dynos():
	o = open("ultimatespelltome_Dynos.txt", "r")
	ust = ((o.readlines())[0]).strip()
	o.close()
	o = open("ustbackup_Dynos.txt", "r")
	ustbackup = ((o.readlines())[0]).strip()
	o.close()
	return [ust, ustbackup]

def on_ust():
	os.system("heroku dyno:scale worker=0 -a ultimatespelltome")
	label3["text"] = "\tUST Ativado"

def off_ust():
	os.system("heroku dyno:scale worker=0 -a ultimatespelltome")
	label3["text"] = "\tUST Destivado"

def on_ustbackup():
	os.system("heroku dyno:scale worker=1 -a ustbackup")
	label4["text"] = "\tUST Backup Ativado"

def off_ustbackup():
	os.system("heroku dyno:scale worker=0 -a ustbackup")
	label4["text"] = "\tUST Backup Destivado"

window = tk.Tk()

geometry = [800, 600] #1 é a altura, 0 é a largura

#Frames Configs
spacing = 5
frame_bg = "#ffffff"
frame_height = (geometry[1]*0.4)-spacing
frame_width = geometry[0]
frame_ust_place = [0, 0] #x, y
frame_ustbackup_place = [0, frame_height+(spacing*2)] #x,y
frame_border = 1
frame_highlight_bg = "#000000"
frame_highlight_color = "#000000"
total_frame_height = (2*frame_height) + (2*spacing)

#Button 1 Config
b1_place = [10, total_frame_height + (geometry[1] - total_frame_height)/4] #x,y
b1_height = 3
b1_width = 15
b1_text = "Atualizar"
b1_background = "#ffffff"
b1_highlight_color = "#565656"
b1_bd_color = "#000000"
b1_bd = 1

#Title labels Config
label_height = 1
label_width = 50
label_bg = "#ffffff"
label_place = [1, 1]
label_bd_color = "#ffffff"
label_bd = 0
label_anchor = "w"
label_font = 16

#Dyno Labels Config
D_label_height = 7
D_label_width = 79
D_label_bg = "#000000"
D_label_place = [1, 40]
D_label_bd_color = "#ffffff"
D_label_bd = 0
D_label_anchor = "w"
D_label_font = 16
D_label_wrap = 790
D_label_font_color = "#12ff00" #fg

#On/Off Button Config
OO_b1_place_on = [1, 190] #x,y
OO_b1_place_off = [80, 190] #x,y
OO_b1_height = 1
OO_b1_width = 5
OO_b1_text_on = "On"
OO_b1_text_off = "Off"
OO_b1_background = "#ffffff"
OO_b1_highlight_color = "#565656"
OO_b1_bd_color = "#000000"
OO_b1_bd = 1

dynos = "\tAtualize Os Valores Atuais De Dynos"

#Frames
frame_for_contour = tk.Frame(window, bg=frame_bg, height=geometry[1], width=geometry[0], borderwidth=frame_border, highlightbackground=frame_highlight_bg, highlightcolor=frame_highlight_color, highlightthickness=frame_border)
frame_for_contour.place(x=frame_ust_place[0], y=frame_ust_place[1])

frame_ust = tk.Frame(window, bg=frame_bg, height=frame_height, width=frame_width, borderwidth=frame_border, highlightbackground=frame_highlight_bg, highlightcolor=frame_highlight_color, highlightthickness=frame_border)
frame_ust.place(x=frame_ust_place[0], y=frame_ust_place[1])

frame_ustbackup = tk.Frame(window, bg=frame_bg, height=frame_height, width=frame_width, borderwidth=frame_border, highlightbackground=frame_highlight_bg, highlightcolor=frame_highlight_color, highlightthickness=frame_border)
frame_ustbackup.place(x=frame_ustbackup_place[0], y=frame_ustbackup_place[1])

#Buttons
button1 = tk.Button(window, text=b1_text, command=get_dynos, height=b1_height, width=b1_width, bg=b1_background, bd=b1_bd, highlightbackground=b1_bd_color, highlightthickness=b1_bd, highlightcolor=b1_highlight_color, relief="flat")
button1.place(x=b1_place[0], y=b1_place[1])

button4 = tk.Button(frame_ust, text=OO_b1_text_on, command=on_ust, height=OO_b1_height, width=OO_b1_width, bg=OO_b1_background, bd=OO_b1_bd, highlightbackground=OO_b1_bd_color, highlightthickness=OO_b1_bd, highlightcolor=OO_b1_highlight_color, relief="flat")
button4.place(x=OO_b1_place_on[0], y=OO_b1_place_on[1])

button4 = tk.Button(frame_ust, text=OO_b1_text_off, command=off_ust, height=OO_b1_height, width=OO_b1_width, bg=OO_b1_background, bd=OO_b1_bd, highlightbackground=OO_b1_bd_color, highlightthickness=OO_b1_bd, highlightcolor=OO_b1_highlight_color, relief="flat")
button4.place(x=OO_b1_place_off[0], y=OO_b1_place_off[1])

button3 = tk.Button(frame_ustbackup, text=OO_b1_text_on, command=on_ustbackup, height=OO_b1_height, width=OO_b1_width, bg=OO_b1_background, bd=OO_b1_bd, highlightbackground=OO_b1_bd_color, highlightthickness=OO_b1_bd, highlightcolor=OO_b1_highlight_color, relief="flat")
button3.place(x=OO_b1_place_on[0], y=OO_b1_place_on[1])

button4 = tk.Button(frame_ustbackup, text=OO_b1_text_off, command=off_ustbackup, height=OO_b1_height, width=OO_b1_width, bg=OO_b1_background, bd=OO_b1_bd, highlightbackground=OO_b1_bd_color, highlightthickness=OO_b1_bd, highlightcolor=OO_b1_highlight_color, relief="flat")
button4.place(x=OO_b1_place_off[0], y=OO_b1_place_off[1])

#Labels
label1 = tk.Label(frame_ust, text="Ultimate Spell Tome", height=label_height, width=label_width, bg=label_bg, anchor=label_anchor, font=label_font)
label1.place(x=label_place[0], y=label_place[1])

label2 = tk.Label(frame_ustbackup, text="Backup Ultimate Spell Tome", height=label_height, width=label_width, bg=label_bg, anchor=label_anchor, font=label_font)
label2.place(x=label_place[0], y=label_place[1])

label3 = tk.Label(frame_ust, text=dynos, height=D_label_height, width=D_label_width, bg=D_label_bg, anchor=D_label_anchor, font=D_label_font, wraplength=D_label_wrap, fg=D_label_font_color)
label3.place(x=D_label_place[0], y=D_label_place[1])

label4 = tk.Label(frame_ustbackup, text=dynos, height=D_label_height, width=D_label_width, bg=D_label_bg, anchor=D_label_anchor, font=D_label_font, wraplength=D_label_wrap, fg=D_label_font_color)
label4.place(x=D_label_place[0], y=D_label_place[1])

#Window Config
window["bg"] = "#ffffff"    #Background da janela é branco
window.geometry(f"{str(geometry[0])}x{str(geometry[1])}")
window.resizable(width=False, height=False)    #Impede resize
window.title("UST Manager")
window.mainloop()

#O deploy por cli funciona da seguinte forma:
#O repositório deve estar no path atual e deve haver a pasta .git nele ( git init cria essa pasta )
#Para pushar a pasta atual basta usar o comando git push caminho_do_git_do_heroku master
#https://git.heroku.com/ultimatespelltome.git
#https://git.heroku.com/ustbackup.git