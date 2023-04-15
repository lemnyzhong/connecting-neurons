import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
from ttkwidgets import Table
from Session import *
from Faculties import *
from Faculty import *
from Student import *
import time

faculty = Faculties()
students = Students()

class loginScreen:
    def __init__(self):
        def login():
                e = email_var.get()
                p = password_var.get()

                if faculty.faculty(e, p) is not None:
                    root.destroy()
                    mainScreen(e)
                else:
                    ttkStyle.configure('incorrect.TLabel', background='#76b5c5', foreground='red')
                    incorrect_label = ttk.Label(footerFrame, text='incorrect details', style='incorrect.TLabel')
                    incorrect_label.grid(column=3, row=2, pady=40, padx=224)


        root = tk.Tk()
        root.title('login screen')
        root.resizable(0,0)
        
        ttkStyle = ttk.Style()
        
        ttkStyle.configure('titleFrame.TFrame', background='#76b5c5')
        titleFrame = ttk.Frame(root, height=100, width=536, style='titleFrame.TFrame')
        titleFrame.grid()
        

        ttkStyle.configure('mainFrame.TFrame', background='#76b5c5')
        mainFrame = ttk.Frame(root, style='mainFrame.TFrame')
        mainFrame.grid(row=2)
        
        login_label = ttk.Label(mainFrame, text='login', font='Calibri 20 bold', background='#76b5c5')
        login_label.grid(column=0, row=0, sticky='W', padx=15)

        email_var = ttk.StringVar()
        email_label = ttk.Label(mainFrame, text='Username:', background='#76b5c5', font='Calibri 10 bold')
        email_label.grid(column=0,row=1, padx=15)
        email_entry = ttk.Entry(mainFrame, textvariable=email_var)
        email_entry.grid(column=2, row=1)

        password_var = ttk.StringVar()
        password_label = ttk.Label(mainFrame, text='Password:', background='#76b5c5', font='Calibri 10 bold')
        password_entry = ttk.Entry(mainFrame, text='Enter username:', textvariable=password_var, show='*')
        password_label.grid(column=3, row=1, padx=15)
        password_entry.grid(column=4, row=1)

        ttkStyle.configure('loginButton.TButton', background='#e28743')
        login_button = ttk.Button(mainFrame, text='Login', command=login, takefocus=False, style='loginButton.TButton')
        login_button.grid(column=5, row=1, padx=15)

        ttkStyle.configure('headerFrame.TFrame', background='#76b5c5',)
        footerFrame = ttk.Frame(root, height=100, width=536, style='headerFrame.TFrame')
        footerFrame.grid()
    
        root.mainloop()

