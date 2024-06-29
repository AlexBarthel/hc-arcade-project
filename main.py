from tkinter import *
import winsound

# configure the window
window = Tk()
window.title("hc-arcade-project")
window.attributes("-fullscreen", True)
window.configure(background="black")
window.configure(cursor="none")

# define images
sm_btn_bg = PhotoImage(file="img/storymode.png")
sm_btn_bg_alt = PhotoImage(file="img/storymode-alt.png")
fp_btn_bg = PhotoImage(file="img/freeplay.png")
fp_btn_bg_alt = PhotoImage(file="img/freeplay-alt.png")
op_btn_bg = PhotoImage(file="img/options.png")
op_btn_bg_alt = PhotoImage(file="img/options-alt.png")

# create buttons on main screen
menu_btn_1 = Button(window, image=sm_btn_bg_alt, bg="black", borderwidth=0, activebackground="black")
menu_btn_1.grid(row=0, column=0)

menu_btn_2 = Button(window, image=fp_btn_bg, bg="black", borderwidth=0, activebackground="black")
menu_btn_2.grid(row=1, column=0)

menu_btn_3 = Button(window, image=op_btn_bg, bg="black", borderwidth=0, activebackground="black")
menu_btn_3.grid(row=2, column=0)

window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)
window.grid_rowconfigure(2, weight=1)
window.grid_columnconfigure(0, weight=1)

# initialize the selected button
selected_btn = 0
previous_btn = None

def update_btn_states():
    if selected_btn == 0:
        menu_btn_1.config(image=sm_btn_bg_alt)
        menu_btn_2.config(image=fp_btn_bg)
        menu_btn_3.config(image=op_btn_bg)
    elif selected_btn == 1:
        menu_btn_1.config(image=sm_btn_bg)
        menu_btn_2.config(image=fp_btn_bg_alt)
        menu_btn_3.config(image=op_btn_bg)
    elif selected_btn == 2:
        menu_btn_1.config(image=sm_btn_bg)
        menu_btn_2.config(image=fp_btn_bg)
        menu_btn_3.config(image=op_btn_bg_alt)

def arrow_up_handler(e):
    global previous_btn
    global selected_btn
    
    # set the previous btn to the current btn index
    previous_btn = selected_btn

    # find the next btn index
    selected_btn -= -2 if selected_btn == 0 else 1

    # change the state of the btns
    update_btn_states()

def arrow_down_handler(e):
    global previous_btn
    global selected_btn
    
    # set the previous btn to the current btn index
    previous_btn = selected_btn

    # find the next btn index
    selected_btn += -2 if selected_btn == 2 else 1

    # change the state of the btns
    update_btn_states()

def return_handler(e):
    winsound.PlaySound(None, winsound.SND_PURGE)
    menu_btn_1.grid_forget()
    menu_btn_2.grid_forget()
    menu_btn_3.grid_forget()
    print("STORY MODE" if selected_btn == 0 else "FREEPLAY" if selected_btn == 1 else "OPTIONS")

window.bind("<Up>", arrow_up_handler)
window.bind("<Down>", arrow_down_handler)
window.bind("<Return>", return_handler)

winsound.PlaySound("audio\menu-music.wav", winsound.SND_ASYNC | winsound.SND_LOOP)

# display the tk window
window.mainloop()
