import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    miles_input = entry_int.get() 
    kilometers = miles_input * 1.609344
    output_string.set(f"{kilometers:0,.2f}")

# create the main window
window = tk.Tk()
window.title("demo converter")
window.geometry("300x150")

# title
title_label = ttk.Label(master = window, text = "Miles to Kilometers", font = "Calibri 16 bold")
title_label.pack(pady= 10)

# input field
input_frame = ttk.Frame(master = window)
entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable= entry_int)
button = ttk.Button(master = input_frame, text= "Convert", command= convert)
entry.pack(side = "left", padx= 10)
entry.focus()
button.pack(side = "left")
input_frame.pack(pady= 10)

# output
output_string = tk.StringVar()
output_label = ttk.Label(master= window, text= "Output", font = "Calibri 20", textvariable= output_string)
output_label.pack()

# run the application
window.mainloop()