class mainScreen:
    def __init__(self, email):
        def getName(email):
            for i in faculty.faculties:
                if(i.email == email):
                        return (f'{i.name}')
        
        def temp_text():
            if(student_name_entry.get() == 'Enter name' or student_email_entry.get() == 'Enter email'):
                student_name_entry.delete(0, "end")
                student_email_entry.delete(0, "end")
        
        def refresh_table():
            student_table.delete(*student_table.get_children())

            for i, student in enumerate(students.students):
                student_table.insert(parent='', index='end', iid=i, values=(student.name, student.phone, student.email))

        def filter_students(event=None):
            # Get the values entered in the filter widgets
            name_filter = student_name_entry.get().lower()
            email_filter = student_email_entry.get().lower()

            # Clear the current contents of the Treeview widget
            student_table.delete(*student_table.get_children())

            # Insert matching students into the Treeview widget
            for i, student in enumerate(students.students):
                if (name_filter in student.name.lower() or not name_filter) and (email_filter in student.email.lower() or not email_filter):
                    student_table.insert(parent='', index='end', iid=i, values=(student.name, student.phone, student.email))
    
        def add():
            addScreen(root)

        def delete_entry():
            selected = student_table.selection()

            for i in selected:
                student_table.delete(i)
                students.students.pop(int(selected[0]))

        def select():
            selected = student_table.selection()

            selectScreen(root, students.students[int(selected[0])])

        def slip():
            selected = student_table.selection()

            slipScreen(root, students.students[int(selected[0])])
        
        def report():
            reportScreen(root)

        def exit():
            root.destroy()
            logoutScreen()

        root = tk.Tk()
        root.title(f'session admin: {getName(email)}')
        root.resizable(0, 0)

        ttkStyle = ttk.Style()

        user_name = ttk.Label(root, text='Welcome: '+getName(email), background="#76b5c5")
        user_name.grid(column=0, row=0)

        # time_label = ttk.Label(root, text=f'{time.localtime()[3]}:{time.localtime()[4]}', background="#76b5c5")
        # time_label.grid(column=3, row=0)
        
        # Filter section
        # title
        filter_title = ttk.Label(root, text='FILTER', background='#76b5c5', font='Calibri 24 bold')
        filter_title.grid(column=1, row=1, sticky='W', padx=18, pady=10)

        # name label
        student_name = ttk.Label(root, text='student name:', background='#76b5c5')
        student_name.grid(column=1, row=2, sticky='NWS', padx=20, pady=5)

        # name entry
        student_name_entry = ttk.Entry(root)
        student_name_entry.bind('<Enter>', lambda event: temp_text())
        student_name_entry.grid(column=2, row=2, pady=5)

        # email label
        student_email = ttk.Label(root, text='student email:', background='#76b5c5')
        student_email.grid(column=3, row=2, sticky='NWS', padx=10, pady=5)
        
        # email entry
        student_email_entry = ttk.Entry(root)
        student_email_entry.bind('<Enter>', lambda event: temp_text())
        student_email_entry.grid(column=4, row=2, pady=5)
        
        # refresh button
        refresh_button = tk.Button(root, text='refresh', command=refresh_table, background='#e28743')
        refresh_button.grid(column=0, row=5, pady=10, sticky='E')

        # table
        student_table = ttk.Treeview(root)
        student_table['columns'] = ('name', 'phone', 'email')

        student_table.column('#0', width=0, minwidth=0, stretch=False)
        student_table.heading("name", text="Name")
        student_table.column("name", anchor="w", width=100)
        student_table.heading("phone", text="Phone")
        student_table.column("phone", anchor="w", width=100)
        student_table.heading("email", text="Email")
        student_table.column("email", anchor="w", width=200)
        
        for i in range(len(students.students)):
            student_table.insert(parent='', index='end', iid=i, values=(students.students[i].name, students.students[i].phone, students.students[i].email))

        student_table.grid(column=0, row=5, columnspan=6, rowspan=10, pady=20, padx=10)

        student_name_entry.bind('<KeyRelease>', lambda event: filter_students())
        student_email_entry.bind('<KeyRelease>', lambda event: filter_students())
        

        # buttons
        add_button = tk.Button(root, text='add', command=add, width=10, height=2, background='#e28743')
        add_button.grid(column=0, row=15)

        delete_button = tk.Button(root, text='delete', command=delete_entry, width=10, height=2, background='#e28743')
        delete_button.grid(column=1, row=15)

        select_button = tk.Button(root, text='select', command=select, width=10, height=2, background='#e28743')
        select_button.grid(column=2, row=15, padx=25)

        slip_button = tk.Button(root, text='slip', width=10, height=2, background='#e28743', command=slip)
        slip_button.grid(column=3, row=15, padx=10)

        report_button = tk.Button(root, text='report', width=10, height=2, background='#e28743', command=report)
        report_button.grid(column=4, row=15)
        
        logout_button = tk.Button(root, text='logout', command=exit, width=10, height=2)
        logout_button.grid(column=5, row=15, padx=10, pady=10)

        root.configure(background="#76b5c5")
        root.mainloop()
    
