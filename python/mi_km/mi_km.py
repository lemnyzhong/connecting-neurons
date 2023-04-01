import tkinter as tk
import ttkbootstrap as ttk

def convert():
    km = entry_type.get() * 1.60934
    output_type.set(str(km) + " kms")

# creates window 
root = ttk.Window(themename='vapor')
root.title('Metric Converter')
root.geometry('400x200')

# title label
title = ttk.Label(master=root, text='mi - km', font='Calibri 26 bold underline')
explaination = ttk.Label(master=root, text='pows miles into kilometers', font='Calibri')
title.pack()
explaination.pack()

# input
input_frame = ttk.Frame(master=root)
entry_type = tk.IntVar()
input_entry = ttk.Entry(master=input_frame, textvariable=entry_type)
convert_button = ttk.Button(master=input_frame, text='pow!', command=convert)
input_entry.pack(side='left', padx=10)
convert_button.pack(side='left')
input_frame.pack(pady=15)

# output
output_type = tk.StringVar()
output = ttk.Label(master=root, text='output', font='Calibri 14 bold', textvariable=output_type)
output.pack(pady=10)

# runs window
root.mainloop()