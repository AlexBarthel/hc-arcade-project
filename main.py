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
story_mode_btn = Button(window, image=sm_btn_bg)
story_mode_btn.pack()
freeplay_btn = Button(window, image=fp_btn_bg)
freeplay_btn.pack()
options_btn = Button(window, image=op_btn_bg, bg=None)
options_btn.pack()

# display the tk window
window.mainloop()