class addScreen:
     def __init__(self, parent):
            self.parent = parent

            def add():
                new_student = Student(name=name_entry.get(), 
                                        email=email_entry.get(), 
                                        phone=phone_entry.get(), 
                                        address=address_entry.get(),
                                        idNumber=id_entry.get(), 
                                        studyType=type_entry.get(), 
                                        credits=credits_entry.get(), 
                                        scholarship=scholarship_entry.get(), 
                                        deductionCode=deduction_entry.get())
                 
                students.students.append(new_student)
                root.destroy()

            def close():
                root.destroy()

            root = ttk.Toplevel(self.parent)
            root.title('add student')
            root.geometry('290x570')
            root.resizable(0, 0)

            # personal details
            personal_title = ttk.Label(root, text='personal details', font='Calibri 24 bold', background="#76b5c5")
            personal_title.grid(column=0, row=0, padx=15, pady=10, columnspan=4)

            name_label = ttk.Label(root, text='name:', background="#76b5c5")
            name_label.grid(column=0, row=1, padx=16, sticky="NW", pady=10)

            name_var = ttk.StringVar()
            name_entry = ttk.Entry(root, width=25, textvariable=name_var)
            name_entry.grid(column=1, row=1, pady=10, sticky='W', columnspan=2)
            

            email_label = ttk.Label(root, text='email:', background="#76b5c5")
            email_label.grid(column=0, row=2, padx=16, sticky='W')
            
            email_var = ttk.StringVar()
            email_entry = ttk.Entry(root, width=25, textvariable=email_var)
            email_entry.grid(column=1, row=2, sticky='W', pady=10)

            phone_label = ttk.Label(root, text='phone:', background="#76b5c5")
            phone_label.grid(column=0, row=3, padx=16, sticky='W')

            phone_var = ttk.StringVar()
            phone_entry = ttk.Entry(root, width=25, textvariable=phone_var)
            phone_entry.grid(column=1, row=3, sticky='W', pady=10)

            address_label = ttk.Label(root, text='address:', background="#76b5c5")
            address_label.grid(column=0, row=4, padx=16, sticky='W')

            address_var = ttk.StringVar()
            address_entry = ttk.Entry(root, width=25, textvariable=address_var)
            address_entry.grid(column=1, row=4, sticky='W', pady=10)

            #tuition details
            tuition_title = ttk.Label(root, text='tuition details', font='Calibri 24 bold', background="#76b5c5")
            tuition_title.grid(column=0, row=5, padx=15, pady=10, columnspan=4)

            id_label = ttk.Label(root, text='student id:', background="#76b5c5")
            id_label.grid(column=0, row=6, padx=16, sticky="NW", pady=10)
            
            id_var = ttk.IntVar()
            id_entry = ttk.Entry(root, width=25, textvariable=id_var)
            id_entry.grid(column=1, row=6, pady=10, sticky='W')
            
            type_label = ttk.Label(root, text='type:', background="#76b5c5")
            type_label.grid(column=0, row=7, padx=16, sticky='W')

            type_var = ttk.StringVar()
            type_entry = ttk.Entry(root, width=25, textvariable=type_var)
            type_entry.grid(column=1, row=7, sticky='W', pady=10)

            credits_label = ttk.Label(root, text='credits:', background="#76b5c5")
            credits_label.grid(column=0, row=8, padx=16, sticky='W')
            
            credits_var = ttk.IntVar()
            credits_entry = ttk.Entry(root, width=25, textvariable=credits_var)
            credits_entry.grid(column=1, row=8, sticky='W', pady=10)

            scholarship_label = ttk.Label(root, text='scholarship:', background="#76b5c5")
            scholarship_label.grid(column=0, row=9, padx=16, sticky='W')

            scholarship_var = ttk.DoubleVar()
            scholarship_entry = ttk.Entry(root, width=25, textvariable=scholarship_var)
            scholarship_entry.grid(column=1, row=9, sticky='W', pady=10)

            deduction_label = ttk.Label(root, text='deduction:', background="#76b5c5")
            deduction_label.grid(column=0, row=10, padx=16, sticky='W')

            deduction_var = ttk.StringVar()
            deduction_entry = ttk.Entry(root, width=25, text='entry', textvariable=deduction_var)
            deduction_entry.insert(0, 'code')
            deduction_entry.grid(column=1, row=10, sticky='W', pady=10)

            add_button = tk.Button(root, text='add', background="#76b5c5", width=10, height=2, command=add)
            add_button.grid(column=0, row=12, padx=20, pady=20)

            close_button = tk.Button(root, text='close', background="#76b5c5", width=10, height=2, command=close)
            close_button.grid(column=1, row=12, padx=10, pady=20, sticky='E')

            root.configure(background="#76b5c5")
            root.mainloop()

