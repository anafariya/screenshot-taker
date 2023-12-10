import os
import pyautogui
from tkinter import *

def take_screenshot():
    try:
        folder_name = "screenshots"
        folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), folder_name)
        os.makedirs(folder_path, exist_ok=True)

        # Get the count of existing screenshots
        screenshot_count = len([f for f in os.listdir(folder_path) if f.startswith("screenshot")])

        # Construct the new filename
        file_name = f"screenshot{str(screenshot_count + 1)}"
        file_path = os.path.join(folder_path, f"{file_name}.png")

        ss = pyautogui.screenshot()
        ss.save(file_path)
        status_label.config(text=f"Screenshot saved successfully!\nSaved at: {file_path}", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")

win = Tk()
win.title("Joy SS taker")
win.geometry("700x400")
win.config(bg="lightgray")
win.resizable(False, False)

entry = Entry(win, font=('Times New Roman', 20), justify="center")
entry.place(x=20, height=50, width=660, y=50)

button = Button(win, text="Take Screenshot", font=('Times New Roman', 15, "bold"), command=take_screenshot)
button.pack(pady=20)

status_label = Label(win, text="", font=('Times New Roman', 12), fg="black", bg="lightgray")
status_label.pack()

win.mainloop()
