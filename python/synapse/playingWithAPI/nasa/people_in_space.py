import requests
import tkinter as tk
import ttkbootstrap as ttk

# this isn't correct information, don't treat it as such.
#                                                           the earth is round

people = requests.get('http://api.open-notify.org/astros.json')
people_json = people.json()

# how many people on the ISS
iss_names = ""
for i in people_json['people']:
    if(i['craft'] == 'ISS'):
        iss_names += i['name'] + '\n'


# how many people on Shenzhou 15
sz15_names = ""
for i in people_json['people']:
    if(i['craft'] == 'Shenzhou 15'):
        sz15_names += i['name'] + '\n'

# root
root = ttk.Window(themename='darkly')
root.title('These brave humans, may god be with them.')
root.geometry("550x300")

# iss
iss_frame = ttk.Frame(master=root, borderwidth=1, relief='solid')
iss_title = ttk.Label(master=iss_frame, text='These are the people on ISS', font='Calibri 12 bold')
iss_title.pack()

iss_output = ttk.Label(master=iss_frame, text=iss_names)
iss_output.pack(pady=10)
iss_frame.pack(side='left', padx=20)

# sz15
sz15_frame = ttk.Frame(master=root, borderwidth=1, relief='solid')
sz15_title = ttk.Label(master=sz15_frame, text='These are the people on Shenzhou 15', font='Calibri 12 bold')
sz15_title.pack()

sz15_output = ttk.Label(master=sz15_frame, text=sz15_names)
sz15_output.pack(pady=10)

sz15_frame.pack(side='right', padx=20)
sz15_frame.place(x=260, y=65)

# end quote
end_quote = "man and his quest for knowledge and progress is determined and cannot be deterred. - JFK"
end_title = ttk.Label(master=root, text=end_quote)
end_title.pack()
end_title.place(x=30, y=260)
# run
root.mainloop()