class selectScreen:
     def __init__(self, parent, student):
            self.parent = parent

            def update():
                student.name = name_entry.get()
                student.email = email_entry.get()
                student.phone = phone_entry.get()
                student.address = address_entry.get()
                student.idNumber = id_entry.get()
                student.studyType = type_entry.get()
                student.credits = credits_entry.get()
                student.scholarship = scholarship_entry.get()
                student.deduction = deduction_entry.get()

                root.destroy()

            def close():
                root.destroy()

            root = tk.Toplevel(self.parent)
            root.title('making adjustments')
            root.geometry('290x570')
            root.resizable(0, 0)

            # personal details
            personal_title = ttk.Label(root, text='personal details', font='Calibri 24 bold', background="#76b5c5")
            personal_title.grid(column=0, row=0, padx=15, pady=10, columnspan=4)

            name_label = ttk.Label(root, text='name:', background="#76b5c5")
            name_label.grid(column=0, row=1, padx=16, sticky="NW", pady=10)

            name_var = ttk.StringVar()
            name_entry = ttk.Entry(root, width=25, textvariable=name_var)
            name_entry.insert(0, student.name)
            name_entry.grid(column=1, row=1, pady=10, sticky='W', columnspan=2)
            

            email_label = ttk.Label(root, text='email:', background="#76b5c5")
            email_label.grid(column=0, row=2, padx=16, sticky='W')
            
            email_var = ttk.StringVar()
            email_entry = ttk.Entry(root, width=25, textvariable=email_var)
            email_entry.insert(0, student.email)
            email_entry.grid(column=1, row=2, sticky='W', pady=10)

            phone_label = ttk.Label(root, text='phone:', background="#76b5c5")
            phone_label.grid(column=0, row=3, padx=16, sticky='W')

            phone_var = ttk.StringVar()
            phone_entry = ttk.Entry(root, width=25, textvariable=phone_var)
            phone_entry.insert(0, student.phone)
            phone_entry.grid(column=1, row=3, sticky='W', pady=10)

            address_label = ttk.Label(root, text='address:', background="#76b5c5")
            address_label.grid(column=0, row=4, padx=16, sticky='W')

            address_var = ttk.StringVar()
            address_entry = ttk.Entry(root, width=25, textvariable=address_var)
            address_entry.insert(0, student.address)
            address_entry.grid(column=1, row=4, sticky='W', pady=10)

            #tuition details
            tuition_title = ttk.Label(root, text='tuition details', font='Calibri 24 bold', background="#76b5c5")
            tuition_title.grid(column=0, row=5, padx=15, pady=10, columnspan=4)

            id_label = ttk.Label(root, text='student id:', background="#76b5c5")
            id_label.grid(column=0, row=6, padx=16, sticky="NW", pady=10)
            
            id_var = ttk.IntVar()
            id_entry = ttk.Entry(root, width=25, textvariable=id_var)
            id_entry.insert(0, student.idNumber)
            id_entry.grid(column=1, row=6, pady=10, sticky='W')
            
            type_label = ttk.Label(root, text='type:', background="#76b5c5")
            type_label.grid(column=0, row=7, padx=16, sticky='W')

            type_var = ttk.StringVar()
            type_entry = ttk.Entry(root, width=25, textvariable=type_var)
            type_entry.insert(0, student.studyType)
            type_entry.grid(column=1, row=7, sticky='W', pady=10)

            credits_label = ttk.Label(root, text='credits:', background="#76b5c5")
            credits_label.grid(column=0, row=8, padx=16, sticky='W')
            
            credits_var = ttk.IntVar()
            credits_entry = ttk.Entry(root, width=25, textvariable=credits_var)
            credits_entry.insert(0, student.credits)
            credits_entry.grid(column=1, row=8, sticky='W', pady=10)

            scholarship_label = ttk.Label(root, text='scholarship:', background="#76b5c5")
            scholarship_label.grid(column=0, row=9, padx=16, sticky='W')

            scholarship_var = ttk.DoubleVar()
            scholarship_entry = ttk.Entry(root, width=25, textvariable=scholarship_var)
            scholarship_entry.delete(0, 'end')
            scholarship_entry.insert(0, student.scholarship)
            scholarship_entry.grid(column=1, row=9, sticky='W', pady=10)

            deduction_label = ttk.Label(root, text='deduction:', background="#76b5c5")
            deduction_label.grid(column=0, row=10, padx=16, sticky='W')

            deduction_var = ttk.StringVar()
            deduction_entry = ttk.Entry(root, width=25, text='entry', textvariable=deduction_var)
            deduction_entry.insert(0, student.deduction)
            deduction_entry.grid(column=1, row=10, sticky='W', pady=10)

            update_button = tk.Button(root, text='update', background="#76b5c5", width=10, height=2, command=update)
            update_button.grid(column=0, row=12, padx=20, pady=20)

            close_button = tk.Button(root, text='close', background="#76b5c5", width=10, height=2, command=close)
            close_button.grid(column=1, row=12, padx=10, pady=20, sticky='E')

            root.configure(background="#76b5c5")
            root.mainloop()

