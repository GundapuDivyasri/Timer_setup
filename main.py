from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 10
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 5
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(time_text, text="00:00")
    label.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:
        stop_count(LONG_BREAK_MIN * 60)
        label.config(text="Leisure Mode", fg=RED)
    elif reps % 2 == 0:
        stop_count(SHORT_BREAK_MIN * 60)
        label.config(text="BREAK", fg=GREEN)
    else:
        stop_count(WORK_MIN * 60)
        label.config(text="WORK MODE", fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def stop_count(count):
    min = math.floor(count / 60)
    sec = count % 60
    if sec < 10:
        sec = "0" + str(sec)
    canvas.itemconfig(time_text, text=f"{min}:{sec}")
    if count > 0:
        global timer
        timer = window.after(1000, stop_count, count - 1)
    else:
        start_timer()
        check = ""
        sessions = math.floor(reps / 2)
        for i in range(sessions):
            check += "✓"
        checkmark.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("PORODOMO")
window.config(padx=100, pady=50, bg=YELLOW)
label = Label(text="Timer", fg=PINK, font=(FONT_NAME, 45), bg=YELLOW)
label.grid(column=1, row=0)
# canvas widget
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_pic = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_pic)
time_text = canvas.create_text(100, 135, text="00:00", fill="wheat", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
# stop_count(5)
start = Button(text="START", highlightthickness=0, command=start_timer)
reset = Button(text="RESET", highlightthickness=0, command=reset_timer)
start.grid(column=0, row=2)
reset.grid(column=2, row=2)
checkmark = Label(text="✓", fg="green", bg=YELLOW, font=(FONT_NAME, 20))
checkmark.grid(column=1, row=3)
window.mainloop()
