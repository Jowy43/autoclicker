import tkinter as tk
import pyautogui
import threading
import time
import keyboard

clicking = False
thread = None


def autoclick(clicks_per_second):
    global clicking
    interval = 1 / clicks_per_second
    while clicking:
        pyautogui.click()
        time.sleep(interval)


def toggle_clicking():
    global clicking, thread
    clicks_per_second = float(entry_cps.get())

    if not clicking:
        clicking = True
        thread = threading.Thread(target=autoclick, args=(clicks_per_second,))
        thread.start()
    else:
        clicking = False
        if thread:
            thread.join()


root = tk.Tk()
root.title("Autoclicker")

label_cps = tk.Label(root, text="Clics por segundo:")
label_cps.pack()

entry_cps = tk.Entry(root)
entry_cps.pack()

label_info = tk.Label(root, text="Presiona la barra espaciadora para iniciar/detener.")
label_info.pack()

keyboard.add_hotkey('space', toggle_clicking)

root.mainloop()