class slipScreen:
     def __init__(self, parent, student):
            self.parent = parent
            
            def close():
                root.destroy()

            root = tk.Toplevel(self.parent)
            root.title(f"{student.name}'s slip report")
            root.geometry('475x250')
            root.resizable(0, 0)

            title_label = ttk.Label(root, text='tuition slip:', font='Calibri 22 bold', background="#76b5c5")
            title_label.grid(column=0, row=0, columnspan=4, padx=15, sticky='W', pady=20)

            credits_label = ttk.Label(root, text='credits:', background="#76b5c5", width=15, font='Calibri 12 bold')
            credits_label.grid(column=0, row=1, padx=15)
            credits_var = ttk.Label(root, text=student.credits, background="#76b5c5", foreground='#ff0000', width=5, font='Calibri 12')
            credits_var.grid(column=1, row=1, sticky='NE', padx=10)

            payper_label = ttk.Label(root, text='pay per credit:', background="#76b5c5", width=15, font='Calibri 12 bold')
            payper_label.grid(column=2, row=1, padx=20)
            payper_var = ttk.Label(root, text=f'${student.payPerCredit}', background="#76b5c5", foreground='#ff0000', font='Calibri 12')
            payper_var.grid(column=3, row=1, padx=10, sticky='W')

            fee_total_label = ttk.Label(root, text='total fee:', background="#76b5c5", width=15, font='Calibri 12 bold')
            fee_total_label.grid(column=0, row=2, padx=15, pady=10)
            fee_total_var = ttk.Label(root, text=f'${student.totalFee}', background="#76b5c5", foreground='#ff0000', width=5, font='Calibri 12')
            fee_total_var.grid(column=1, row=2, sticky='NE', padx=10, pady=10)

            scholarship_label = ttk.Label(root, text='scholarship', background="#76b5c5", width=15, font='Calibri 12 bold')
            scholarship_label.grid(column=2, row=2, padx=20, pady=10)
            scholarship_var = ttk.Label(root, text=f'${student.scholarship}', background="#76b5c5", foreground='#ff0000', font='Calibri 12')
            scholarship_var.grid(column=3, row=2, padx=10, sticky='W', pady=10)

            fee_net_label = ttk.Label(root, text='net fee:', background="#76b5c5", width=15, font='Calibri 12 bold')
            fee_net_label.grid(column=0, row=3, padx=15)
            fee_net_var = ttk.Label(root, text=f'${student.netFee}', background="#76b5c5", foreground='#ff0000', width=5, font='Calibri 12')
            fee_net_var.grid(column=1, row=3, sticky='NE', padx=10)

            deduction_label = ttk.Label(root, text='deduction:', background="#76b5c5", width=15, font='Calibri 12 bold')
            deduction_label.grid(column=2, row=3, padx=20)
            deduction_var = ttk.Label(root, text=f'${student.deductionAmount}', background="#76b5c5", foreground='#ff0000', font='Calibri 12')
            deduction_var.grid(column=3, row=3, padx=10, sticky='W')


            close_button = tk.Button(root, text='close', width=10, height=2, command=close)
            close_button.grid(column=2, row=4, pady=20, sticky='SW')

            root.configure(background="#76b5c5")
            root.mainloop()

