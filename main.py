from tkinter import *
from playsound import playsound

# configure the window
window = Tk()
window.title("hc-arcade-project")
window.attributes("-fullscreen", True)
window.configure(background="black")

# define images
sm_btn_bg = PhotoImage(file="img/storymode.png")
sm_btn_bg_alt = PhotoImage(file="img/storymode-alt.png")
fp_btn_bg = PhotoImage(file="img/freeplay.png")
fp_btn_bg_alt = PhotoImage(file="img/freeplay-alt.png")
op_btn_bg = PhotoImage(file="img/options.png")
op_btn_bg_alt = PhotoImage(file="img/options-alt.png")

# create buttons on main screen
menu_btn_1 = Button(window, image=sm_btn_bg, bg="black", borderwidth=0)
menu_btn_1.grid(row=0, column=0)

menu_btn_2 = Button(window, image=fp_btn_bg, bg="black", borderwidth=0)
menu_btn_2.grid(row=1, column=0)

menu_btn_3 = Button(window, image=op_btn_bg, bg="black", borderwidth=0)
menu_btn_3.grid(row=2, column=0)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)

# display the tk window
window.mainloop()