class reportScreen:
     def __init__(self, parent):
            self.parent = parent

            def all_tuition():
                total = 0
                
                for i in range(len(students.students)):
                    total += int(students.students[i].totalFee)

                return f'${total}'
            
            def all_scholarship():
                total = 0

                for i in range(len(students.students)):
                        total += int(students.students[i].scholarship)
                
                return f'${total}'
            
            def all_net_fee():
                total = 0
                
                for i in range(len(students.students)):
                     total += int(students.students[i].netFee)
                
                return f'${total}'
            
            def all_deduction():
                total = 0
                
                for i in range(len(students.students)):
                    total += int(students.students[i].deductionAmount)

                return f'${total}'
            
            def all_bas():
                total = 0

                for i in range(len(students.students)):
                     total += int(students.students[i].bas)
                
                return f'${total}'
            
            def close():
                root.destroy()

            root = tk.Toplevel(self.parent)
            root.title('tms report')

            tuition_table = ttk.Treeview(root)
            tuition_table['columns'] = ['name', 'tuition', 'scholarship', 'deduction', 'net fee']

            tuition_table.column('#0', width=0, minwidth=0, stretch=False)
            tuition_table.heading("name", text="Name")
            tuition_table.column("name", anchor="w", width=100)
            tuition_table.heading("tuition", text="Tuition")
            tuition_table.column("tuition", anchor="w", width=100)
            tuition_table.heading("scholarship", text="Scholarship")
            tuition_table.column("scholarship", anchor="w", width=200)
            tuition_table.heading("deduction", text="Deduction")
            tuition_table.column("deduction", anchor="w", width=100)
            tuition_table.heading("net fee", text="Net fee")
            tuition_table.column("net fee", anchor="w", width=200)

            for i in range(len(students.students)):
                 tuition_table.insert(parent='', index='end', iid=i, values=(students.students[i].name, 
                                                                             f'${students.students[i].totalFee}', 
                                                                             f'${students.students[i].scholarship}', 
                                                                             f'${students.students[i].deductionAmount}',
                                                                             f'${students.students[i].netFee}'))
                 
            tuition_table.grid(column=0, row=0, padx=10, pady=10, columnspan=8)

            total_tuition_label = ttk.Label(root, text='tuition total:', background="#76b5c5")
            total_tuition_label.grid(column=2, row=1, sticky='W')
            total_tuition_var = ttk.Label(root, text=all_tuition(), background="#76b5c5", foreground='#ff0000', font='Calibri 12')
            total_tuition_var.grid(column=3, row=1, sticky='W')

            total_scholarship_label = ttk.Label(root, text='scholarship total: ', background="#76b5c5")
            total_scholarship_label.grid(column=4, row=1, sticky='W')
            total_scholarship_var = ttk.Label(root, text=all_scholarship(), background="#76b5c5", foreground='#ff0000', font='Calibri 12')
            total_scholarship_var.grid(column=5, row=1, sticky='W')

            total_net_fee_label = ttk.Label(root, text='net fee total:', background="#76b5c5")
            total_net_fee_label.grid(column=2, row=2, sticky='W')
            total_net_fee_var = ttk.Label(root, text=all_net_fee(), background="#76b5c5", foreground='#ff0000', font='Calibri 12')
            total_net_fee_var.grid(column=3, row=2, sticky='W')

            total_deduction_label = ttk.Label(root, text='deduction total:', background="#76b5c5")
            total_deduction_label.grid(column=4, row=2, sticky='W')
            total_deduction_var = ttk.Label(root, text=all_deduction(), background="#76b5c5", foreground='#ff0000', font='Calibri 12')
            total_deduction_var.grid(column=5, row=2, sticky='W')

            total_bas_label = ttk.Label(root, text='bas total:', background="#76b5c5")
            total_bas_label.grid(column=2, row=3, sticky='W')
            total_bas_var = ttk.Label(root, text=all_bas(), background="#76b5c5", foreground='#ff0000', font='Calibri 12')
            total_bas_var.grid(column=3, row=3, sticky='W')

            close_button = tk.Button(root, text='close', width=10, height=2, command=close)
            close_button.grid(column=6, row=5, sticky='W', pady=30)

            root.configure(background="#76b5c5")
            root.mainloop()

class logoutScreen:
     def __init__(self):
            def close():
                root.destroy()

            root = tk.Tk()
            root.title('goodnight')
            root.geometry('500x300')
            root.resizable(0, 0)

            logging_label = ttk.Label(root, text='Logging Off', font='Calibri 14 bold', background="#76b5c5")
            logging_label.place(x=213, y=120)
            goodnight_label = ttk.Label(root, text='goodnight', font='Calibri 14 bold', background="#76b5c5")
            goodnight_label.place(x=218, y=160)

            root.after(4000, lambda: close())

            root.configure(background="#76b5c5")
            root.mainloop()
            
def main():
    loginScreen()

if __name__ == '__main__':
    main()
